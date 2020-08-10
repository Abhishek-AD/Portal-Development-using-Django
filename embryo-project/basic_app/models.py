from django.db import models
import datetime
# Create your models here.


class ResourcePerson(models.Model):
    DEPARTMENT_CHOICES=(
        ('BIO','Biological Sciences'),
        ('CHE','Chemical'),
        ('CHEM','Chemistry'),
        ('CE','Civil'),
        ('CS','Computer Science'),
        ('EEE','Electical and Electronics'),
        ('ECON','Economics and Finances'),
        ('HSS','Humanities and Social Sciences'),
        ('MATH','Mathematics'),
        ('ME','Mechanical'),
        ('PHA','Pharmacy'),
        ('PHY','Physics'),
        ('BITS','Other'),

    )
    resourcePerson_ID = models.AutoField(primary_key=True)
    department = models.CharField(max_length=264, choices=DEPARTMENT_CHOICES, blank=True)
    address = models.TextField( blank=True)
    email = models.EmailField(max_length=254,  blank=True)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=264)
    def __str__(self):
        return self.name


class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    date = models.DateField()
    venue = models.CharField(max_length=264)
    time = models.TimeField()
    description = models.TextField()
    topic = models.CharField(max_length=264)
    speaker = models.ManyToManyField(ResourcePerson)
    def __str__(self):
        return self.topic


class MemberInfo(models.Model):
    POSITION_CHOICES = (
        ('SC','Student Coordinator'),
        ('PRE','President'),
        ('SEC','Secretary'),
        ('SEC1','Secretary:Internal Affairs'),
        ('SEC2','Secretary:All-Year Talks'),
        ('SEC3','Secretary:Fests'),
        ('COMM','Communications Team Head'),
        ('CONTENT','Content and Online Publicity Team Head'),
        ('TECH','Tech Team Head'),
        ('EVE','Events Management Team Head'),
        ('EX','Ex-Officio')

    )
    RANK = (
        ('1','Student Coordinator'),
        ('2','President'),
        ('3','Secretary'),
        ('4','Team Head'),
        ('5','Ex-Officio')
    )
    rank = models.CharField(max_length=264,choices=RANK)
    position = models.CharField(max_length=264, choices=POSITION_CHOICES)
    name = models.CharField(max_length=264)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Expenses(models.Model):
    expenseID = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    type = models.CharField(max_length=264)
    date = models.DateField()
    expenditure = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.type
