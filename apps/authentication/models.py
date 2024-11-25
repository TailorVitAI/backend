from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADM", "Admin"
        MANAGER = "MNG", "Manager"
        AGENT = "AGN", "Agent"
        CUSTOMER = "CTM", "Customer"
        PRODUCER = "PRD", "Producer"
        TRANSPORTER = "TRS", "Transporter"
        SHIPMENT_MANAGER = "SHM", "Shipment Manager"

    class Type(models.TextChoices):
        NATURAL_PERSON = "NPR", "Natural Person"
        LEGAL_PERSONALITY = "LPR", "Legal Personality"

    base_currency = models.ForeignKey(
        to="main.Currency",
        on_delete=models.PROTECT,
    )
    identification = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    trade_id = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=3,
        choices=Role.choices,
    )
    type = models.CharField(
        max_length=3,
        choices=Type.choices,
    )
    tax_invoices = models.BooleanField(
        default=True,
        help_text="should the invoices include tax?",
    )

    @property
    def full_name(self):
        return " ".join(
            [
                name
                for name in [self.first_name, self.last_name]
                if name is not None or name != ""
            ]
        )

    class Meta:
        unique_together = (("base_currency", "username"),)
