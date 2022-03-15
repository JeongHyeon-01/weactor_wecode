# Generated by Django 4.0.3 on 2022-03-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_actor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='movies',
            field=models.ManyToManyField(related_name='actor_movie', to='movies_actor.movie'),
        ),
    ]
