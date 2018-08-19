from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
# Create your views here.
from contact.forms import ContactForm
from django.core.mail import send_mail


def contact_view(request):
    form_class = ContactForm

    #the logic
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():

            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            #Email the profile with the contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['rlezamaswift@gmail.com'],
                headers = {'Reply-To': contact_email}
                )
            #send_mail(subject, message, from_email, to_list, fail_silently = True)
            

            subject = "Thank You for your message, I'll try to answer as soon as possible"
            message = "Hello, I appreciate your email"
            from_email = settings.EMAIL_HOST_USER
            to = [email, settings.EMAIL_HOST_USER]
            send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
            messages.success(request, "The message has been sent")
            return redirect('contactRedirect')


    return render(request, 'contact.html',{
        'form':form_class
        })