from django.contrib import admin
from django.urls import path,include
from home import views
from home.views import TaskDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete')
]
admin.site.site_header="TODO-LIST"
admin.site.site_title="welcome to TODO-LIST dashboard"
admin.site.index_title="welcome to my TODO-LIST"