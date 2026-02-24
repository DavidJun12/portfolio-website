from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . import models
from .models import Contact
from django.http import JsonResponse

def home(request):
    return render(request,'home.html')


def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        number=request.POST.get('number')
        print(name,email,number,content)

        #if len(name)>1 and len(name)<30:
        #    pass
        #else:
        #    messages.error(request,'length of name be between 2-30 chars')
        #    return render(request,'home.html')
        
        #if len(email)>1 and len(email)<30:
        #    pass
        #else:
        #    messages.error(request,'invalid email try again')
        #    return render(request,'home.html')
        
        #if len(number)>2 and len(number)<13:
        #    pass
        #else:
        #    messages.error(request,'invalid number try again')
        #    return render(request,'home.html')
        
        #ins=models.Contact(name=name,email=email,content=content, number=number)
        #ins.save()
        #messages.success(request,'Thankyou for contacting me || your message has been saved')
        #print('data has been saved to database')

        Contact.objects.create(
            name = name,
            email = email,
            content = content,
            number = number
        )

    #return render(request,'home.html')
    #return redirect('/#contact')
    
    return JsonResponse({
        "status": "success",
        "message": "Thankyou for contacting me 👍 Your message has been saved "
    })