from django.shortcuts import render
from .models import Links, Words

from math import log
def tagcloud(threshold=0, maxsize=1.75, minsize=.75):
    """usage:
        -threshold: Tag usage less than the threshold is excluded from
            being displayed.  A value of 0 displays all tags.
        -maxsize: max desired CSS font-size in em units
        -minsize: min desired CSS font-size in em units
    Returns a list of dictionaries of the tag, its count and
    calculated font-size.
    """

    return tagcloud

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
        links = Links.objects.filter(hidden=False).all()

        counts, taglist, tagcloud = [], [], []
        tags = Links.objects.filter(hidden=False).all()

        words = Words.objects.filter(hidden=False).order_by('-viewed').all()[:50]
        return render(request, 'okgen_cms/landing.html', dict(
            lang=lang, tagcloud=tagcloud, words=words))