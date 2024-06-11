from django.db import models


class Title(models.Model):
    title = models.TextField(verbose_name="Title", null=True, blank=True)

    def __str__(self):
        return self.title


class Station(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    titles = models.ManyToManyField(Title, verbose_name="Titles", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_titles(self):
        titles = [tt.title for tt in self.titles.all()]
        return titles

