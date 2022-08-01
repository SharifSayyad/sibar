from django.db import models

class Emp(models.Model):
    name = models.CharField('emp_name', max_length=30)
    age = models.IntegerField('emp_age')
    salary = models.FloatField('emp_sal')
    #Emp(name='AAA',age=29,salary=5555)

    def __str__(self):
        return f'''
            {self.name}
        '''

class Address(models.Model):
    city = models.CharField('emp_city',max_length=30)
    state = models.CharField('emp_state',max_length=30)
    pin = models.IntegerField('emp_pincode')
    empref = models.OneToOneField('Emp',on_delete=models.CASCADE,related_name='adrref',
                                   null=True)
    def __str__(self):
        return f'''
                {self.city}
            '''

