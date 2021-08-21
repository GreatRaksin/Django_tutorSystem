from django.shortcuts import render, redirect
from .forms import TutorSelectForm
from .models import Tutor

# Create your views here.
def index(request):
    form = TutorSelectForm()
    town = request.GET.get('city')
    predm = request.GET.get('subject')
    tutors = Tutor.objects.filter(city=town, subject=predm)

    return render(request, 'index.html', {'form': form,
                                          'tutors': tutors})