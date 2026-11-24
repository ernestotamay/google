from django.utils import timezone
from django.views import generic
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Tag, Note

class IndexView(generic.ListView):
    template_name = "keeps/index.html"
    context_object_name = "latest_tag_list"

    def get_queryset(self):
        """Últimas 5 tags publicadas (excluye futuras)."""
        return Tag.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Tag
    template_name = "keeps/detail.html"

    def get_queryset(self):
        """Excluye tags no publicadas todavía."""
        return Tag.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Tag
    template_name = "keeps/results.html"


def vote(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    try:
        selected_note = tag.note_set.get(pk=request.POST["note"])
    except (KeyError, Note.DoesNotExist):
        return render(
            request,
            "keeps/detail.html",
            {
                "tag": tag,
                "error_message": "You didn't select a note.",
            },
        )
    else:
        selected_note.votes = F("votes") + 1
        selected_note.save()
        return HttpResponseRedirect(reverse("keeps:results", args=(tag.id,)))