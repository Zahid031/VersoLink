# Generated by Django 5.1.3 on 2024-12-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_testimonial_rating_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyAskedQuesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
    ]