from django.shortcuts import render

from django import forms
from django_ace import AceWidget


Languages = [
				('C', 'C'),
				('CPP', 'CPP'),
				('PYTHON', 'PYTHON'),
			]

class EditorForm(forms.Form):
    sourceCode = forms.CharField( widget=forms.Textarea(attrs={'cols': 150, 'rows': 20}))
    lang = forms.ChoiceField(choices=Languages)
    customInput = forms.CharField( widget=forms.Textarea(attrs={'cols': 50, 'rows': 20}), required=False)


def runCode(request, run_id):

	print('testing before submit')
	form = EditorForm(request.POST or None)
	if form.is_valid():
		print('testing after submit')

		#---------------------HE_API------------------------------------------
		import requests

		# constants
		RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
		CLIENT_SECRET = '66cbe706e0538bc8599cd99f3825ee74f6c02d38'

		data = {
		    'client_secret': CLIENT_SECRET,
		    'async': 0,
		    'source': form.cleaned_data.get('sourceCode'),
		    'lang': form.cleaned_data.get('lang'),
		    'input': form.cleaned_data.get('customInput'),
		    'time_limit': 5,
		    'memory_limit': 262144,
		}

		r = requests.post(RUN_URL, data=data)
		resultJson = r.json()
		print(resultJson)
		
		
		context = { "form": form, "output": resultJson['run_status']['output']  }

		return render(request, "code.html", context)

	#---------------------HE_API ends------------------------------------------

	context = { "form": form,   }

	return render(request, "code.html", context)






# Create your views here.
