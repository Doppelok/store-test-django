# Generated by Django 4.1.6 on 2023-02-15 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=122)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_db.group')),
            ],
        ),
        migrations.CreateModel(
            name='NVRCameraParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(choices=[('16ch', 16), ('32ch', 32)], default='N/A', max_length=10)),
                ('hdd', models.CharField(choices=[('2 HDD', 2), ('4 HDD', 4)], default='N/A', max_length=10)),
                ('poe', models.CharField(choices=[('8ch', 8), ('16ch', 16)], default='N/A', max_length=10)),
                ('nvr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_db.person')),
            ],
        ),
        migrations.CreateModel(
            name='IpCameraParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.CharField(choices=[('5MP', 5), ('2MP', 2)], default='N/A', max_length=10)),
                ('case', models.CharField(choices=[('box', 'bullet'), ('dome', 'dome')], default='N/A', max_length=10)),
                ('lens', models.CharField(choices=[('2.8mm', 2.8), ('4mm', 4)], default='N/A', max_length=10)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_db.person')),
            ],
        ),
    ]