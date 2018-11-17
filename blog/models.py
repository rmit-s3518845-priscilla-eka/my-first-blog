# Create a blog post model

# import code from other python files
from django.conf import settings
from django.db import models
from django.utils import timezone

# defines a model called Post
# (class name starts with an uppercase letter)
# models.Model --> Post is a Django model so Django knows it should  be saved in the database
# models.CharField --> define text with a limited number of characters
# models.TextField --> long text without a limit
# models.DateTimeField --> date and time
# models.ForeignKey --> link to another model
class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

# method called publish
# (method names --> lowercase and underscores)
# Python is sensitive to whitespace so indent methods within class
	def publish(self):
		self.published_date = timezone.now()
		self.save()

# methods often return something
# calling _str_() returns a text string with a Post title
	def _str_(self):
		return self.title 

