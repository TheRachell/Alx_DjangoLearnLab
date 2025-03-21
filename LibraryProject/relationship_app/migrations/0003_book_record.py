# Generated by Django 5.1.1 on 2025-03-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
            ],
            options={
                'permissions': [('can_add_book', 'can add a new book'), ('can_change_book', 'Can change book details'), ('can_delete_book', 'Can delete a book')],
            },
        ),
    ]
