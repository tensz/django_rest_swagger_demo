from django.conf.urls import url
import views

urlpatterns = [
    url(r'^resource/$', views.Resource.as_view()),
]