from django.db import models

class ChildManager(models.Manager):
    def get_queryset(self):
        return super(ChildManager,self).get_queryset().filter(id_usuario=2)