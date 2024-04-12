from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):

    class Difficulty(models.TextChoices):
        EASY = 'ES', _('Easy')
        MEDIUM = 'MD', _('Medium')
        HARD = 'HD', _('Hard')
        EXTRA = 'EX', _('Extra')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    difficulty = models.CharField(max_length=2, choices=Difficulty.choices, default=Difficulty.MEDIUM, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.difficulty)
