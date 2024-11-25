from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    @property
    def full_name(self):
        return " ".join(
            [
                name
                for name in [self.first_name, self.last_name]
                if name is not None or name != ""
            ]
        )
