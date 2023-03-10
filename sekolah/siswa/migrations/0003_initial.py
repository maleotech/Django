# Generated by Django 4.1.4 on 2023-02-21 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('siswa', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('alamat', models.CharField(blank=True, max_length=100, null=True)),
                ('nisn', models.CharField(default='0', max_length=10)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('kelas', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
