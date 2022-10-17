from email.policy import default
from django.db import models
from credentials.models import *
from student.models import *


class Course(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, default="")
    admin = models.OneToOneField("credentials.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.last_name + " " + self.admin.first_name


class LeaveReportStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=False, default="")
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeedbackStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=False, default="")
    feedback = models.TextField()
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NotificationStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=False, default="")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Attendance(models.Model):
    session = models.ForeignKey("credentials.Session", on_delete=models.CASCADE, null=False, default="")
    subject = models.ForeignKey("student.Subject", on_delete=models.CASCADE, null=False, default="")
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AttendanceReport(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE, null=False, default="")
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, null=False, default="")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


