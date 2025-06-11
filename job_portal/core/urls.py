from django.urls import path
from . import views

urlpatterns = [

    path('',views.LandingView.as_view(),name='landing_page'),
    path('contact/',views.ContactView.as_view(),name='contact_page'),
    path('about/',views.AboutView.as_view(),name='about_page'),
    path('user_selection/',views.UserSelectionView.as_view(),name='user_selection_page'),

]