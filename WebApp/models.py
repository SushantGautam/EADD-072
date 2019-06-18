import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.forms import CharField, IntegerField, DateTimeField

USER_ROLES = (
    ('CenterAdmin', 'CenterAdmin'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Parent', 'Parent'),
)


class StudentInfo(AbstractUser):
    Member_ID = CharField(max_length=250, blank=True, null=True)
    Member_Password = CharField(max_length=250, blank=True, null=True)
    Member_Type = IntegerField(blank=True, null=True)
    Member_Name = CharField(max_length=500, blank=True, null=True)
    Member_Permanent_Address = CharField(max_length=500, blank=True, null=True)
    Member_Temporary_Address = CharField(max_length=500, blank=True, null=True)
    Member_BirthDate = CharField(max_length=50, blank=True, null=True)
    Member_Email = CharField(max_length=150, blank=True, null=True)
    Member_Phone = CharField(max_length=150, blank=True, null=True)
    member_Avatar = CharField(max_length=50, blank=True, null=True)
    member_Gender = IntegerField(blank=True, null=True)
    Use_Flag = CharField(max_length=1, blank=True, null=True)
    Register_DateTime = DateTimeField(default=datetime.now(), blank=True)
    Register_Agent = CharField(max_length=200, blank=True, null=True)
    Member_Memo = CharField(max_length=500, blank=True, null=True)

    # role = models.ManyToManyField(Role)

    role = models.CharField(max_length=30, choices=USER_ROLES, default="Student")



