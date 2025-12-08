from django.urls import path
from .views import RegisterView, ProtectedTestView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('test/', ProtectedTestView.as_view(), name='protected-test'),
]
