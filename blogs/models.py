from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe
from markdown import markdown


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    # babyl_slug = models.CharField(unique=True)
    description = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    slug = models.SlugField(
        default='',
        editable=False,
        max_length=50
    )

    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('article-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)



    #Later add options for making password protecting, collecting emails, indexing on search engines

class Post(models.Model):
    blog = models.ForeignKey(Blog,  null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    #post_slug = models.CharField(max_length=50, unique=True)
    body = models.TextField() #max_length=50000 perhaps?
    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(
        default='',
        editable=False,
        max_length=50
    )

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_post_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))

    def __str__(self):
        return self.title
    #Later add options for editing posts
    #updated_at = models.DateTimeField(null=True)
    #prior_posts


#Delete this
# class Topic(models.Model):
#     subject = models.CharField(max_length=255)
#     last_updated = models.DateTimeField(auto_now_add=True)
#     board = models.ForeignKey(Board, related_name='topics')
#     starter = models.ForeignKey(User, related_name='topics')