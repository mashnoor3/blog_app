from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

# Model for blog posts
class Post(models.Model):
    # Author is connected to a superuser on the website
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(blank=True, null=True) #could be blank and could be left empty

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def approved_comments(self):
        # comments is the name of the foreign key in Comment model
        return self.comments.filter(approved_comment=True)

    # This will be called after creating an insante of a port.
    # Tells Django where to go. Has to be called get_absolute_url
    def get_absolute_url(self):
        # TO DO: implement a post_detail URL
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment (models.Model):
    # each comment will align with a post
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
