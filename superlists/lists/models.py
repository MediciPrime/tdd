from django.db import models


class List(models.Model):
    pass

# TODO: Support more than one list!
class Item(models.Model):
    text = models.TextField(default='ignore')
    list = models.ForeignKey(List, default=None)
