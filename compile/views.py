from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django_ace import AceWidget

from compile.models import Code

from django.core.exceptions import ObjectDoesNotExist

Languages = [
				('C', 'C'),
				('CPP', 'CPP'),
				('PYTHON', 'PYTHON'),
			]

class CodeTableForm(forms.Form):
    sourceCode = forms.CharField( widget=forms.Textarea(attrs={'cols': 150, 'rows': 20}))
    lang = forms.ChoiceField(choices=Languages)
    customInput = forms.CharField( widget=forms.Textarea(attrs={'cols': 50, 'rows': 20}), required=False)


def he_api(sourceCode, lang, customInput):

	import requests

	# constants
	RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
	CLIENT_SECRET = '66cbe706e0538bc8599cd99f3825ee74f6c02d38'

	data = {
	    'client_secret': CLIENT_SECRET,
	    'async': 0,
	    'source': sourceCode,
	    'lang': lang,
	    'input': customInput,
	    'time_limit': 5,
	    'memory_limit': 262144,
	}

	r = requests.post(RUN_URL, data=data)
	resultJson = r.json()
	return resultJson


def runNewCode(request):
	print('new run before submit')
	form = CodeTableForm(request.POST or None)
	if form.is_valid():
		print('new run after submit')

		# calling he_api

		sourceCode = form.cleaned_data.get('sourceCode')
		lang = form.cleaned_data.get('lang')
		customInput = form.cleaned_data.get('customInput')

		resultJson = he_api(sourceCode, lang, customInput)
		print(resultJson)

		run_id = resultJson['code_id']
		compileStatus = resultJson['compile_status']
		status = resultJson['run_status']['status']
		statusDetail = resultJson['run_status']['status_detail']

		if compileStatus=='OK':
			timeUsed = resultJson['run_status']['time_used']
			memoryUsed = resultJson['run_status']['memory_used']
			output = resultJson['run_status']['output']
			outputHtml = resultJson['run_status']['output_html']
			stderr = resultJson['run_status']['stderr']

			C = Code(code_id=run_id, source_code=sourceCode, lang=lang, compile_status=compileStatus, time_used=timeUsed,memory_used=memoryUsed, status=status, status_detail=statusDetail, user_input=customInput, output=output, output_html=outputHtml, stderr=stderr) 
			C.save()
		else:
			C = Code(code_id=run_id, source_code=sourceCode, lang=lang, compile_status=compileStatus, status=status, status_detail=statusDetail, user_input=customInput) 
			C.save()

		context = { "form": form, 'run_id': run_id }
		return HttpResponseRedirect(run_id+'/')

	context = { "form": form,   }

	return render(request, "code.html", context)


def runCode(request, run_id):

	print('runCode before submit')
	try:
		q = Code.objects.get(pk=run_id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/code/')

	form = CodeTableForm(request.POST or None, initial={'sourceCode':q.source_code, 'lang':	q.lang, 'customInput':q.user_input})

	if form.is_valid():
		print('runCode after submit')

		resultJson = he_api(form.cleaned_data.get('sourceCode'), form.cleaned_data.get('lang'), form.cleaned_data.get('customInput') )
		print(resultJson)

		context = { "form": form, "output": resultJson['run_status']['output'], 'run_id':run_id  }

		return render(request, "code.html", context)


	context = { "form": form, "output":q.output_html  }

	return render(request, "code.html", context)


# Create your views here.
