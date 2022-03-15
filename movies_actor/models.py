from django.db import models

# Create your models here.
class Actors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    movies = models.ManyToManyField('Movie',through='AcMv',related_name='actor_movie')
    #through 사용이유 : 다대다 관계를 나타낼 때, custom 한 중개모델을 지정할 때 사용한다.through='AcMv'
    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=45)
    relese_date = models.DateField()
    running_time = models.IntegerField()
    
    class Meta:
        db_table = 'movies'


class AcMv(models.Model):
    actor=models.ForeignKey('Actors', on_delete=models.CASCADE)
    movie=models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actor_movie'