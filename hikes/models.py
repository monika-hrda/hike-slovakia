from django.db import models


class Hike(models.Model):
    EASY = 0
    MODERATE = 1
    DIFFICULT = 2
    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MODERATE, 'Moderate'),
        (DIFFICULT, 'Difficult'),
    ]
    difficulty = models.IntegerField(
        choices=DIFFICULTY_CHOICES,
        default=EASY,
    )
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='hikes', null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class ScheduledHike(models.Model):
    hike = models.ForeignKey('Hike', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'Hike {self.hike} is scheduled for {self.date}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['hike', 'date'],
                name='unique_hike'),
        ]
