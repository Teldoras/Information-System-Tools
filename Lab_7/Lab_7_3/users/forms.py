from django import forms
import datetime

# объявляем форму с именем NameForm
# принадлежащую классу Form
class NameForm(forms.Form):
    # форма имеет одно поле, строкового типа
    # имеет подпись - label
    # имеет максимальную длину 100 символов
    user_name = forms.CharField(label='The username contains:',
                                max_length=100)


class DateForm(forms.Form):
    user_date_1 = forms.DateField(label='The date of birth from:',
                                  widget=forms.DateInput(
                                      attrs={'type': 'date'}),
                                  required=False,
                                  initial=datetime.date(year=1900, month=1, day=1)
                                  )
    user_date_2 = forms.DateField(label='The date of birth to:',
                                  widget=forms.DateInput(
                                      attrs={'type': 'date'}),
                                  required=False,
                                  initial=datetime.date(day=1, month=1, year=2000)
                                  )


class ChoiceForm(forms.Form):
    user_choice = forms.ChoiceField(label='Search users by:', choices=[('Name', 'Name'), ('Date', 'Date')])
