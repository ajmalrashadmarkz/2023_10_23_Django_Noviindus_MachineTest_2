from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
# Create your models here.


class ShortTermCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1 )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/',  blank=False)
    status = models.CharField(
        max_length=10,
        choices=[('Enable', 'Enable'), ('Disable', 'Disable')],
        default='Enable'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shorttermcourse_detail",kwargs={"pk": self.pk})

    
    
