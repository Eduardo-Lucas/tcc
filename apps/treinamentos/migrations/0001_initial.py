# Generated by Django 2.2.6 on 2019-10-03 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0003_auto_20191003_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treinamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treinamento', models.CharField(max_length=50)),
                ('imagem', models.ImageField(blank=True, upload_to='treinamentos')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa')),
            ],
        ),
    ]
