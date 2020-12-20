from django.db import models

# Create your models here.


class Room(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    host = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.code + '@' + self.host

    class Meta:
        db_table = 'room'
