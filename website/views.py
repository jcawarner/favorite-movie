from django.shortcuts import render, redirect
import requests
import json
from website.models import Movie

headers = {
	    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
	    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	    }

# Create your views here.
def home(request):
	return render(request, 'index.html', {})


def popular(request):

	url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	querystring = {"type":"get-popular-movies","page":"1","year":"2020"}

	response = requests.request("GET", url, headers=headers, params=querystring)
	results = json.loads(response.content)

	# retrieve image id from random list
	image_list = []
	for movie in results['movie_results']:
		image_list.append(movie['imdb_id'])

	# get image for each random result
	image_source = []
	for image_id in image_list:

		# Get image results from API
		image_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
		image_querystring = {f"type":"get-movies-images-by-imdb","imdb":{image_id}}
		image_response = requests.request("GET", image_url, headers=headers, params=image_querystring)
		image_results = json.loads(image_response.content)
		image_source.append(image_results['poster'])

	# get movie details
	details_list = []
	details_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	for detail in image_list:
		details_querystring = {f"type":"get-movie-details","imdb":{detail}}
		details_response = requests.request("GET", details_url, headers=headers, params=details_querystring)
		details_results = json.loads(details_response.content)
		details_list.append(details_results)

	movie_list = zip(image_source, details_list)

	return render(request, 'popular.html', {'results': results, 'image':image_results, 'image_list': image_list, 'details':details_list, 'image_source':image_source, 'movie':movie_list})



def random_movies(request):

	
	# Get random results from API
	random_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	random_querystring = {"type":"get-random-movies","page":"1"}
	random_response = requests.request("GET", random_url, headers=headers, params=random_querystring)
	random_results = json.loads(random_response.content)

	# retrieve image id from random list
	image_list = []
	for movie in random_results['movie_results']:
		image_list.append(movie['imdb_id'])

	# get image for each random result
	image_source = []
	for image_id in image_list:

		# Get image results from API
		image_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
		image_querystring = {f"type":"get-movies-images-by-imdb","imdb":{image_id}}
		image_response = requests.request("GET", image_url, headers=headers, params=image_querystring)
		image_results = json.loads(image_response.content)
		image_source.append(image_results['poster'])

	# get movie details
	details_list = []
	details_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	for detail in image_list:
		details_querystring = {f"type":"get-movie-details","imdb":{detail}}
		details_response = requests.request("GET", details_url, headers=headers, params=details_querystring)
		details_results = json.loads(details_response.content)
		details_list.append(details_results)

	movie_list = zip(image_source, details_list)

	return render(request, 'random.html', {'results': random_results, 'image':image_results, 'image_list': image_list, 'details':details_list, 'image_source':image_source, 'movie':movie_list})


def trending(request):

	url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	querystring = {"type":"get-trending-movies","page":"1"}

	response = requests.request("GET", url, headers=headers, params=querystring)
	results = json.loads(response.content)

	# retrieve image id from random list
	image_list = []
	for movie in results['movie_results']:
		image_list.append(movie['imdb_id'])

	# get image for each random result
	image_source = []
	for image_id in image_list:

		# Get image results from API
		image_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
		image_querystring = {f"type":"get-movies-images-by-imdb","imdb":{image_id}}
		image_response = requests.request("GET", image_url, headers=headers, params=image_querystring)
		image_results = json.loads(image_response.content)
		image_source.append(image_results['poster'])

	# get movie details
	details_list = []
	details_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	for detail in image_list:
		details_querystring = {f"type":"get-movie-details","imdb":{detail}}
		details_response = requests.request("GET", details_url, headers=headers, params=details_querystring)
		details_results = json.loads(details_response.content)
		details_list.append(details_results)

	movie_list = zip(image_source, details_list)

	return render(request, 'trending.html', {'results': results, 'image':image_results, 'image_list': image_list, 'details':details_list, 'image_source':image_source, 'movie':movie_list})



def now_playing(request):
	url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

	querystring = {"type":"get-trending-movies","page":"1"}

	response = requests.request("GET", url, headers=headers, params=querystring)
	results = json.loads(response.content)

	# retrieve image id from random list
	image_list = []
	for movie in results['movie_results']:
		image_list.append(movie['imdb_id'])

	# get image for each random result
	image_source = []
	for image_id in image_list:

		# Get image results from API
		image_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
		image_querystring = {f"type":"get-movies-images-by-imdb","imdb":{image_id}}
		image_response = requests.request("GET", image_url, headers=headers, params=image_querystring)
		image_results = json.loads(image_response.content)
		image_source.append(image_results['poster'])

	# get movie details
	details_list = []
	details_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	for detail in image_list:
		details_querystring = {f"type":"get-movie-details","imdb":{detail}}
		details_response = requests.request("GET", details_url, headers=headers, params=details_querystring)
		details_results = json.loads(details_response.content)
		details_list.append(details_results)

	movie_list = zip(image_source, details_list)

	return render(request, 'now_playing.html', {'results': results, 'image':image_results, 'image_list': image_list, 'details':details_list, 'image_source':image_source, 'movie':movie_list})



def movie(request, id):
	headers = {
	    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
	    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	    }
	# request api for images
	image_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	image_querystring = {f"type":"get-movies-images-by-imdb","imdb":{id}}
	image_response = requests.request("GET", image_url, headers=headers, params=image_querystring)
	image_results = json.loads(image_response.content)
	main_image = image_results['poster']
	fan_image = image_results['fanart']

	# request api for movie details
	details_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	details_querystring = {f"type":"get-movie-details","imdb":{id}}
	details_response = requests.request("GET", details_url, headers=headers, params=details_querystring)
	details_results = json.loads(details_response.content)


	return render(request, 'movie.html', {'main_image':main_image, 'fanart':fan_image, 'details':details_results})

def save_movie(request, id):
	headers = {
	    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
	    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	    }

	# request api for movie details
	details_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	details_querystring = {f"type":"get-movie-details","imdb":{id}}
	details_response = requests.request("GET", details_url, headers=headers, params=details_querystring)
	details_results = json.loads(details_response.content)

	# request api for images
	image_url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
	image_querystring = {f"type":"get-movies-images-by-imdb","imdb":{id}}
	image_response = requests.request("GET", image_url, headers=headers, params=image_querystring)
	image_results = json.loads(image_response.content)
	main_image = image_results['poster']

	current_user = request.user
	m = Movie(movie_title=details_results['title'], movie_release_date=details_results['release_date'], rating=details_results['imdb_rating'], 
		runtime=details_results['runtime'], summary=details_results['description'], image = main_image, user=current_user)
	m.save()

	return redirect(account)


def account(request):
	current_user = request.user
	firstname = current_user.first_name
	lastname = current_user.last_name
	email = current_user.email
	
	movies = Movie.objects.all()
	saved_movie_list = []
	for movie in movies:
		if current_user == movie.user:
			saved_movie_list.append(movie) 

	return render(request, 'logged_in.html', {'firstname':firstname, 'lastname':lastname, 'email':email, 'movies':movies, 
		 'current_user':current_user, 'saved':saved_movie_list})
