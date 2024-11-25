from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

import apps.main.models as MODELS


@transaction.atomic()
@receiver(post_save, sender=MODELS.User)
def user_post_save(
    sender,
    instance: MODELS.User,
    created: bool,
    **kwargs,
):
    if created:
        _ = MODELS.Profile.objects.create(
            user=instance,
        )
        instance.save()
