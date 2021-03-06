# Generated by Django 3.0.5 on 2020-04-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodBooksApp', '0003_auto_20200428_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('user', 'book')},
        ),
    ]
