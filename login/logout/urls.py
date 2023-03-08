from django.urls import path,include
from .views import UserViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'',UserViewset)
urlpatterns = [
    path('create/',include(router.urls)),
]