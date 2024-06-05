from django.shortcuts import render

# Create your views here.

import random
import string

def generate_password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))
        include_lowercase = request.POST.get('include_lowercase', False)
        include_uppercase = request.POST.get('include_uppercase', False)
        include_digits = request.POST.get('include_digits', False)
        include_special_chars = request.POST.get('include_special_chars', False)

        characters = ''
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        context = {'password': password}
        return render(request, 'index.html', )

    return render(request, 'index.html')
