from django.test import TestCase
from django.urls import reverse

from .models import Category, HeroSection, Interest


class AboutPageTests(TestCase):
    def test_about_page_renders_with_interests(self):
        HeroSection.objects.create(
            headline='Building things',
            bio_letter='A short note about me.',
        )
        category = Category.objects.create(name='Reading', slug='reading')
        Interest.objects.create(
            category=category,
            title='Books',
            description='Currently reading a lot.',
            cover_image='interests/covers/books.jpg',
        )

        response = self.client.get(reverse('about:about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Books')
        self.assertContains(response, 'Reading')
