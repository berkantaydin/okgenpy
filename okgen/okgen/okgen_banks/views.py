from django.shortcuts import render, get_object_or_404, redirect
from .models import Banks, Branches


def banks(request):
    banks = Banks.objects.all()
    return render(request, 'okgen_banks/banks.html', dict(banks=banks))


def bank(request, slug):
    bank = get_object_or_404(Banks, slug=slug)
    return render(request, 'okgen_banks/bank.html', dict(bank=bank))


def branches(request, slug):
    branches = Branches.objects.all()
    return render(request, 'okgen_banks/branches.html', dict(branches=branches))


def branch(request, slug):
    branch = get_object_or_404(Branches, slug=slug)
    return render(request, 'okgen_banks/branch.html', dict(banks=branch))