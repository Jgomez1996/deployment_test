from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['show_title']) < 2:
            errors["show_title"] = "Show title should be at least 2 characters!"
        if len(postData['show_network']) < 3:
            errors["show_network"] = "Network should be at least 3 characters"
        if len(postData['show_description']) < 10:
            errors["show_description"] = "description should be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=30)
    release_date = models.CharField(max_length=10, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

