from django.shortcuts import render
from django.views.generic import TemplateView
from birthday.models import Birthday


class HomePage(TemplateView):
    template_name = 'pages/index.html'

    # переопределение контекста наследуемого класса TemplateView
    def get_context_data(self, **kwargs):
        # получаем словарь context из родительского метода
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь ключ total_count
        # значение ключа - кол-во объектов в модели Birthday
        context['total_count'] = Birthday.objects.count()
        return context
