from django.urls import path
from credentials.views import *

urlpatterns = [
    path('', SignupView.as_view(template_name='student/student_register.html')),
]
