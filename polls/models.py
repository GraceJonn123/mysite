from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	def __str__(self):
		return self.choice_text
