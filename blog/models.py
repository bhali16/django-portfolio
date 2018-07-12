from django.db import models

# Create A Blog models
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#Function to show tile of blogpost in list on admin panel
    def __str__(self):
        return self.title
#Function to show Summary of Blogpost
    def summary(self):
        return self.body[:150]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
        #strftime.org for more date time formats.













#create migrations , migrate , add to admin
