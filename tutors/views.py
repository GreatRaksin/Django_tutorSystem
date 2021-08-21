from django.shortcuts import render, redirect
from .forms import TutorSelectForm
from .models import Tutor

# Create your views here.
def index(request):
    form = TutorSelectForm()

    if form.is_valid():
        predm = form.cleaned_data.get('subject')
        city = form.cleaned_data.get('city')
        tutors = Tutor.objects.all().filter(subject=1, city=1)
        print(predm, city)
        return render(request, 'index.html', {'form': form, 'tutors': tutors})
    else:
        tutors = []
    return render(request, 'index.html', {'form': form,
                                          'tutors': tutors})