import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Page

pages_data = [
    {'title': 'Біртұтас тәрбие бағыты', 'slug': 'birtutas-tarbie', 'content': 'Ақпарат осында болады.'},
    {'title': 'Тәрбие жұмысының жылдық жоспары', 'slug': 'tarbie-zhospary', 'content': 'Ақпарат осында болады.'},
    {'title': 'Тәрбие құндылықтары бойынша іс-шаралар', 'slug': 'tarbie-sharalar', 'content': 'Ақпарат осында болады.'},
    {'title': 'Ата-аналарға педагогикалық қолдау орталығы', 'slug': 'ata-analar-ortalygy', 'content': 'Ақпарат осында болады.'},
    {'title': 'Құқықбұзушылықтың алдын алу жұмыстары', 'slug': 'quqyq-aldyn-alu', 'content': 'Ақпарат осында болады.'},
    {'title': 'Профилактикалық кеңес', 'slug': 'profilaktika', 'content': 'Ақпарат осында болады.'},
    {'title': 'Сынып жетекшілер әдістемелік бірлестік жетекшілердің құжаттары', 'slug': 'synyp-zhetekshiler', 'content': 'Ақпарат осында болады.'},
    {'title': 'Мектеп парламенті', 'slug': 'mektep-parlamenti', 'content': 'Ақпарат осында болады.'},
    {'title': 'Адал ұрпақ', 'slug': 'adal-urpaq', 'content': 'Ақпарат осында болады.'},
    {'title': 'Жас ұлан', 'slug': 'zhas-ulan', 'content': 'Ақпарат осында болады.'}
]

for p in pages_data:
    page, created = Page.objects.get_or_create(slug=p['slug'], defaults={'title': p['title'], 'content': p['content']})
    print(f"Page '{page.title}' {'created' if created else 'already exists'}.")

print('All pages processed successfully!')
