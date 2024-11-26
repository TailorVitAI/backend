# Generated by Django 5.0.1 on 2024-11-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[("EDU", "Education"), ("CAR", "Carrier"), ("PRJ", "Project")],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="hobbies",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name="profile",
            name="interests",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name="profile",
            name="languages",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name="profile",
            name="skills",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name="profile",
            name="summary",
            field=models.TextField(blank=True, default=""),
        ),
    ]