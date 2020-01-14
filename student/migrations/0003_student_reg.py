# Generated by Django 3.0.1 on 2020-01-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0002_delete_student_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_reg',
            fields=[
                ('admission_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('batch', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('admissn_date', models.CharField(max_length=200, null=True)),
                ('blood_grp', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('religion', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'student_registration',
            },
        ),
    ]