from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Simple title return queue for django admin or auto template
    def __str__(self):
        return self.name
