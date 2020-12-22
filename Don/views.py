from django.shortcuts import render
from Admin.models import Don,Utilisateur
from .table import DonateurForm
from Statistique.views import getStatistique
from .form import UtilisateurForm, rawUtilisateurForm
# Create your views here.



def suiviDon(request):
    #getStatistique()
    form = DonateurForm()
    return render(request,'don.html', {'form': form , 'dataDon':Don.objects.all()})

def inscription (request ):
    my_form=rawUtilisateurForm()
    if request.method=="POST":
        my_form=rawUtilisateurForm(request.POST)
        if my_form.is_valid():
            Utilisateur.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context ={ 
        "form":my_form
    }


    return render(request,'inscription.html',context)
