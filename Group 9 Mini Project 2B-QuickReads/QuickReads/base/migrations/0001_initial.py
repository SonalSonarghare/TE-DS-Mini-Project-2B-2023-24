# Generated by Django 4.2.5 on 2024-04-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Title_link', models.URLField()),
                ('Image', models.ImageField(upload_to='Image/')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Summary', models.TextField()),
                ('Content', models.TextField()),
                ('Field1', models.TextField()),
            ],
        ),
    ]