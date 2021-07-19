"""Model tells Django how to work with the data that will be stored in the app.

Code-wise, a model is just a class; it has attributes and methods.

To record what we've been learning about each topic we need to define a model
for the kinds of entries users can make in their leaning logs. Each entry needs
to be associated with a particular topic. This relationship is called a many-
to-one relationship, meaning many entries can be associated with one topic.
"""


from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    # Foreign key is ref to another record in the database.
    # on_delete=models.CASCADE tells Django that when a topic is deleted, all
    # of the entries associated with that topic should be deleted as well.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Class holds extra info for managing a model."""

        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."
