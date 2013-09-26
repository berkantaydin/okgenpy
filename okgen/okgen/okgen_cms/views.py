from django.shortcuts import render
from .models import Words


def landing(request):
    lang = (request.GET.get('lang',request.LANGUAGE_CODE))

    word = request.GET.get('text', None)
    if word is not None:
        word = word.lower()

    if word is not None:
        try:
            word = Words.objects.filter(word=word.lower()).get(word=word)
            word.viewed += 1
            word.save()
        except Exception as e:
            Words(word=word, viewed=1).save()

        return render(request, 'okgen_cms/results.html', dict(lang=lang));
    else:
        words = Words.objects.filter(hidden=False).order_by('-viewed').all()[:50]
        return render(request, 'okgen_cms/landing.html', dict(lang=lang, mostly_searched=words))