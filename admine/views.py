from django.shortcuts import render
from myapp.models import *
# Create your views here.


def contact(request):
    contacts = Contact.objects.all()
    
    # Render the template using the combined context
    return render(request, 'myApp/contactingMessage.html', {'Contact': contacts})