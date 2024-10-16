from django.db import models

# Create your models here.

class Administration(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    

class NewsModel(models.Model):
    news_heading = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='images/')
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField() 
    date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.news_heading
    
      
class BlogModel(models.Model):
    main_heading = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='images/')
    date = models.DateField(null=True, blank=True)
    blog_description = models.TextField()
   
    def __str__(self):
        return self.blog_description
    
class MassesModel(models.Model):
    Mass_Name = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    place = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
   
   
    def __str__(self):
        return self.description
    
class GalleryModel(models.Model):
    gallery_name = models.CharField(max_length=100)
    gallery_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.gallery_name
    
class EventModel(models.Model):
    heading = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='images/')
    venue = models.CharField(max_length=200)
    description = models.TextField() 
    date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.heading
    
class EnquiryModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10,null=True,blank=True)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class AboutModel(models.Model):
    About_video = models.URLField(max_length=200, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.About_video