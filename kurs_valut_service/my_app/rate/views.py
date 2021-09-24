from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Rate, date_now, get_rates
from .forms import *
import psycopg2


def create_connection(db_name, db_user, db_password, db_host, db_port):
    con = None
    try:
        con = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    return con


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")


conn = create_connection(
    'ratenow', 'khan3290', 'khan12985', '127.0.0.1', '5432'
)
delete_comment = 'delete from "public".rate_rate'
execute_query(conn, delete_comment)


result = get_rates()
length = len(result)
data_rate = []
for l in range(length):
    data_rate.append({'digital_code': result[l]['r030'],
                      'letter_code': result[l]['cc'],
                      'rate_name': result[l]['txt'],
                      'official_rate': result[l]['rate']})

for el in data_rate:
    Rate.objects.create(**el)


class RateList(View):

    def get(self, request):

        context = {
            'title': 'Rate now',
            'head_text': 'Офіційний курс гривні щодо іноземних валют',
            'date': f'на дату {date_now}',
            'rates': Rate.objects.all()
        }

        return render(request, 'rate/rate_now.html', context)


class Registrator(View):

    def get(self, request):

        context = {
            'title': 'Registration',
            'form': UserCreationForm()
        }

        return render(request, 'rate/registration.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Реєстрація пройшла успішно!')
            return redirect('login')
        messages.error(request, 'Помилка реєстрації!')
        return render(request, 'rate/registration.html', {'form': form})


class Login(View):

    def get(self, request):

        context = {
            'title': 'Login',
            'form': LoginForm()
        }

        return render(request, 'rate/login.html', context)

    def post(self, request):

        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.get_user()
            login(request, username)
            messages.success(request, f'Ласкаво просимо, {username}')
            return redirect('main')
        messages.error(request, 'Помилка входу!')
        return render(request, 'rate/login.html', {'form': form})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('login')


def main_page(request):

    context = {
        'title': 'Main page',
    }

    return render(request, 'rate/index.html', context)
