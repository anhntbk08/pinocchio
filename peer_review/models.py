from django.db import models
from django.core.management import call_command

class QuestionType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Question(models.Model):
    questionText = models.CharField(max_length=300)
    pubDate = models.DateTimeField('date published')
    questionType = models.ForeignKey(QuestionType)
    questionGrouping = models.IntegerField()
    def __str__(self):
        return self.questionText
    def was_published_recently(self):
        return self.pubDate >= timezone.now() - datetime.timedelta(days=1)
    def makeDump(self):
        output = open("dump",'w') # Point stdout at a file for dumping data to.
        call_command('dumpdata','Question',format='json',indent=4,stdout=output)
        output.close()

class Header(models.Model):
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    header = models.ForeignKey(Header)
    num = models.IntegerField(default=0)
    def __str__(self):
        return self.header.text
    # num = models.IntegerField(default=0)
    # choiceText = models.CharField(max_length=200)

class Student(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=2)

class StudentDetail(models.Model):
    student = models.ForeignKey(Student)
    title = models.CharField(max_length=4)
    initials = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    cell = models.CharField(max_length=15)
    email = models.CharField(max_length=60)

class Questionnaire(models.Model):
    intro = models.CharField(max_length=50)

class RoundDetail(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    startingDate = models.DateTimeField('starting date')
    endingDate = models.DateTimeField('ending date')
    description = models.CharField(max_length=200)

class TeamDetail(models.Model):
    studentDetail = models.ForeignKey(StudentDetail)
    roundDetail = models.ForeignKey(RoundDetail)
    teamNumber = models.IntegerField(default=0)
    status = models.CharField(max_length=20)