from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

SCHOOL = ((0, "Astromancy"), (1, "Chronomancy"), (2, "Conjuration"),
          (3, "Destruction"), (4, "Divination"), (5, "Enchantment"),
          (6, "Illusion"), (7, "Necromancy"), (8, "Protection"),
          (9, "Restoration"), (10, "Transmutation"))


# Models
class Spell(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="homebrew_spell_entries")
    name = models.CharField(max_length=256)
    excerpt = models.TextField(blank=True, max_length=256)
    school = models.IntegerField(choices=SCHOOL, default=0)
    ap_cost = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)])
    mp_cost = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9)])
    range = models.CharField(max_length=256)
    duration = models.CharField(max_length=256)
    concentration = models.BooleanField()
    description = models.TextField(unique=True)
    ap_enhancements = models.TextField(blank=True)
    mp_enhancements = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.name} | written by {self.creator}"
