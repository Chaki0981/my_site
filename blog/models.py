from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.caption}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    slug = models.SlugField(default="", unique=True, blank=True, null=False, db_index=True)
    date = models.DateField(auto_now=True)
    # image_name = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='posts')
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="posts", null=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.author.first_name})"
