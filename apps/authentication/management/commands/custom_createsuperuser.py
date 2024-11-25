import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create SuperUser (admin)"

    def handle(self, *args, **options):
        User = get_user_model()

        superuser_username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        superuser_email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        superuser_password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        if superuser_username and superuser_password:
            superuser, _ = User.objects.get_or_create(
                username=superuser_username,
                email=superuser_email,
            )
            superuser.is_staff = True
            superuser.is_superuser = True
            superuser.is_active = True
            superuser.set_password(superuser_password)
            superuser.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"SuperUser for {superuser_username} is created successfully"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("ENV Variables are not set to create SuperUser")
            )
