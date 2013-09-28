from django.shortcuts import render, get_object_or_404, redirect
from .models import Banks


def banks(request):
    banks = Banks.objects.all()
    return render(request, 'okgen_banks/banks.html', dict(banks=banks))


def bank(request, id):
    # TODO: SLUG OLACAK
    banks = Banks.objects.all()
    return render(request, 'okgen_banks/bank.html', dict(banks=bank))