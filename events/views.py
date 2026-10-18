from django.http import HttpResponse


def welcome_view(request):
    return HttpResponse("Welcome to EventHub – the platform for managing events and tickets!")


def about_view(request):
    return HttpResponse(
        "EventHub lets organizers create and publish events such as conferences, workshops and concerts, "
        "lets attendees buy tickets for them, and allows everyone to rate and review the events they attended."
    )
