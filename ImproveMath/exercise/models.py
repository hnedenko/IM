from django.db import models


class Exercise(models.Model):
    chapter = models.ForeignKey('Chapter', on_delete=models.PROTECT, null=False)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.PROTECT, null=False)
    time_create = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='exercise/res')

    def __str__(self):
        return str(self.chapter) + ' - ' + str(self.difficulty)


class Chapter(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return str(self.name)


class Difficulty(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return str(self.name)
