from django.db import models

# Create your models here.
# A model is the single, definitive source of truth about your data.
# It contains the essential fields and behaviors of the data you’re storing. 

# There are two steps in making migrations
# 1. docker-compose run web python manage.py makemigrations
# 2. docker-compose run web python manage.py migrate
# To Make the "main" app modifiable in the admin
# Register the models in the admin.py 


# This Tutorial, Question and Choice are like a table in the database 
# and the tutorial_title, tutorial_content,  tutorial_published, etc are like columns in the table 
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')

    def __str__(self):
        return self.tutorial_title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text