# Generated by Django 5.0.1 on 2024-12-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_remove_curriculumvitae_uri_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("EDU", "Education"),
                    ("CAR", "Carrier"),
                    ("PRJ", "Project"),
                    ("CON", "Contract"),
                ],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="location",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
