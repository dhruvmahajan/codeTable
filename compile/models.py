from django.db import models

# Create your models here.

LANG_CHOICES = [
				('C', 'C'),
				('CPP', 'CPP'),
				('PYTHON', 'PYTHON'),
			]

class Code(models.Model):
	code_id = models.CharField(max_length=20, primary_key=True)
	source_code = models.TextField()
	lang = models.CharField(choices=LANG_CHOICES, max_length=20, default='C')
	compiled_on = models.DateTimeField(auto_now_add=True)
	last_saved_on = models.DateTimeField(auto_now=True, null=True)
	compile_status = models.TextField(null=True)
	time_used = models.FloatField(default=0)
	memory_used = models.IntegerField(default=64)
	status = models.CharField(max_length=20, null=True)
	status_detail = models.CharField(max_length=20, null=True)
	user_input = models.TextField(null=True)
	output = models.TextField(null=True)
	output_html = models.TextField(null=True)
	stderr = models.TextField(null=True)

	def __str__(self):
		return self.code_id

	class Meta:
		ordering=('-compiled_on',)