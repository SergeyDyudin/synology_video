import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Records


def create_record(title, days):
    """
    Create a record with the given `title` and published the
    given number of `days` offset to now (negative for record published
    in the past, positive for record that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    r = Records(title=title, time_create=time, time_update=time)
    r.save_with_slug()
    return r
    # return Records.objects.create(title=title, time_create=time, time_update=time)


class RecordIndexViewTests(TestCase):
    def test_no_records(self):
        """
        If no records exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('records:home'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No records are available.")
        self.assertQuerysetEqual(response.context['records_list'], [])

    def test_past_record(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        record = create_record(title="Past record.", days=-30)
        response = self.client.get(reverse('records:home'))
        self.assertQuerysetEqual(
            response.context['records_list'],
            [record],
        )

    def test_future_record(self):
        """
        Record with a pub_date in the future aren't displayed on
        the index page.
        """
        create_record(title="Future record.", days=30)
        response = self.client.get(reverse('records:home'))
        # self.assertContains(response, "No records are available.")
        self.assertQuerysetEqual(response.context['records_list'], [])

    def test_future_records_and_past_records(self):
        """
        Even if both past and future records exist, only past records
        are displayed.
        """
        record = create_record(title="Past record.", days=-30)
        create_record(title="Future record.", days=30)
        response = self.client.get(reverse('records:home'))
        self.assertQuerysetEqual(
            response.context['records_list'],
            [record],
        )

    def test_two_past_records(self):
        """
        The records index page may display multiple records.
        """
        record1 = create_record(title="Past record 1.", days=-30)
        record2 = create_record(title="Past record 2.", days=-5)
        response = self.client.get(reverse('records:home'))
        self.assertQuerysetEqual(
            response.context['records_list'],
            [record2, record1],
        )
