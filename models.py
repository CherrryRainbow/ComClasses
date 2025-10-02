from django.db import models
from datetime import datetime
import uuid

class Student(models.Model):
    id = models.CharField(name="id",max_length=10)
    pname = models.CharField(name="pname",max_length=3)
    fname = models.CharField(name="fname",max_length=20)
    lname = models.CharField(name="lname",max_length=25)
    section = models.IntegerField(name="section",default=1)

    def __str__(self):
        return f"""
        id="{self.id}",
        pname="{self.pname}",
        fname="{self.fname}",
        lname="{self.lname}",
        section={self.section}
        """

class Subject(models.Model):
    id = models.CharField(name="id",max_length=15)
    name = models.CharField(name="name",max_length=128)
    year = models.IntegerField(name="year",max_length=4,default=datetime.now().year)
    term = models.PositiveIntegerField(name="term")
    teacher1 = models.CharField(name="teacher1",max_length=64)
    teacher2 = models.CharField(name="teacher2",max_length=64,null=True)
    std_count = models.IntegerField(name="std_count")

    def __str__(self):
        return f"""
        id="{self.id}",
        name="{self.name}",
        year={self.year},
        term={self.term},
        teacher1="{self.teacher1}",
        teacher2="{self.teacher2}",
        std_count="{self.std_count}"
        """

class Work(models.Model):
    id = models.UUIDField(default=f"{uuid.uuid1()}",primary_key=True)
    topic = models.CharField(name="topic",max_length=25)
    assign_datetime = models.DateTimeField(name="assign_datetime")
    due_to_datetime = models.DateTimeField(name="due_to_datetime")
    description = models.TextField(name="description")
    full_points = models.FloatField(name="full_points")
    file_encode = models.BinaryField(name="file_encode",blank=True)

    def __str__(self):
        return f"""
        id="{self.id}",
        topic="{self.topic}",
        assign_datetime="{self.assign_datetime}",
        due_to_datetime="{self.due_to_datetime}",
        full_points={self.full_points}
        """

class SubmitWorks(models.Model):
    id = models.UUIDField(name="id",default=f"{uuid.uuid1()}")
    student = models.ForeignKey(Student,name="student",on_delete=models.CASCADE)
    work = models.ForeignKey(Work,name="work",on_delete=models.CASCADE)
    submit_datetime = models.DateTimeField(name="submit_datetime")
    recv_points = models.FloatField(name="recv_points")
    description = models.TextField(name="description")
    file_encode = models.BinaryField(name="file_encode",blank=True)

    def __str__(self):
        return f"""
        id={self.id},
        student="{self.student.id}",
        work={self.work.topic},
        submit_datetime="{self.submit_datetime}",
        recv_points={self.recv_points},
        description={self.description},
        """