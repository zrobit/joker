from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, max_length=32, db_index=True)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, max_length=32, db_index=True)
    date = models.DateField(auto_now_add=True)
    status_choices = (
        ('featured', 'Featured'),
        ('published', 'Published'),
        ('deleted', 'Deleted'),
    )
    status = models.CharField(
        max_length=16, choices=status_choices, default='published')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


# class Set(models.Model):
#     title = models.CharField(max_length=128, blank=True, null=True)
#     slug = models.SlugField(unique=True, max_length=128, db_index=True)
#     date = models.DateField(blank=True, null=True)
#     description = models.TextField(max_length=512, blank=True, null=True)
#     is_simple = models.BooleanField(default=False)

#     STATUS_CHOICES = (
#         ('featured', 'Featured'),
#         ('published', 'Published'),
#         ('deleted', 'Deleted'),
#         ('pending', 'Pending'),
#         ('flagged', 'Flagged'),
#     )

#     status = models.CharField(
#         max_length=16, choices=STATUS_CHOICES, blank=True, null=True)
#     category = models.ForeignKey(Category, blank=True, null=True)
#     tags = models.ManyToManyField(Tag, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.title)
#         super(Set, self).save(*args, **kwargs)

#     def __unicode__(self):
#         return 'id: %d | hash: %s' % (self.id, self.hash)


# class Site(models.Model):
#     name = models.CharField(max_length=128, blank=True, null=True)
#     domain =  models.URLField(blank=True, null=True)


class Joke (models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    slug = models.SlugField(max_length=80, db_index=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=512, blank=True, null=True)

    STATUS_CHOICES = (
        ('featured', 'Featured'),
        ('published', 'Published'),
        ('deleted', 'Deleted'),
        ('pending', 'Pending'),
        ('flagged', 'Flagged'),
    )

    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, blank=True, null=True)

    views = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'id: %d | hash: %s' % (self.id, self.hash)
