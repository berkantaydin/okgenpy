from django.shortcuts import render, get_object_or_404, redirect
from .models import Banks, Branches


def banks(request):
    banks = Banks.objects.all()
    return render(request, 'okgen_banks/banks.html', dict(banks=banks))


def bank(request, slug):
    bank = get_object_or_404(Banks, slug=slug)
    bank.viewed += 1
    bank.save()
    return render(request, 'okgen_banks/bank.html', dict(bank=bank))


def branches(request, slug):
    bank = get_object_or_404(Banks, slug=slug)
    branches = Branches.objects.filter(bank=bank).order_by('city').all()
    return render(request, 'okgen_banks/branches.html', dict(bank=bank, branches=branches))


def branch(request, id):
    branch = get_object_or_404(Branches, id=id)
    bank = branch.bank
    return render(request, 'okgen_banks/branch.html', dict(bank=bank, branch=branch))