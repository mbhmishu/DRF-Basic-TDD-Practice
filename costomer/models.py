from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# Create your models here.

class PublisherManager(models.Manager):
    def get_queryset(self):
        return super(PublisherManager,self).get_queryset().filter(status='published')
    

GENDER_CHOICES=(
    ('Maile','Maile'),
    ('Femaile','Femaile'),
    ('Other','Other')

)
STATUS_CHOICES=(
    ('draft','draft'),
    ('published','published')
    
)
class Customer(models.Model):
    title = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.PROTECT,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES)


    objects = models.Manager()
    published=PublisherManager()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

