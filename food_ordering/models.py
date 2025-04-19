from django.db import models
from django.contrib.auth.models import User

# Tuple defining the available meal types in the system
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
)
# Tuple defining the availability status of menu items
STATUS = (
    (0, "Unavailable"),
    (1, "Available"),
)


class Item(models.Model):
    """
    Model representing a food item on the menu.

    Each item has details like name, description, price, and availability status.
    Items are categorized by meal type and associated with an author (staff member).
    """

    meal = models.CharField(
        max_length=80, unique=True
    )  # Name of the food item, must be unique
    description = models.TextField()  # Detailed description of the food item
    price = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Price with 2 decimal places
    meal_type = models.CharField(choices=MEAL_TYPE)  # Category of the meal
    author = models.ForeignKey(
        User, on_delete=models.PROTECT
    )  # Staff member who added this item
    status = models.IntegerField(
        choices=STATUS, default=0
    )  # Availability status, default is Unavailable
    date_created = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when item was created
    date_updated = models.DateTimeField(
        auto_now=True
    )  # Timestamp when item was last updated

    def __str__(self):
        """Return the meal name as the string representation of this item."""
        return self.meal
