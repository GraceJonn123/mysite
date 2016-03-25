import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		 return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	def __str__(self):
		return self.choice_text
