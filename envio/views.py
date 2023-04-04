from django.shortcuts import render
from django.http import HttpResponse
"""
from django.core.mail import send_mail 

def enviar_email(request):
    #send_mail('Assunto', 'Menssagem', 'remetente', ['destinatario', 'destinatario', ...])
    send_mail('Assunto', 'Menssagem', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    return HttpResponse('Olá')
"""

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings #importar dados sensiveis do .env (biblioteca python_decouple)

nome = 'Glauber Monteiro'
data = '04/04/23'

def enviar_email(request):
  
  html_content = render_to_string('emails/cadastroconfirmado.html', {'nome': nome, 'data': data})
  text_content = strip_tags(html_content) #converter o html para txt (remover tudo que se pareça com uma tag html).

  email = EmailMultiAlternatives('Cadastro Confirmado', text_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER]) #EMAIL_HOST_USER foi cadastrado no .env
  email.attach_alternative(html_content, 'text/html')
  email.send()

  return HttpResponse('Olá')