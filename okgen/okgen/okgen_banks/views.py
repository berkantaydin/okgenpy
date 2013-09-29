from django.shortcuts import render, get_object_or_404, redirect
from .models import Banks, Branches


def banks(request):
    banks = Banks.objects.all()
    return render(request, 'okgen_banks/banks.html', dict(banks=banks))


def bank(request, id):
    get_object_or_404(Banks, pk=id)
    return render(request, 'okgen_banks/bank.html', dict(banks=bank))


def branches(request):
    branches = Branches.objects.all()
    return render(request, 'okgen_banks/branches.html', dict(branches=branches))


def branch(request, id):
    get_object_or_404(Branches, pk=id)
    return render(request, 'okgen_banks/branch.html', dict(banks=bank))