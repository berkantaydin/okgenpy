from django.template.loader import render_to_string


def ads(request):
    return {
        "ads160x600": render_to_string('ads/160x600.html'),
        "ads160x90": render_to_string('ads/160x90.html'),
        "ads728x90": render_to_string('ads/728x90.html'),
        "ads336x280": render_to_string('ads/336x280.html'),
        "ads320x50": render_to_string('ads/320x50.html'),
        "ads300x250": render_to_string('ads/300x250.html'),
        "ads200x200": render_to_string('ads/200x200.html'),
    }