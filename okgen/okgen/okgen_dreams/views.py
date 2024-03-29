from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Dreams


def dreams(request, page=1):
    dreams = Dreams.objects.all()

    paginator = Paginator(dreams, 50)

    try:
        dreams = paginator.page(page)
    except (EmptyPage, InvalidPage):
        dreams = paginator.page(paginator.num_pages)
    return render(request, 'okgen_dreams/dreams.html', dict(dreams=dreams))


def dream(request, slug):
    dream = get_object_or_404(Dreams, slug=slug)
    return render(request, 'okgen_dreams/dream.html', dict(dream=dream))
