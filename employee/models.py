from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User, Group


state_choices = (
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('The Government of NCT of Delhi', 'The Government of NCT of Delhi'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal')
)

gender_choices = (('Male','Male'), ('Female', 'Female'), ('DNS', 'Do not want to specify'))
 
leave_choices = (('Sick', 'Sick'), ('Casual', 'Casual'), ('Closed', 'Closed'))

# group_choices = (('Kitchen', 'Kitchen'), ('Floor', 'Floor'), ('Admin', 'Admin'))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    profile_pic = models.ImageField(default='profile.png', null=True, blank=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    city = models.CharField(default='Bengaluru', max_length=30)
    state = models.CharField(choices=state_choices, default='Karnataka', max_length=50)
    gender = models.CharField(choices=gender_choices, max_length=50, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)


    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    
    
    def __str__(self):
        return f"{self.user.username}"
    


class EmployeeLeave(models.Model):
    employee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    leave_type = models.CharField(max_length=10, blank=True, null=True, choices=leave_choices)
    leave_details = models.TextField(max_length=100, blank=True, null=True)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.leave_type} Leave"
    
    def date_difference(self):
        return self.leave_end_date - self.leave_start_date
    
    class Meta:
        ordering = ('leave_start_date',)