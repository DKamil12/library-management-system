from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_at = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # isbn contains of 13 digits divided by 4 '-' symbols
    isbn = models.CharField(max_length=17)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images',
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.name} by {self.author}'
