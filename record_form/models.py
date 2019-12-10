from django.utils.crypto import get_random_string
from django.utils import timezone
from django.db import models, IntegrityError
from django.urls import reverse
from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm

# phone validator using regular expressions for numbers
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the form '+233206754455'")

SEX = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

Nature_Of_Disability = (
    ('Blindness', 'Blindness'),
    ('Low Vision', 'Low Vision'),
    ('Leprosoy Cured persons', 'Leprosoy Cured persons'),
    ('Locomotor Disability', 'Locomotor Disability'),
    ('Dwarfism', 'Dwarfism'),
    ('Intellectual Disability', 'Intellectual Disability'),
    ('Mental Illness', 'Mental Illness'),
    ('Cerebral Palsy', 'Cerebral Palsy'),
    ('Specific Learning Disabilities', 'Specific Learning Disabilities'),
    ('Speech and Language disability', 'Speech and Language disability'),
    ('Hearing Impairment', 'Hearing Impairment'),
    ('Muscular Dystrophy', 'Muscular Dystrophy'),
    ('Acid Attack Victim', 'Acid Attack Victim'),
    ('Parkinson’s disease', 'Parkinson’s disease'),
    ('Multiple Sclerosis', 'Multiple Sclerosis'),
    ('Thalassemia', 'Thalassemia'),
    ('Hemophilia', 'Hemophilia'),
    ('Sickle Cell disease', 'Sickle Cell disease'),
    ('Autism Spectrum Disorder', 'Autism Spectrum Disorder'),
    ('Chronic Neurological conditions', 'Chronic Neurological conditions'),
    ('Multiple Disabilities including Deaf Blindness',
     'Multiple Disabilities including Deaf Blindness')
)

ZONAL_COUNCIL = (
    ('Gbentaana', 'Gbentaana'),
    ('Koose', 'Koose'),
    ('Nii Ashaley', 'Nii Ashaley'),
)

ID_TYPE = (
    ('Voters Id', 'Voters Id'),
    ('Birth Certificate', 'Birth Certificate'),
    ('National Health Insurance', 'National Health Insurance'),
)


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=140)
    zonal_council = models.CharField(max_length=255, choices=ZONAL_COUNCIL)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"


class PersonInfo(models.Model):
    # p_code = models.UUIDField(
    #     max_length=8, help_text='Auto generated code for person', auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(
        max_length=100, help_text='Provide full and other names here')
    date_of_birth = models.DateField(
        auto_now=False, help_text='Please select date of birth of person')
    today_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=6, choices=SEX)
    id_type = models.CharField(
        max_length=26, choices=ID_TYPE, help_text='National Identification Type')
    id_number = models.CharField(
        max_length=20, help_text='Enter ID Type number here')
    mobile_number = models.CharField(validators=[phone_regex], max_length=17)
    disability_type = models.CharField(
        max_length=255, choices=Nature_Of_Disability, help_text='Select Nature of disability')
    community_name = models.CharField(
        max_length=50, help_text='Area where he/she lives')
    street_name = models.CharField(
        max_length=50, help_text='Name of the particular street of residence')
    land_mark = models.CharField(
        max_length=100, help_text='Could be a popular building, or anything that makes identifying the place easy')
    house_number = models.CharField(
        max_length=100, help_text='House number / GPS Code', blank=False)
    caregiver_name = models.CharField(
        max_length=100, help_text='Provide full name of care giver')
    caregiver_number = models.CharField(
        validators=[phone_regex], max_length=17)
    passport_pic = models.ImageField(
        upload_to='passport/%y%m%d/', blank=False, null=False)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Informations"

    def __str__(self):
        return self.full_name

    # def save(self, *args, **kwargs):
    #     if (self.id is None) or (len(self.id) == 0):
    #         self.id = self.creator
    #     super(PersonInfo, self).save(self, *args, **kwargs)

    # def generate_id(self):
    #     return '_' + get_random_string(length=8,
    #                                    allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    def get_absolute_url(self):
        return reverse('record_form:create_person')