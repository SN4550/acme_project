from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator

from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday


def birthday(request: HttpRequest, pk: int = None) -> HttpResponse:
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None
    form = BirthdayForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=instance)
    context: dict = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday'])
        context.update({'birthday_countdown': birthday_countdown})
    return render(request=request,
                  template_name='birthday/birthday.html',
                  context=context)


def birthday_list(request: HttpRequest) -> HttpResponse:
    birthdays = Birthday.objects.order_by('id')

    paginator = Paginator(birthdays, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context: dict = {'page_obj': page_obj}
    return render(request=request,
                  template_name='birthday/birthday_list.html',
                  context=context)


def delete_birthday(request: HttpRequest, pk: int) -> HttpResponse:
    instance = get_object_or_404(Birthday, pk=pk)
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    return render(request=request,
                  template_name='birthday/birthday.html',
                  context=context)
