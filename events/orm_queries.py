from decimal import Decimal

from events.models import Event


def published_events():
    return Event.objects.filter(is_published=True).order_by('date')


def large_events():
    return Event.objects.filter(capacity__gte=50)


def free_events_count():
    return Event.objects.filter(price=Decimal('0.00')).count()


def unpublish_event(event_id):
    event = Event.objects.get(id=event_id)
    event.is_published = False
    event.save()
    return event


def run():
    print("Published events (chronological):")
    for event in published_events():
        print(f"  {event}")

    print("Events with capacity of at least 50:")
    for event in large_events():
        print(f"  {event} - capacity {event.capacity}")

    print(f"Number of free events: {free_events_count()}")

    first_published = published_events().first()
    if first_published is None:
        print("No published event to unpublish.")
        return
    event = unpublish_event(first_published.id)
    event.refresh_from_db()
    print(f"Unpublished event: {event} - is_published={event.is_published}")
