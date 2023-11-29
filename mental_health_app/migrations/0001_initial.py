# Generated by Django 4.1.2 on 2023-11-29 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Missionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_president_comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('missionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mental_health_app.missionary')),
            ],
        ),
    ]
