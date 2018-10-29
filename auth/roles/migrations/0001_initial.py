# Generated by Django 2.1.1 on 2018-10-29 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permissions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='')),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_time', models.DateTimeField(auto_now_add=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roles.Role')),
            ],
            options={
                'db_table': 'role_permission',
            },
        ),
        migrations.AddField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(through='roles.RolePermission', to='permissions.Permission'),
        ),
    ]