import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import Tag


def create_tag(tag_text, days):
    """
    Crea un Tag con el texto dado y una fecha de publicación desplazada
    en días desde ahora (negativo = pasado, positivo = futuro).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Tag.objects.create(tag_text=tag_text, pub_date=time)


class TagIndexViewTests(TestCase):
    def test_no_tags(self):
        response = self.client.get(reverse("keeps:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tags are available.")
        self.assertQuerySetEqual(response.context["latest_tag_list"], [])

    def test_past_tag(self):
        tag = create_tag("Past tag.", -30)
        response = self.client.get(reverse("keeps:index"))
        self.assertQuerySetEqual(response.context["latest_tag_list"], [tag])

    def test_future_tag(self):
        create_tag("Future tag.", 30)
        response = self.client.get(reverse("keeps:index"))
        self.assertContains(response, "No tags are available.")
        self.assertQuerySetEqual(response.context["latest_tag_list"], [])

    def test_future_tag_and_past_tag(self):
        tag = create_tag("Past tag.", -30)
        create_tag("Future tag.", 30)
        response = self.client.get(reverse("keeps:index"))
        self.assertQuerySetEqual(response.context["latest_tag_list"], [tag])

    def test_two_past_tags(self):
        tag1 = create_tag("Past tag 1.", -30)
        tag2 = create_tag("Past tag 2.", -5)
        response = self.client.get(reverse("keeps:index"))
        self.assertQuerySetEqual(response.context["latest_tag_list"], [tag2, tag1])