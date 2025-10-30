from django.shortcuts import render,redirect, get_object_or_404
from .models import Club, Staff, News
from .forms import ContactForm
from django.core.mail import send_mail

def index(request):
    # Получаем активные кружки и сотрудников
    clubs = Club.objects.filter(is_active=True).order_by('order')
    staff_members = Staff.objects.filter(is_active=True).order_by('order')
    news_list = News.objects.all().order_by('-date')  # Сортировка новостей по дате (сначала свежие)

    success = False  # флаг успешной отправки формы

    # Обработка формы контакта
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                f"Хабарлама от {cd['name']}",
                cd['message'],
                cd['email'],
                ['your_email@example.com'],  # замени на свою почту
                fail_silently=False,
            )
            success = True
            form = ContactForm()  # очистка формы после отправки
    else:
        form = ContactForm()

    context = {
        'clubs': clubs,
        'staff_members': staff_members,
        'news_list': news_list,  # добавляем новости в контекст
        'form': form,
        'success': success,
    }

    return render(request, 'index.html', context)

def contact_view(request):
    success = False  # флаг успешной отправки формы

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                f"Хабарлама от {cd['name']}",
                cd['message'],
                cd['email'],
                ['your_email@example.com'],  # замени на свою почту
                fail_silently=False,
            )
            success = True
            form = ContactForm()
        return redirect("success")  # очистка формы после отправки
    else:
        form = ContactForm()

    context = {
        'form': form,
        'success': success,
    }

    return render(request, 'contact.html', context)

def contact_success(request):
    
    return render(request, 'success.html')


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    clubs = Club.objects.filter(is_active=True)
    return render(request, 'news_detail.html', {'news': news, 'clubs': clubs})

def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    return render(request, 'club_detail.html', {'club': club})