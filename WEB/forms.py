import os
# from importlib._common import _

from dal import autocomplete
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm, Form, CharField, ChoiceField

from .models import *

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)


# class UploadForm(forms.Form):
#
#     def validate_file_extension(value):
#         from django.core.exceptions import ValidationError
#
#         ext = os.path.splitext(value.name)[1]
#         valid_extensions = ['.csv']
#         if not ext.lower() in valid_extensions:
#             raise ValidationError(u'Invalid file extension ')
#
#     excel_file = forms.FileField(label='Excel File (.csv)', required=False, validators=[validate_file_extension])


# class EntryForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ('admission', 'first_name', 'middle_name', 'last_name', 'sex', 'entry_rank')
#

# class SchoolForm(ModelForm):
#     class Meta:
#         model = School
#         fields = ('name', 'district')
#         widgets = {
#             'district': autocomplete.ModelSelect2(url='WEB:district_autocomplete')
#         }


# class WorkLoadForm(ModelForm):
#     class Meta:
#         model = WorkLoad
#         fields = ('staff', 'subject', 'rank')


class DateInput(forms.DateInput):
    input_type = 'date'


# class RegistrationForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ('dob', 'parent_phone','residency')
#         widgets = {
#             'dob': DateInput(),
#         }


# class CoordinatorForm(ModelForm):
#     class Meta:
#         model = Coordinator
#         fields = ('staff', 'rank')


# class AcademicEventForm(ModelForm):
#     class Meta:
#         model = AcademicEvent
#         fields = ('year', 'event', 'rank', 'deadline')
#         widgets = {
#             'deadline': DateInput(),
#
#         }


# class CombinationSubjectForm(ModelForm):
#     class Meta:
#         model = CombinationSubject
#         fields = ('combination', 'subject')

class DateInput(forms.DateInput):
    input_type = 'date'


def news_image_validation(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'allowed file format is .png and .jpg')


class NewsForm(ModelForm):
    place = forms.CharField(help_text="Enter the place where the news was taken")
    image = forms.FileField(label="Image Content", required=True, validators=[news_image_validation],
                            help_text="upload an image")

    class Meta:
        model = Content
        fields = ('title', 'place', 'image', 'body')

    import os

    # def clean_coupling_file(self):
    #     image = self.cleaned_data['image']
    #     extension = os.path.splitext(image.name)[1]  # [0] returns path+filename
    #     VALID_EXTENSION = ['.png','.jpg']
    #
    #     if extension != VALID_EXTENSION:
    #         self.add_error(
    #             'image',
    #             _('Only files with ".png or jpg" extension are supported, '
    #               'received: "%s" file.' % extension)
    #         )
    #     return image


class FilterForm(Form):
    FILTER_CHOICES = (
        ('all', 'All'),
        ('people', 'People'),
        ('certification', 'Certification'),
        ('skillset', 'Skillset'),
    )
    search = forms.CharField(required=False)
    filter_field = forms.ChoiceField(choices=FILTER_CHOICES)


class EventForm(ModelForm):
    place = forms.CharField(help_text="Enter the place where the news was taken")
    image = forms.FileField(label=" Event Image", required=True, validators=[news_image_validation],
                            help_text="upload an image")

    class Meta:
        model = Content
        fields = ('title', 'place', 'image', 'date', 'body')
        widgets = {
            'date': DateInput(),
        }


def pdf_validation(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'allowed file format is .pdf')


class DownloadForm(ModelForm):
    image = forms.FileField(label=" Document", required=True, validators=[pdf_validation],
                            help_text="upload the document")

    class Meta:
        model = Content
        fields = ('title', 'image',)


class ReportForm(ModelForm):
    image = forms.FileField(label=" Report", required=True, validators=[pdf_validation],
                            help_text="upload a report ")

    class Meta:
        model = Content
        fields = ('title', 'image',)


class NewsLetterForm(ModelForm):
    image = forms.FileField(label=" News Letter", required=True, validators=[pdf_validation],
                            help_text="upload a news Letter ")

    class Meta:
        model = Content
        fields = ('title', 'image',)


class ProgrammeForm(ModelForm):
    class Meta:
        model = Programme
        fields = ('name', 'category', 'fee', 'duration', 'description',)
