from django.db import models

from apps.authentication.models import User
from apps.common.models import BaseModel


class Profile(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    summary = models.TextField(
        default="",
        blank=True,
    )
    company = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    email = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    linkedin = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    github = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    website = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    skills = models.JSONField(
        default=list,
        blank=True,
    )
    languages = models.JSONField(
        default=list,
        blank=True,
    )
    hobbies = models.JSONField(
        default=list,
        blank=True,
    )
    interests = models.JSONField(
        default=list,
        blank=True,
    )


class Experience(BaseModel):
    class Category(models.TextChoices):
        EDUCATION = "EDU", "Education"
        CARRIER = "CAR", "Carrier"
        PROJECT = "PRJ", "Project"

    class Type(models.TextChoices):
        FULL_TIME = "FLT", "Full-time"
        PART_TIME = "PRT", "Part-time"
        SELF_EMPLOYED = "SLE", "Self-employed"
        VOLUNTEER = "VOL", "Volunteer"

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=128,
    )
    role = models.CharField(
        max_length=128,
    )
    location = models.CharField(
        max_length=128,
    )
    type = models.CharField(
        choices=Type.choices,
        max_length=3,
        null=True,
        blank=True,
    )
    category = models.CharField(
        choices=Category.choices,
        max_length=3,
        null=True,
        blank=True,
    )
    url = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    starting = models.DateField(
        null=True,
        blank=True,
    )
    ending = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField()


class Tailor(BaseModel):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=128,
    )
    description = models.TextField()
    additional = models.TextField(default="")


class CurriculumVitae(BaseModel):

    tailor = models.ForeignKey(
        Tailor,
        on_delete=models.CASCADE,
    )
    uri = models.CharField(
        max_length=128,
    )
    fit = models.IntegerField(
        help_text="an integer value between 0 and 5",
    )
    comment = models.TextField(
        help_text="AI's comment about the CV and position match",
    )
    content = models.TextField(
        help_text="latex text for CV to be rendered",
    )
    meta = models.JSONField(
        help_text="meta information including prompt and model versions",
    )
