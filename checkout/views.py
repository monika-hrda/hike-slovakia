from django.shortcuts import render, get_object_or_404
from hikes.models import Hike


def checkout(request, hike_id):
    # bag = request.session.get('bag', {})
    # if not bag:
    #     messages.error(request, "There's nothing in your bag at the moment")
    #     return redirect(reverse('products'))

    hike = get_object_or_404(Hike, pk=hike_id)

    hike_date = None
    if 'hike_date' in request.POST:
        hike_date = request.POST['hike_date']

    num_hikers = 1
    if 'number_of_people' in request.POST:
        num_hikers = request.POST['number_of_people']

    # order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'hike': hike,
        'hike_date': hike_date,
        'num_hikers': num_hikers,
        # 'order_form': order_form,
    }

    return render(request, template, context)
