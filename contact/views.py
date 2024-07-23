# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponse

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        # Envie o e-mail
        send_mail(
            
            # f'Mensagem de {nome}', 
            # mensagem, 
            # email, 
            # ['destinatario@example.com'],
            subject="Form de Contato MEDCARE",
            message=mensagem,
            html_message=f"<b>Nome:<br/></b>{nome} <br/><b>Email:</b><br/>{email}<br/><b>Mensagem:</b><br/> {mensagem}",
            from_email=email,
            recipient_list=['leorodriguesaguiar@gmail.com'],  # Lista de destinatários
        )
        
        return redirect('contato_sucesso')
    
    return render(request, 'contato.html')

def contato_sucesso(request):
    return HttpResponse("Mensagem enviada com sucesso!")
