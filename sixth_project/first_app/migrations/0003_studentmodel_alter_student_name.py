# Generated by Django 4.2.3 on 2023-08-09 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_student_father_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]