from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Certificate
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from reportlab.lib.pagesizes import letter
from io import BytesIO
from .forms import RegistrationForm
from django.contrib import messages
import os

# certificates create/views
def create_certificate(request):
    if request.method == 'POST':
        # Handle form submission and generate PDF certificate using reportlab or WeasyPrint
        # Save the certificate to the database
        # Return the generated PDF for download or display

        # Example:
        name= request.POST['name']
        subtitle = request.POST['subtitle']
        date = request.POST['date']
        sign= request.POST['sign']

        # Generate the PDF certificate (You need to write this part using reportlab or WeasyPrint)

        # Save the certificate to the database
        certificate = Certificate(name=name, subtitle=subtitle, date=date, sign=sign)
        certificate.save()

        # Return the PDF certificate to the user (You need to write this part)
        return redirect("list")
    return render(request, 'create_certificate.html')

# certificates verification/views
def verify_certificate(request):
    if request.method == 'POST':
        # Handle form submission for certificate verification

        # Example:
        certificate_id = request.POST['certificate_id']

        # Retrieve the certificate from the database
        certificate = get_object_or_404(Certificate, id=certificate_id)

        # Compare the provided details with the stored details for verification
        # You can use cryptographic hashing to compare the data to enhance security

        # Return the verification result to the user (You need to write this part)
        return HttpResponse("<h1>Certificate verified successfully!</h1>")
    return render(request, 'verify_certificate.html')


# certificates/views.pyimport os
def generate_certificate(request, certificate_id):
    certificate = Certificate.objects.get(pk=certificate_id)
    
    # Specify the path to the certificate template image
    template_path = os.path.join(settings.STATICFILES_DIRS[0], 'certificates', 'Certificate.png')
    
    # Load the certificate template image
    template_image = Image.open(template_path)

    # Load a font (change the font path to your desired font file)
    font_path = os.path.join(settings.STATICFILES_DIRS[0], 'certificates', 'arial.ttf')
    font = ImageFont.truetype(font_path, 36)  # Adjust font size as needed
    
    # Create a drawing context
    draw = ImageDraw.Draw(template_image)
    
    # Define the position to place the dynamic data on the certificate
    name_position = (700, 535)
    subtitle_position = (680, 750)
    date_position = (290, 985)
    sign_position = (1150, 985)
    
    # Insert dynamic data into the certificate image
    draw.text(name_position, certificate.name, fill='black', font=font)
    draw.text(subtitle_position, certificate.subtitle, fill='black', font=font)
    draw.text(date_position, str(certificate.date), fill='black', font=font)
    draw.text(sign_position, certificate.sign, fill='black', font=font)

    # Create a PDF document
    buffer = BytesIO()
    pdf_image = template_image.convert("RGB")
    pdf_image.save(buffer, format="PDF")

    # Serve the generated PDF for download
    buffer.seek(0)
    response = HttpResponse(buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    return response


#fetchin all certificates/views  
def listPage(request):
    certificates = Certificate.objects.all()
    return render(request,'certificates_list.html',{'certificates':certificates})

#view for registration page
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #reteriving user name 
            name=form.cleaned_data.get('name')
            messages.success(request,f'welcome {name} your account is register')
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'register.html',{'form':form})

#restrict access profile 



