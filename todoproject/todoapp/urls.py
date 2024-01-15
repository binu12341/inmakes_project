from django.urls import path
from todoapp import views

urlpatterns=[
    path('',views.taskadd,name='taskadd'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classbasedviewhome/',views.TaskListView.as_view(),name='classbasedviewhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]