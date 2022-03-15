import json
from django.http import JsonResponse
from django.views import View
from .models import Actors,Movie
from django.shortcuts import render
# Create your views here.
class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actors.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            date_of_birth = data['birth'],
        )
        return JsonResponse({'message':'created'}, status=201)
    def get(self, requets):
        actors = Actors.objects.all()
        result = []
        for actor in actors:
            result.append(
                {
                    'name' : actor.last_name + ' '+ actor.first_name,
                    'Filmography' : [{"movie":movie.title} for movie in actor.movies.all()]
                }
            )
        return JsonResponse({'results':result}, status=200)
            


class MovieView(View):
    def post(self, requets):
        data =json.loads(requets.body)
        Movie.objects.create(
            title = data['title'],
            running_time = data['running_time'],
            relese_date = data['relese']
        )
        return JsonResponse({'message':'created'}, status=201)
    def get (self, requets):
        movies = Movie.objects.all()
        result = [] 
        for movie in movies:
            result.append({
                'title':movie.title,
                'running_time':movie.running_time
            })
        return JsonResponse({'results':result},status=200)


class AcMv(View):
    def post(self, request):
        data = json.loads(request.body)
        #Actor 에서 중간테이블이 movies이기때문에 바로불러올수있다.
        Ac = Actors.objects.get(last_name=data['last_name'])
        Mv = Movie.objects.get(title=data['title'])
        Ac.movies.add(Mv)

        # 역으로 참조하면
        # Mv.movies_set.all(Ac)

        return JsonResponse({'message':'created'}, status=201)