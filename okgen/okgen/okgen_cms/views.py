from math import log
from django.shortcuts import render, get_object_or_404
from .models import Links, Words
from django.core.urlresolvers import reverse

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
        max_clicked = 1
        min_clicked = 1000000
        for link in links:
            max_clicked = link.clicked > max_clicked if link.clicked else max_clicked
            min_clicked = link.clicked < min_clicked if link.clicked else min_clicked

        counts, taglist, tagcloud = [], [], []
        tags = Links.objects.filter(hidden=False).all()
        if len(tags) > 1:
            for tag in tags:
                count = tag.clicked
                count >= 0 and (counts.append(count), taglist.append(tag))
            maxcount = max(counts)
            mincount = min(counts)
            constant = log(maxcount - (mincount - 1))/(22 - 8 or 1)
            tagcount = zip(taglist, counts)
            for tag, count in tagcount:
                size = log(count - (mincount - 1))/constant + 8
                tagcloud.append({'tag': tag, 'count': count, 'size': round(size, 7)})

        words = Words.objects.filter(hidden=False).order_by('-viewed').all()[:50]
        return render(request, 'okgen_cms/landing.html', dict(
            lang=lang, tagcloud=tagcloud, mostly_searched=words))


def link_clicked(request):
    print "--------------------------------------"
    #link = Links.objects.get_object_or_404(pk=id)
