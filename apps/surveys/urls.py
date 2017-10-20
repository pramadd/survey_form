from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$',views.index),
    url(r'^process$', views.process),     # This line has changed!
    url(r'^result$',views.result),
    url(r'^refresh$', views.refresh)
]    