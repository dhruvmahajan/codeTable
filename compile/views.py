from django.shortcuts import render


def runCode(request, run_id):

	print('dhruv mahajan testing')
	import requests

	# constants
	RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
	CLIENT_SECRET = '66cbe706e0538bc8599cd99f3825ee74f6c02d38'

	source = "print 'Hello World'"

	data = {
	    'client_secret': CLIENT_SECRET,
	    'async': 0,
	    'source': source,
	    'lang': "PYTHON",
	    'time_limit': 5,
	    'memory_limit': 262144,
	}

	r = requests.post(RUN_URL, data=data)
	print(r.json())
	#return render(request, "forms.html", context)





# Create your views here.
