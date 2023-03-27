from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Index.as_view(),name="index"),
    
    path('post/<int:pk>/',views.PostView.as_view(),name="postUrl"),
    path('postadd/',views.postadd,name="postadd"),
    path('comment/add/<int:id>/',views.commentadd,name="commentadd"),
    path('comment/parent/add/<int:id>/',views.parent_comment,name="parent_comment"),
    path('logout/',views.logoutview,name="logout_page"),
    path('about/',views.about,name="about")
    
]