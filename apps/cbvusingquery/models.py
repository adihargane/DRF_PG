from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    uid = models.AutoField(primary_key=True, db_column='uid')
    ucode = models.IntegerField(db_column='ucode', null=False, unique=True)
    firstname = models.CharField(max_length=25, db_column='firstname', null=False)
    lastname = models.CharField(max_length=25, db_column='lastname', null=False)
    emailid = models.CharField(max_length=30, db_column='emailid', null=True)
    mobile = models.CharField(max_length=10, db_column='mobile', null=False, unique=True)
    department = models.CharField(max_length=50, db_column='department', null=True)
    salary = models.DecimalField(db_column='salary', max_digits=10, decimal_places=2, null=True)
    active = models.BooleanField(db_column='active', default=True, null=True)

    def __str__(self):
        return self.uid

    class Meta:
        managed = True
        db_table = 'employee'


class DocumentModel(models.Model):
    uid = models.AutoField(primary_key=True, db_column='uid')
    ucode = models.IntegerField(db_column='ucode', null=False, unique=True)
    employeeucode = models.IntegerField(db_column='employeeucode', null=False)
    docname = models.CharField(max_length=20, db_column='docname', null=False)
    doctype = models.CharField(max_length=10, db_column='doctype', null=False)
    expdate = models.IntegerField(db_column='expdate', null=True)
    issuedby = models.CharField(max_length=25, db_column='issuedby', null=False)
    active = models.BooleanField(db_column='active', default=True, null=True)

    def __str__(self):
        return self.uid

    class Meta:
        managed = True
        db_table = 'document'


class EducationModel(models.Model):
    uid = models.AutoField(primary_key=True, db_column='uid')
    ucode = models.IntegerField(db_column='ucode', null=False, unique=True)
    employeeucode = models.IntegerField(db_column='employeeucode', null=False)
    institutionname = models.CharField(max_length=100, db_column='institutionname', null=False)
    degree = models.CharField(max_length=30, db_column='degree', null=False)
    fieldofstudy = models.CharField(max_length=50, db_column='fieldofstudy', null=True)
    graduationdate = models.IntegerField(db_column='graduationdate', null=True)
    active = models.BooleanField(db_column='active', default=True, null=True)

    def __str__(self):
        return self.uid

    class Meta:
        managed = True
        db_table = 'education'