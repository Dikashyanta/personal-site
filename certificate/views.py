from django.shortcuts import render

from .models import Certificate


def certificate_view(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificate/certificate.html', {'certificates': certificates})
