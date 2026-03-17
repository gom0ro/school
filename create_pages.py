import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Page

pages_data = [
    {'title': 'Мектеп тарихы', 'slug': 'history', 'content': 'Мектеп тарихы туралы ақпарат осында болады.'},
    {'title': 'Мектеп әкімшілігі', 'slug': 'administration', 'content': 'Мектеп әкімшілігі туралы ақпарат осында болады.'},
    {'title': 'Оқу орынбасарлары', 'slug': 'deputies', 'content': 'Оқу орынбасарлары туралы ақпарат осында болады.'},
    {'title': 'Нормативтік құжаттар', 'slug': 'normative', 'content': 'Нормативтік құжаттар тізімі осында болады.'},
    {'title': 'Бухгалтерия', 'slug': 'accounting', 'content': 'Бухгалтерия туралы ақпарат осында болады.'},
    {'title': 'Материалдық техникалық база', 'slug': 'facilities', 'content': 'Материалдық техникалық база туралы ақпарат осында болады.'}
]

for p in pages_data:
    page, created = Page.objects.get_or_create(slug=p['slug'], defaults={'title': p['title'], 'content': p['content']})
    print(f"Page '{page.title}' {'created' if created else 'already exists'}.")

print('All pages processed successfully!')
