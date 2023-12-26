from django.db import models

# Create your models here.

class UserModel(models.Model):
    uid = models.AutoField(primary_key=True, db_column='uid')
    firstname = models.CharField(max_length=25, db_column='firstname', null=False)
    lastname = models.CharField(max_length=25, db_column='lastname', null=False)
    username = models.CharField(max_length=25, db_column='username', null=False)
    password = models.CharField(max_length=25, db_column='password', null=True)
    address = models.CharField(max_length=100, db_column='address', null=True)
    dob = models.IntegerField(db_column='dob', null=True)
    active = models.BooleanField(db_column='active', default=True, null=True)

    def __str__(self):
        return self.uuid

    class Meta:
        managed = True
        db_table = 'user'
