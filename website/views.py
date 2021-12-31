from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
	return render(request, 'index.html', {})


def apitest(request):
	# url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

	# querystring = {"type":"get-movies-by-title","title":"matrix"}

	# headers = {
	#     'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
	#     'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	#     }

	# response = requests.request("GET", url, headers=headers, params=querystring)
	# popular = json.loads(response.content)

	url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

	querystring = {"type":"get-random-movies","page":"2"}

	headers = {
	    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
	    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)
	results = json.loads(response.content)

	
	return render(request, 'apitesting.html', {'results': results})