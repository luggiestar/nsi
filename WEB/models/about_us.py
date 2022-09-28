from django.db import models
from ckeditor.fields import RichTextField

CATEGORY = (
    ('history','Our history'),
    ('function','Our Function'),
    ('mission','Mission, Vision & Core Values'),
)


class AboutUs(models.Model):
    category = models.CharField(choices=CATEGORY, max_length=40, null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "about"
        verbose_name_plural = "about"

    def __str__(self):
        return self.category