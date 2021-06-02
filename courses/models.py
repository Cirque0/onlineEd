from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Instructor(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id}: {self.firstname} {self.lastname}"

class GeneralTopic(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Course(models.Model):
    name = models.CharField(max_length=64)
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, related_name="lectures")
    generaltopic = models.ForeignKey(GeneralTopic, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"{self.id}: {self.generaltopic} - {self.name} - Instructor: {self.instructor}"

class Country(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.code}|{self.name}"

class User(AbstractUser):
    birthday = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="citizens")

class CoursesTaken(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coursestaken")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="inprogress")
    certification = models.BooleanField()

    def __str__(self):
        return f"{self.id}: Student: {self.student} Course: {self.course} Certification: {self.certification}"