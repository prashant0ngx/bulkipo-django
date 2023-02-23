from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.index,name='index'),

    path('dmatsaccount/',views.dmatsaccount,name='dmatsaccount'),
    path('applyipo/',views.applyipo,name='applyipo'),
    path('applyshareid/',views.applyshareid,name='applyshareid'),
    path('about/',views.about,name='about'),
    path('dmatslist/<int:pk>/delete/',views.dmatsdelete, name='dmatsdelete'),
    path('dmatslist/deleteall/',views.dmatsdeleteall, name='dmatsdeleteall'), 
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
