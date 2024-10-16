from .import views
from django.urls import path
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('',views.index,name='index'),
    path('user_login/', views.user_login, name="user_login"),

   
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),

    path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),
    # path('ckeditor/upload/', views.ckeditor_views.upload, name='ckeditor_upload'),
    # path('ckeditor/browse/', views.ckeditor_views.browse, name='ckeditor_browse'),
    path('ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.browse, name='ckeditor_browse'),

    
    
    path('add_administaration',views.add_administaration, name='add_administaration'),
    path('view_administration', views.view_administration, name='view_administration'),
    path('update_administration/<int:pk>/', views.update_administration, name='update_administration'),
    path('delete_administration/<int:pk>/', views.delete_administration, name='delete_administration'),
    
    path('admin_add_gallery',views.admin_add_gallery,name='admin_add_gallery'),
    path('admin_gallery_view',views.admin_gallery_view,name='admin_gallery_view'),
    path('admin_update_gallery/<int:id>/',views.admin_update_gallery,name='admin_update_gallery'),
    path('admin_delete_gallery/<int:id>/',views.admin_delete_gallery,name='admin_delete_gallery'),
    
    path('admin_view_comments',views.admin_view_comments,name='admin_view_comments'),
    
    path('admin_delete_comments/<int:id>',views.admin_delete_comments,name='admin_delete_comments'),
    
    path('create_news', views.create_news, name='create_news'),
    path('news_view', views.news_view, name='news_view'),
    path('update_news/<int:id>', views.update_news, name='update_news'),
    path('delete_news/<int:id>', views.delete_news, name='delete_news'),
    
    path('create_event', views.create_event, name='create_event'),
    path('view_event', views.view_event, name='view_event'),
    path('update_event/<int:id>', views.update_event, name='update_event'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event'),
    
    path('create_blog', views.create_blog, name='create_blog'),
    path('blog_view', views.blog_view, name='blog_view'),
    path('update_blog/<int:id>', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
    
    path('create_masses', views.create_masses, name='create_masses'),
    path('masses_view', views.masses_view, name='masses_view'),
    path('update_masses/<int:id>', views.update_masses, name='update_masses'),
    path('delete_masses/<int:id>', views.delete_masses, name='delete_masses'),
    
    path('add_about_video', views.add_about_video, name='add_about_video'),
    path('admin_view_video', views.admin_view_video, name='admin_view_video'),
    path('update_video_link/<int:id>/',views.update_video_link, name='update_video_link'),
    path('delete_video/<int:id>/',views.delete_video, name='delete_video'),
 
    path('about', views.about,name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact',views.contact, name='contact'),
    
    path('administration',views.administration, name='administration'),
    path('blog', views.blog, name='blog'),
    
    
    
    path('mass',views.mass, name='mass'),
    path('event',views.event, name='event'),
    
    path('wish', views.wish, name='wish'),
    
    path('news_details/<int:id>/', views.news_details, name='news_details'),
    # path('blog_details/<int:id>/', views.blog_details, name='blog_details')
    path('blog_details/<int:id>/', views.blog_details, name='blog_details')
]