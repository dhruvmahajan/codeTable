from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django_ace import AceWidget
	
from compile.models import Code

from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings


class CodeTableForm(forms.Form):
    sourceCode = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))
    lang = forms.ChoiceField(choices=settings.LANG_CHOICES)
    customInput = forms.CharField( widget=forms.Textarea(attrs={'cols': 80, 'rows': 5}), required=False)


def he_api(sourceCode, lang, customInput):

	import requests

	data = {
	    'client_secret': settings.CLIENT_SECRET,
	    'async': 0,
	    'source': sourceCode,
	    'lang': lang,
	    'input': customInput,
	    'time_limit': 5,
	    'memory_limit': 262144,
	}

	r = requests.post(settings.RUN_URL, data=data)
	resultJson = r.json()
	return resultJson


def runNewCode(request, run_id=None, form=None):
	
	if form==None:
		form = CodeTableForm(request.POST or None)
 

	if form.is_valid() or run_id!=None:
				
		sourceCode = form.cleaned_data.get('sourceCode')
		lang = form.cleaned_data.get('lang')
		customInput = form.cleaned_data.get('customInput')

		# calling he_api

		resultJson = he_api(sourceCode, lang, customInput)
		
		print(resultJson)

		# if new run then we have to asign new run_id for it

		if run_id==None:
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

			C = Code(code_id=run_id,
					source_code=sourceCode,
					lang=lang,
					compile_status=compileStatus,
					time_used=timeUsed,
					memory_used=memoryUsed,
					status=status,
					status_detail=statusDetail,
					user_input=customInput,
					output=output,
					output_html=outputHtml,
					stderr=stderr
				) 
			C.save()
		else:
			C = Code(code_id=run_id,
					source_code=sourceCode,
					lang=lang,
					compile_status=compileStatus,
					status=status,
					status_detail=statusDetail,
					user_input=customInput
				) 
			C.save()

		context = { "form": form, 'run_id': run_id }
		return HttpResponseRedirect('/'+run_id)

	context = { "form": form, 
	
			  }

	return render(request, "code.html", context)


def runOldCode(request, run_id):

	try:
		q = Code.objects.get(pk=run_id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	form = CodeTableForm(request.POST or None, initial={'sourceCode':q.source_code, 'lang':	q.lang, 'customInput':q.user_input})

	if form.is_valid():
		q.delete()
		runNewCode(None, run_id, form)
		return HttpResponseRedirect('/'+run_id)


	context = { "form": form, 
				"output":q.output,
				"time":q.time_used,
				"memory":q.memory_used,
				"status":q.status,
				"status_detail":q.status_detail,
				"compile_status":q.compile_status,
				"compiled_on":q.compiled_on,
				"stderr":q.stderr,
								
				}

	return render(request, "code.html", context)


# Create your views here.
