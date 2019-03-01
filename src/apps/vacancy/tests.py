from django.test import TestCase, Client

from .models import Vacancy, Tag


class VacancyDetailViewTestCase(TestCase):
    def setUp(self):
        self.description = 'Bla bla bla, blah-blah-blay!'
        Vacancy.objects.create(
            title='New senior python develover vacancy',
            description=self.description,
            slug='new_senior_vac_1',
            is_activated=True,
        )

    def test_if_it_shows_description(self):
        client = Client()
        response = client.get('/vacancies/vacancy_detail/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.description)
