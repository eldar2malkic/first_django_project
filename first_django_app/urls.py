from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.root_method),
    path('some_route', views.success),
    path('<str:name>', views.hello_name),
    # path('another_route', views.another_method),
    # path('redirected_route', views.redirected_method)
]
