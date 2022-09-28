from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# from .views import DistrictAutocomplete
from .views import *

app_name = 'WEB'

urlpatterns = [
    # path('', views.home, name="home"),
    path('', home, name="index"),
    path('about-us/', about_us, name="about_us"),
    path('Institute-Administration/', administration, name="administration"),
    path('Programme-view/<str:id>', view_programme, name="view_programme"),
    path('All-Programmes/', all_programme, name="all_programme"),
    path('login', views.user_login, name="login"),

    # CONTENT VIEWS
    path('news-list', NewsList.as_view(), name="news_list"),
    path('report-list', ReportsList.as_view(), name="report_list"),
    path('news-letter-list', NewsLettersList.as_view(), name="news_letter_list"),
    path('downloads-list', DownloadsList.as_view(), name="downloads_list"),
    path('event-list', EventList.as_view(), name="event_list"),
    path('programme-list', ProgrammeList.as_view(), name="programme_list"),

    # FORM VIEWS
    path('delete-content/<content>', views.delete_content, name="delete_content"),
    path('delete-programme/<programme>', views.delete_programme, name="delete_programme"),
    path('add-news/', views.news_form, name="add_news"),
    path('add-news-Letter/', views.news_letter_form, name="news_letter_form"),
    path('add-event/', views.event_form, name="add_event"),
    path('add-report/', views.report_form, name="report_form"),
    path('add-programme/', views.programme_form, name="programme_form"),
    path('upload-document/', views.upload_document_form, name="upload_document_form"),

    # FORM UPDATES  VIEWS
    path('update-news/<object_pk>', views.update_news, name="update_news"),
    path('update-event/<object_pk>', views.update_event, name="update_event"),
    path('update-downloads/<object_pk>', views.update_downloads, name="update_downloads"),
    path('update-news-letter/<object_pk>', views.update_news_letter, name="update_news_letter"),
    path('update-report/<object_pk>', views.update_report, name="update_report"),
    path('update-programme/<object_pk>', views.update_programme, name="update_programme"),


    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # autocomplete views
    # path('district-auto-complete/', DistrictAutocomplete.as_view(), name='district_autocomplete'),
    path('password_reset/', auth_views.PasswordResetView.
         as_view(template_name='password/password_reset.html'), name='password_reset'),

]

'''
    Password view For reseting password
------------------------------------------
1 - PasswordResetView submit email from user
2 - PasswordResetDoneView email sent successfull
3 - link to password Rest form in email
4 - Password successfully changed
'''
