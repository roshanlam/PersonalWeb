from django.db import models
from django.core.validators import RegexValidator

class Platform(models.Model):
    name = models.CharField(max_length=50)
    icon = models.FileField(upload_to='icons/platforms/')
    url = models.URLField()

    def __str__(self):
        return self.name

class WorkPiece(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    platform = models.ForeignKey(Platform, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    color = models.CharField(
        max_length = 7,
        default = '#FFFFFF',
        validators = [RegexValidator(
            regex = '^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
            message = 'Color must be in hex format'
        )]
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Blog(WorkPiece):
    publish_date = models.DateField()
    class Meta:
        ordering = ('-publish_date',)