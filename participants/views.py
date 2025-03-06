from django.shortcuts import render, redirect
from .models import Participant
from .forms import ParticipantForm


def register_participant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("participants_list")
    else:
        form = ParticipantForm()
    return render(request, "participants/register.html", {"form": form})


def participants_list(request):
    participants = Participant.objects.all()
    return render(request, "participants/list.html", {"participants": participants})
