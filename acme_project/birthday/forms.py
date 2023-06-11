from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(
        label='Имя', max_length=20)
    last_name = forms.CharField(
        label='Фамилия', help_text='Необязательное поле', required=False)
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'}))
    # title = forms.CharField(
    #     label='Название:', max_length=20, required=True)
    # description = forms.CharField(
    #     label='Описание:',
    #     required=True,
    #     widget=forms.Textarea(attrs={'type': 'text'}))
    # price = forms.IntegerField(
    #     label='Цена:',
    #     min_value=10,
    #     max_value=100,
    #     help_text='Рекомендованная розничная цена')
    # comment = forms.CharField(
    #     label='Комментарий:',
    #     required=False,
    #     widget=forms.Textarea(attrs={'type': 'text'}))
