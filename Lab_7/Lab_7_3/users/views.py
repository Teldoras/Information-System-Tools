from django.shortcuts import render
from django.http import HttpResponseRedirect
from manage import cursor
from .forms import NameForm, DateForm, ChoiceForm
from .models import SearchingUsers, ChoosingFilter


# создание формы ввода
def get_name(request):
    # если это запрос POST, нам нужно обработать данные формы
    print('Получен метод запроса 2.1: ', request.method)
    if request.method == 'POST':
        # создать экземпляр формы и заполнить данным из web-запроса
        form_2 = NameForm(request.POST)
        print('Сырые данные: ', request.POST)
        if form_2.is_valid():
            print('Введенное значение: ', form_2.cleaned_data['user_name'])
            # сохраним значение из формы в модель данных django
            SearchingUsers.ByName = form_2.cleaned_data['user_name']
            # перенаправляем по адресу search
            return HttpResponseRedirect('search_by_name/results')
        else:
            print('Form 2 name is not valid')
    # Если GET (или любой другой метод), мы создадим пустую форму
    else:
        form_2 = NameForm()
    return render(request, 'users/search.html', {'form_2': form_2})


def get_date(request):
    print('Получен метод запроса 2.2: ', request.method)
    if request.method == 'POST':
        form_2 = DateForm(request.POST)
        print('Сырые данные: ', request.POST)
        if form_2.is_valid():
            print('Введенное значение: ', form_2.cleaned_data['user_date_1'], form_2.cleaned_data['user_date_2'])
            SearchingUsers.ByDate = [form_2.cleaned_data['user_date_1'], form_2.cleaned_data['user_date_2']]
            return HttpResponseRedirect('search_by_date/results')
        else:
            print('Form 2 date is not valid')

    else:
        form_2 = DateForm()
    return render(request, 'users/search.html', {'form_2': form_2})


# запрос данных из БД
def user_by_name(request):
    print('Получили: ', SearchingUsers.ByName)
    # получим значение из модели и обрамляем в % так как будем искать вхождение подстроки
    substring = '%' + SearchingUsers.ByName + '%'
    # формирование запроса
    sql = "select first_name, last_name, date_of_birth from user where first_name like %s order by first_name"
    # выполнение запроса к БД
    cursor.execute(sql, substring)
    # объявление пустого списка
    user_info = list()
    # формируем список из подсписков,
    # где один подсписок - имя, фамилия, дата рождения.
    for r in cursor:
        #print(r[0], r[1], '\t', r[2])
        #user_info = str(r[0]) + str(r[1]) + str(r[2])
        sublist = [[r[0], r[1], str(r[2])]]
        user_info += sublist
    # открываем страницу с результатами
    return render(request, 'users/results.html', {'user': user_info, 'substring': substring})


def user_by_date(request):
    print('Получили: ', SearchingUsers.ByDate[0], SearchingUsers.ByDate[1])
    start_date = str(SearchingUsers.ByDate[0])
    end_date = str(SearchingUsers.ByDate[1])
    sql = ("select first_name, last_name, date_of_birth from user where (date_of_birth between '"
           + start_date + "' and '" + end_date + "') order by date_of_birth")
    cursor.execute(sql)
    user_info = list()
    for r in cursor:
        sublist = [[r[0], r[1], str(r[2])]]
        user_info += sublist
    return render(request, 'users/results.html',
                  {'user': user_info, 'substring': 'from ' +start_date + ' to ' + end_date})


def get_filter(request):
    print('Получен метод запроса 1: ', request.method)
    if request.method == 'POST':
        form_1 = ChoiceForm(request.POST)
        print('Сырые данные: ', request.POST)
        if form_1.is_valid():
            print('Введенное значение: ', form_1.cleaned_data['user_choice'])
            ChoosingFilter.filter_type = form_1.cleaned_data['user_choice'].lower()
            return HttpResponseRedirect('search_by_' + ChoosingFilter.filter_type)
        else:
            print('Form 1 is not valid')
    else:
        form_1 = ChoiceForm()
    return render(request, 'users/index.html', {'form_1': form_1})
