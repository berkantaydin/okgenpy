from django.shortcuts import render, get_object_or_404, redirect
from .models import Dreams


def dreams(request):
    dreams = Dreams.objects.all()
    return render(request, 'okgen_dreams/dreams.html', dict(dreams=dreams))


def dream(request, id):
    dream = get_object_or_404(Dreams, pk=id)
    return render(request, 'okgen_dreams/dream.html', dict(dream=dream))
