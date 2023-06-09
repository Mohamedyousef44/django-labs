# Generated by Django 4.2.1 on 2023-05-27 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_category_isbn_alter_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.OneToOneField(default=150, on_delete=django.db.models.deletion.CASCADE, to='home.isbn'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=150, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
