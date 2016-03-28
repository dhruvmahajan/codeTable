from django.db import models

# Create your models here.

class Code(models.Model):
	code_id = models.CharField(max_length=20, primary_key=True)
	source_code = models.CharField(max_length=20000)
	LANG_CHOICES = (
            ('C', 'C'),
			('CPP', 'CPP'),
			('PYTHON', 'PYTHON'),
    )
	lang = models.CharField(choices=LANG_CHOICES, max_length=20, default='C')
	compiled_on = models.DateTimeField(auto_now_add=True)
	last_saved_on = models.DateTimeField(auto_now=True)
	compile_status = models.CharField(max_length=20000)

