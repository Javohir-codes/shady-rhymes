from django.db import models
from django.utils.text import slugify
from .models import User, CreateProfile

class Furniture(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        SOLD = "sold", "Sold"


    image = models.ImageField(upload_to="nft_images/")
    price = models.DecimalField(max_digits=10, decimal_places=5)
    status = models.CharField(choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:100] or "nft"
            candidate_slug = base
            i = 1
            while Furniture.objects.filter(slug=candidate_slug).exists():
                candidate_slug = f"{base}-{i}"
                i += 1
            self.slug = candidate_slug
        super().save(*args, **kwargs)

    def __str__(self): return self.title


class Ownership(models.Model):
    Furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE, related_name="ownerships")
    owner = models.ForeignKey(CreateProfile, on_delete=models.CASCADE, related_name="owned_nfts")
    acquired_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.display_name} owns {self.nft.title}"