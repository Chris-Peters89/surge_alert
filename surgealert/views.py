from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	downtown = {'start_latitude':'42.358360','start_longitude':'-71.061029','end_latitude':'42.354808','end_longitude':'-71.061373'}
	cambridge = {'start_latitude':'42.373616','start_longitude':'-71.109734','end_latitude':'42.374131','end_longitude':'-71.113880'}
	southie = {'start_latitude':'42.341106','start_longitude':'-71.048584','end_latitude':'42.334825','end_longitude':'-71.044207'}
	arlington = {'start_latitude':'42.417377','start_longitude':'-71.159542','end_latitude':'42.415286','end_longitude':'-71.156194'}
	chrisIvyHome = {'start_latitude':'42.303296','start_longitude':'-71.058648','end_latitude':'42.301646','end_longitude':'-71.057317'}
	medford = {'start_latitude':'42.422905','start_longitude':'-71.115875','end_latitude':'42.420830','end_longitude':'-71.112871'}
	unionSqr = {'start_latitude':'42.380377','start_longitude':'-71.096241','end_latitude':'42.379505','end_longitude':'-71.095812'}
	eastBoston = {'start_latitude':'42.395394','start_longitude':'-71.004982','end_latitude':'42.384364','end_longitude':'-71.012192'}
	

	cities = []
	cities.append(downtown)
	cities.append(cambridge)
	cities.append(southie)
	cities.append(arlington)
	cities.append(chrisIvyHome)
	cities.append(medford)
	cities.append(unionSqr)
	cities.append(eastBoston)
	info = ''
	names = ["Downtown","Harvard Square","Southie","English Central","Fields Corner","Medford","Union Square","East Boston"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token zg2ae9j7NeRVcvToCH0rBbMIbXmmwddEjl2YEuh3'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['prices'][0]['display_name']) + '    '
		info = info + str((data['prices'][0]['surge_multiplier'])) + '  <br/><br/>'	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

