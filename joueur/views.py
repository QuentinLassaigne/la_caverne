from django.shortcuts import render

# Create your views here.

from .forms import CreaPersoForm

def calcul(request):
    """Display calcul results and save user's personnage information."""

    if request.method == "POST":
        form_perso = CreaPersoForm(request.POST)

    form_perso = CreaPersoForm()

    return render(request, "joueur/perso.html", { "form_perso": form_perso })