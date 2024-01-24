from . import views
from django.urls import path


urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.list_post, name = "list_post"),
    path("<int:post_id>", views.post_detail, name = "post_detail"),
]
