from django.test import TestCase, Client
from django.utils.text import slugify

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


class VacancyModelTestCase(TestCase):
    def setUp(self):
        self.vacation_name = 'New Python Vacation'
        self.tag_title = 'Python3'
        self.tag = Tag.objects.create(title=self.tag_title)
        self.vacation = Vacancy.objects.create(title=self.vacation_name,
            description='Vacation description')

    def test_tag_slug(self):
        slug = slugify(self.tag_title)
        self.assertEqual(slug, self.tag.slug)

    def test_vacancy_slug(self):
        slug = slugify(self.vacation_name)
        self.assertEqual(slug, self.vacation.slug)
