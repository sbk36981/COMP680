# Generated by Django 2.0.3 on 2018-03-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=200)),
                ('request_date', models.DateTimeField(verbose_name='date published')),
                ('csv_data', models.TextField()),
                ('predicted_price', models.DecimalField(decimal_places=20, max_digits=20)),
                ('actual_price', models.DecimalField(decimal_places=20, max_digits=20)),
            ],
        ),
    ]