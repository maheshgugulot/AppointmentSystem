from django.db import models
class Member(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    p1=models.CharField(max_length=20)
    p2=models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.fname+''+self.lname
