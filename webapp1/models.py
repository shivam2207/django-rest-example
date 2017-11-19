from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class employees(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    emp_id = models.IntegerField()
    salary = models.IntegerField()
    phone_no = models.CharField(validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10 and do not use country code', code='nomatch')],max_length=10)

    def __str__(self):
        # return '{}{}'.format(self.first_name, self.last_name)
        return (self.first_name)
