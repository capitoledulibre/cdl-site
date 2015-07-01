from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from symposion.proposals.models import ProposalBase
from cdl.speakers.forms import SpeakerForm
from symposion.speakers.models import Speaker


@login_required
def speaker_edit_staff(request, pk=None):
    if pk is None:
        try:
            speaker = request.user.speaker_profile
        except Speaker.DoesNotExist:
            return redirect("speaker_create")
    else:
        if request.user.is_staff:
            speaker = get_object_or_404(Speaker, pk=pk)
        else:
            raise Http404()
    
    if request.method == "POST":
        form = SpeakerForm(request.POST, request.FILES, instance=speaker)
        if form.is_valid():
            form.save()
            messages.success(request, "Speaker profile updated.")
            if request.user.is_staff:
                return redirect("user_list")
            else:
                return redirect("dashboard")
    else:
        form = SpeakerForm(instance=speaker)
    
    return render(request, "speakers/speaker_edit.html", {
        "form": form,
    })
