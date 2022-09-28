from ckeditor.fields import RichTextField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    # username = None

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    POSITIONS = (
        ('staff', 'staff'),
        ('Accountant', 'Accountant'),
        ('student', 'student'),
        ('tutor', 'tutor'),
        ('ICT Officer', 'ICT Officer'),
        ('System Administrator', 'System Administrator'),
        ('Director', 'Director'),
        # ('Second Master', 'Second Master'),
        # ('Second Mistress', 'Second Mistress'),
    )
    #
    # NATION = (
    #     ('TANZANIA', 'TANZANIA'),
    #     ('KENYA', 'KENYA'),
    #
    # )
    phone_regex = RegexValidator(regex=r'[0][6-9][0-9]{8}', message="Phone number must be entered in the format: "
                                                                    "'0.....'. Up to 10 digits allowed.")

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100, null=True, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=False)

    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    sex = models.CharField(choices=GENDER, max_length=1, null=True, blank=True)
    title = models.CharField(choices=POSITIONS, max_length=40, null=False, default="staff")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class CollegeSettings(models.Model):
    logo = models.ImageField("College Logo", null=False, blank=False)
    Stump = models.ImageField("College Stump", null=True, blank=True)
    Signature = models.ImageField("College Signature", null=False, blank=False)


class Category(models.Model):
    LEVELS = (
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('Short Course', 'Short Course'),
    )
    name = models.CharField(choices=LEVELS, max_length=45, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "Programme Category"
        verbose_name_plural = "Programme Category"

    def __str__(self):
        return self.name


class Programme(models.Model):
    name = models.CharField("", max_length=200, null=False, blank=False, unique=True)
    description = RichTextField(null=True, blank=True)
    fee = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=False,)
    duration = models.CharField(max_length=45, null=True, blank=False)
    class Meta:
        verbose_name = "Programme"
        verbose_name_plural = "Programme"

    def __str__(self):
        return self.name


class Type(models.Model):
    Types = (
        ('NEWS', 'NEWS'),
        ('EVENT', 'EVENT'),
        ('REPORT', 'REPORT'),
        ('NEWS LETTER', 'NEWS LETTER'),
        ('DOWNLOADS', 'DOWNLOADS'),
    )
    name = models.CharField(choices=Types, max_length=45, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "Content Type"
        verbose_name_plural = "Content Type"

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=500, unique=True, null=False)
    date = models.DateField(null=True)
    image = models.FileField("Content Image",upload_to="contents/%Y/%m/%d/", null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    uploaded_date = models.DateField(auto_now_add=True, editable=False)
    place = models.CharField(max_length=500, null=True)
    body = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Content"

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return self.title
