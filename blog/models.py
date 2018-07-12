from django.db import models

# Create A Blog models
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


#Add Blogs app to settings










#create migrations , migrate , add to admin
