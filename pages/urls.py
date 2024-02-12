from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # we create names for our urls so we can use them in our template tags
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home")
]
