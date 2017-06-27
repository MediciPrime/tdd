from django.db import models

# TODO: Support more than one list!
class Item(models.Model):
    text = models.TextField(default='ignore')
