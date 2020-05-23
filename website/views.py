from django.views.generic import ListView
from .models import Session

class SessionList(ListView):
    model = Session
