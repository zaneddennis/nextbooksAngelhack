from django.db import models
from django.urls import reverse

# Create your models here.


class Resource(models.Model):
    LEVEL_CHOICES = (
        ("MS", "Middle School"),
        ("HSL", "High School-Lower"),
        ("HSU", "High School-Upper"),
        ("C1000", "College-1000"),
        ("C2000", "College-2000"),
        ("C3000", "College-3000"),
        ("C4000", "College-4000"),
        ("C5000", "College-5000"),
        ("C6000", "College-6000+"),
    )

    SUBJECT_CHOICES = (
        ("BIO", "Biology"),
        ("CHE", "Chemistry"),
        ("PHY", "Physics"),
        ("CSI", "Computer Science"),
        ("HIS", "History"),
    )

    resourceTitle = models.CharField(max_length=100, verbose_name="Title")
    score = models.IntegerField(default=0)

    levelTag = models.CharField(max_length=5, choices=LEVEL_CHOICES, blank=True, default="", verbose_name="Level")
    subjectTag = models.CharField(max_length=3, choices=SUBJECT_CHOICES, blank=True, default="", verbose_name="Subject")
    courseTag = models.CharField(max_length=30, blank=True, default="", verbose_name="Course Name")
    courseNumberTag = models.IntegerField(null=True, blank=True, verbose_name="Course Number")
    institutionTag = models.CharField(max_length=50, blank=False)

    content = models.TextField(blank=True)

    def __str__(self):
        return self.resourceTitle

    def get_absolute_url(self):
        return reverse("resource-detail", args=[str(self.id)])

    class Meta:
        ordering = ["-score"]
