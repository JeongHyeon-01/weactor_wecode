# Generated by Django 4.0.3 on 2022-03-14 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_actor', '0002_alter_actors_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcMv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'actor_movie',
            },
        ),
        migrations.AlterField(
            model_name='actors',
            name='movies',
            field=models.ManyToManyField(related_name='actor_movie', through='movies_actor.AcMv', to='movies_actor.movie'),
        ),
        migrations.AddField(
            model_name='acmv',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_actor.actors'),
        ),
        migrations.AddField(
            model_name='acmv',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_actor.movie'),
        ),
    ]
