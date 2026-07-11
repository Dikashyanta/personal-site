from django.test import TestCase
from django.urls import reverse

from .models import Certificate


class CertificatePageTests(TestCase):
    def test_certificate_page_displays_admin_certificates(self):
        certificate = Certificate.objects.create(
            title='Django for Beginners',
            issuer='Udemy',
            category='Web Development',
            date_display='March 2024',
            takeaway='Built my first real Django app.',
        )

        response = self.client.get(reverse('certificate:certificate'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, certificate.title)
        self.assertContains(response, certificate.issuer)
        self.assertContains(response, certificate.category)
        self.assertContains(response, certificate.takeaway)
