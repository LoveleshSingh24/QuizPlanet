from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('leaderboard',views.leaderboard_view,name='leaderboard'),
    path('dashboard',views.dashboard_view,name='dashboard'),
    path('message/<int:id>:',views.message_view,name='message'),
    path('about',views.about_view,name='about'),
    path('blogs',views.blogs_view,name='blogs'),
    path('blogs/<str:blog_id>',views.blog_view,name='blog'),
    path('contact',views.contact_view,name='contact'),
    path('downloads',views.downloads_view,name='downloads'),
    path('termsandcondition',views.terms_and_conditions,name='termandcond'),
    path('search/users',views.search_user,name='search_users'),

]
