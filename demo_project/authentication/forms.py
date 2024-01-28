from django import forms 
from .models import Member
class MemberForm(forms.ModelForm):

    class Meta:
        model=Member
        fields=['fname','lname','email','p1','p2']