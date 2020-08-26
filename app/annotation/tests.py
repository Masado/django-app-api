import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Annotation


class AnnotationModelTests(TestCase):
    def test_was_published_recently_with_future_annotation(self):
        """
        was_published_recently() returns false for annotation whose pub_date
        is in the furutre
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_annotation = Annotation(pub_date=time)
        self.assertIs(future_annotation.was_published_recently(), False)
