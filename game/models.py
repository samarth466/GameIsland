from django.db import models
from django.db.models.signals import pre_save, pre_delete
import os
from django.conf import settings

# Create your models here.


class Game(models.Model):
    game_data_path = models.CharField(
        max_length=1000, default=None, null=True, blank=True)
    relative_path = models.BooleanField(blank=True, null=True, default=False)
    game_data_content = models.JSONField(default=dict)

    def pre_save_game_reciever(self, raw=False, using=None, update_fields=None,):
        path = None
        if self.relative_path:
            path = os.path.join(settings.BASE_DIR, self.game_data_path+'.json')
        else:
            path = self.game_data_path+'.json'
        with open(path, 'w') as file:
            file.write(self.game_data_content)
        pre_save.connect(sender=Game, instance=self,
                         using=using, update_fields=update_fields)

    def pre_delete_game_reciever(self, using=None):
        path = None
        if self.relative_path:
            path = os.path.join(settings.BASE_DIR, self.game_data_path+'.json')
        else:
            path = self.game_data_path+'.json'
        os.remove(path)
        pre_delete.connect(sender=Game, instance=self, using=using)
