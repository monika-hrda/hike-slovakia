from django.shortcuts import render


def contact(request):
    """ A view to return the contact page """

    template = 'contact/contact.html'
    context = {
    }

    return render(request, template, context)
