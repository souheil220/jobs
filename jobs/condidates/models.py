from django.db import models

GENDER_MALE = "male"
GENDER_FEMALE = "female"
GENDER_CHOICES = (
    (GENDER_MALE,'Male'),
    (GENDER_FEMALE,'Female'),
)

STATUS_PENDING = 'pending'
STATUS_ACCEPTED = 'accepted'
STATUS_REJECTED = 'rejected'

STATUS_CHOICES = (
    (STATUS_PENDING,'Pending'),
    (STATUS_ACCEPTED,'Accepted'),
    (STATUS_REJECTED,'Rejected'),
)


class Condidate(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default=GENDER_MALE)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    expected_salary = models.IntegerField()
    will_relocate = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.name,self.mobile)

class CondidateJobMapping(models.Model):
    condidate = models.ForeignKey(Condidate,on_delete=models.CASCADE)
    jobs = models.ForeignKey('new_jobs.NewJob',on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default = STATUS_PENDING )
    feedback = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{}-{}".format(self.condidate.name,self.jobs.position_name)