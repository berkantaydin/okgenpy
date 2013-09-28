from math import log

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Links, Words


def landing(request):
    lang = (request.GET.get('lang', request.LANGUAGE_CODE))

    word = request.GET.get('text', None)
    if word is not None:
        word = word.lower().strip()

    if word is not None and len(word) > 1:
        try:
            word = Words.objects.filter(word=word.lower()).get(word=word)
            word.viewed += 1
            word.save()
        except Exception as e:
            Words(word=word, viewed=1).save()

        return render(request, 'okgen_cms/results.html', dict(lang=lang))
    else:
        counts, taglist, tagcloud = [], [], []
        tags = Links.objects.filter(hidden=False).all()

        if len(tags) > 1:
            for tag in tags:
                count = tag.clicked
                count >= 0 and (counts.append(count), taglist.append(tag))
            maxcount = max(counts)
            mincount = min(counts)
            constant = log(maxcount - (mincount - 1))/(settings.TAG_CLOUD_MAX_FONT_SIZE - settings.TAG_CLOUD_MIN_FONT_SIZE or 1)
            tagcount = zip(taglist, counts)
            for tag, count in tagcount:
                try:
                    size = log(count - (mincount - 1))/constant + settings.TAG_CLOUD_MIN_FONT_SIZE
                except ZeroDivisionError:
                    size = 7
                    pass

                tagcloud.append({'tag': tag, 'count': count, 'size': int(round(size, 7))})

        words = Words.objects.filter(hidden=False).order_by('-viewed').all()[:50]
        return render(request, 'okgen_cms/landing.html', dict(
            lang=lang, tagcloud=tagcloud, mostly_searched=words))


def link_clicked(request, id):
    link = get_object_or_404(Links, pk=id)
    link.clicked += 1
    link.save()
    return redirect(link.link)


def searched_words(request, page):
    words = Words.objects.filter(hidden=False).order_by('word').order_by('-viewed').all()
    paginator = Paginator(words, 50)

    try:
        words = paginator.page(page)
    except (EmptyPage, InvalidPage):
        words = paginator.page(paginator.num_pages)

    return render(request,
                  'okgen_cms/searched_words.html', dict(words=words),)


def speed_test(request):
    return render(request, 'okgen_cms/speed_test.html')