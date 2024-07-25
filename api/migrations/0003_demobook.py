# Generated by Django 5.0.3 on 2024-07-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_emailsubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('contacted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]