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
        return "{}".format(self.name)

    def is_engaged(self):
        jobs = CondidateJobMapping.objects.filter(condidate = self).exclude(status=STATUS_REJECTED).all()
        if len(jobs) == 0:
            return "no"
        else:
            return "yes"

class CondidateJobMapping(models.Model):
    condidate = models.ForeignKey(Condidate,on_delete=models.CASCADE)
    jobs = models.ForeignKey('new_jobs.NewJob',on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default = STATUS_PENDING )
    feedback = models.TextField(blank=True,null=True)

    def age(self):
        return self.condidate.age
    
    def position_name(self):
        return self.jobs.position_name

    def name(self):
        return self.condidate.name

    def city(self):
        return self.condidate.city

    def mobile(self):
        return self.condidate.mobile

    def gender(self):
        return self.condidate.gender
    
    def will_relocate(self):
        return self.condidate.will_relocate


    def __str__(self):
        return "{}-{}".format(self.condidate.name,self.jobs.position_name)

    class Meta:
        verbose_name_plural = "Review Condidates"