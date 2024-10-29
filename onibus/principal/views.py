from django.shortcuts import render, HttpResponse
from .models import Veiculos
from autenticacao.models import Cliente
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def site_principal(request):
    return render(request, "principal.html")
    
def vizualizacao(request):
    if request.method=="GET":
        veiculos=Veiculos.objects.all()
        return render( request,'visualizacao.html',{'veiculos':veiculos})
    else:
        segunda=request.POST.get('segunda')
        quarta=request.POST.get('quarta')
        sabado=request.POST.get('sabado')
        saopaulo=request.POST.get('saopaulo')
        campinas=request.POST.get('campinas')
        rio=request.POST.get('rio')
        manha=request.POST.get('manha')
        tarde=request.POST.get('tarde')
        noite=request.POST.get('noite')

        if segunda and not quarta and not sabado:
            veiculos=Veiculos.objects.filter(dia="SE")
            # return render( request,'visualizacao.html',{'veiculos':veiculos})
        elif segunda and quarta and not sabado:
            veiculos=Veiculos.objects.filter(Q(dia='SE')|Q(dia='QA'))
            # return render( request,'visualizacao.html',{'veiculos':veiculos})
        elif segunda and not quarta and sabado:
            veiculos=Veiculos.objects.filter(Q(dia='SE')|Q(dia='SA'))
            # return render( request,'visualizacao.html',{'veiculos':veiculos})
        elif  segunda and quarta and sabado:
            veiculos=Veiculos.objects.filter(Q(dia='SA')|Q(dia='QA')|Q(dia='SE'))
            # return render( request,'visualizacao.html',{'veiculos':veiculos})
        elif  not segunda and not quarta and sabado:
            veiculos=Veiculos.objects.filter(Q(dia='SA'))
            # return render( request,'visualizacao.html',{'veiculos':veiculos})
        elif  not segunda and quarta and sabado:
            veiculos=Veiculos.objects.filter(Q(dia='QA')|Q(dia='SA'))
            # return render( request,'visualizacao.html',{'veiculos':veiculos})
        elif not segunda and quarta and not sabado :
            veiculos=Veiculos.objects.filter(Q(dia='QA'))
            # return render( request,'visualizacao.html',{'veiculos':veiculos})
        else:
            veiculos=Veiculos.objects.all()
            # return render( request,'visualizacao.html',{'veiculos':veiculos})

        if saopaulo and not campinas and not rio:
            veiculos=veiculos.filter(destino="SP")
        elif saopaulo and campinas and not rio:
            veiculos=veiculos.filter(Q(destino='SP')|Q(destino='CA'))
        elif saopaulo and not campinas and rio:
            veiculos=veiculos.filter(Q(destino='SP')|Q(destino='RI'))
        elif  saopaulo and campinas and rio:
            veiculos=veiculos.filter(Q(destino='RI')|Q(destino='CA')|Q(destino='SP'))
        elif  not saopaulo and not campinas and rio:
            veiculos=veiculos.filter(Q(destino='RI'))
        elif  not saopaulo and campinas and rio:
            veiculos=veiculos.filter(Q(destino='CA')|Q(destino='RI'))
        elif not saopaulo and campinas and not rio :
            veiculos=veiculos.filter(Q(destino='CA'))
        else:
            veiculos=veiculos
        
        if manha and not tarde and not noite:
            veiculos=veiculos.filter(horario="MA")
        elif manha and tarde and not noite:
            veiculos=veiculos.filter(Q(horario='MA')|Q(horario='TA'))
        elif manha and not tarde and noite:
            veiculos=veiculos.filter(Q(horario='MA')|Q(horario='NO'))
        elif  manha and tarde and noite:
            veiculos=veiculos.filter(Q(horario='NO')|Q(horario='TA')|Q(horario='MA'))
        elif  not manha and not tarde and noite:
            veiculos=veiculos.filter(Q(horario='TA'))
        elif  not manha and tarde and noite:
            veiculos=veiculos.filter(Q(horario='TA')|Q(horario='NO'))
        elif not manha and tarde and not noite :
            veiculos=veiculos.filter(Q(horario='TA'))
        else:
            veiculos=veiculos

        return render( request,'visualizacao.html',{'veiculos':veiculos})

def checar(request,id):
    veiculo=Veiculos.objects.get(id=id)
    
    return render (request,'checar.html',{'veiculo':veiculo})

@login_required(login_url='/auth/logar/')
def comprar(request,id):
    veiculo=Veiculos.objects.get(id=id)
    
    return render (request,'comprar.html',{'veiculo':veiculo})

@login_required(login_url='/auth/logar/')
def comprar_pas(request):
    bus=request.POST.get('bus')
    poltrona=request.POST.get('assento')
    veiculo=Veiculos.objects.get(id=bus)
    

    if poltrona=="1":
        veiculo.p1=True
        veiculo.save()
    if poltrona=="2":
        veiculo.p2=True
        veiculo.save()
    if poltrona=="3":
        veiculo.p3=True
        veiculo.save()
    if poltrona=="4":
        veiculo.p4=True
        veiculo.save()
    if poltrona=="5":
        veiculo.p5=True
        veiculo.save()
    if poltrona=="6":
        veiculo.p6=True
        veiculo.save()
    if poltrona=="7":
        veiculo.p7=True
        veiculo.save()
    if poltrona=="8":
        veiculo.p8=True
        veiculo.save()
    if poltrona=="9":
        veiculo.p9=True
        veiculo.save()
    if poltrona=="10":
        veiculo.p10=True
        veiculo.save()
    if poltrona=="11":
        veiculo.p11=True
        veiculo.save()
    if poltrona=="12":
        veiculo.p12=True
        veiculo.save()
    if poltrona=="13":
        veiculo.p13=True
        veiculo.save()
    if poltrona=="14":
        veiculo.p14=True
        veiculo.save()
    if poltrona=="15":
        veiculo.p15=True
        veiculo.save()
    if poltrona=="6":
        veiculo.p16=True
        veiculo.save()
    
    if poltrona:
        passagem=Cliente(usuario=request.user,dia=veiculo.dia,destino=veiculo.destino,horario=veiculo.horario)
        passagem.save()
        # usuario=request.user
        # usu=Cliente.objects.get(usuario=usuario)
        # usu.passagem.add(passagem)
        send_mail("confirmação de compra",f'Bom dia, usuário {request.user}. Confirmamos sua compra de passagem para {veiculo.get_destino_display()} no dia {veiculo.get_dia_display()}, horário de {veiculo.get_horario_display()}, na poltrona {poltrona}' ,"barrosjosealexandre332@gmail.com",[request.user.email])
        messages.add_message(request, constants.SUCCESS, 'Passagem comprada com sucesso. Um e-mail de confirmação foi enviado, cheque a caixa de spam.')
        return render(request,'final.html')
    else:
        messages.add_message(request, constants.ERROR, 'Escolha uma poltrona')
        return render(request,'comprar.html')

@login_required(login_url='/auth/logar/')
def agenda(request):
    passagens=[]
    for i in range(27):
        passagens.append(False)
    usuario=request.user
    clientes=Cliente.objects.filter(usuario=usuario)
    
    for cliente in clientes:
        
        if cliente.dia == "SE" and cliente.destino=="SP" and cliente.horario=="MA":
            passagens[0]=True
        
        if cliente.dia == "SE" and cliente.destino=="SP" and cliente.horario=="TA":
            passagens[1]=True

        if cliente.dia == "SE" and cliente.destino=="SP" and cliente.horario=="NO":
            passagens[2]=True
        
        if cliente.dia == "SE" and cliente.destino=="CA" and cliente.horario=="MA":
            passagens[3]=True

        if cliente.dia == "SE" and cliente.destino=="CA" and cliente.horario=="TA":
            passagens[4]=True
        
        if cliente.dia == "SE" and cliente.destino=="CA" and cliente.horario=="NO":
            passagens[5]=True
        
        if cliente.dia == "SE" and cliente.destino=="RI" and cliente.horario=="MA":
            passagens[6]=True
        
        if cliente.dia == "SE" and cliente.destino=="RI" and cliente.horario=="TA":
            passagens[7]=True
        
        if cliente.dia == "SE" and cliente.destino=="RI" and cliente.horario=="NO":
            passagens[8]=True

        if cliente.dia == "QA" and cliente.destino=="SP" and cliente.horario=="MA":
            passagens[9]=True
        
        if cliente.dia == "QA" and cliente.destino=="SP" and cliente.horario=="TA":
            passagens[10]=True

        if cliente.dia == "QA" and cliente.destino=="SP" and cliente.horario=="NO":
            passagens[11]=True
        
        if cliente.dia == "QA" and cliente.destino=="CA" and cliente.horario=="MA":
            passagens[12]=True

        if cliente.dia == "QA" and cliente.destino=="CA" and cliente.horario=="TA":
            passagens[13]=True
        
        if cliente.dia == "QA" and cliente.destino=="CA" and cliente.horario=="NO":
            passagens[14]=True
        
        if cliente.dia == "QA" and cliente.destino=="RI" and cliente.horario=="MA":
            passagens[15]=True
        
        if cliente.dia == "QA" and cliente.destino=="RI" and cliente.horario=="TA":
            passagens[16]=True
        
        if cliente.dia == "QA" and cliente.destino=="RI" and cliente.horario=="NO":
            passagens[17]=True
        
        if cliente.dia == "SA" and cliente.destino=="SP" and cliente.horario=="MA":
            passagens[18]=True
        
        if cliente.dia == "SA" and cliente.destino=="SP" and cliente.horario=="TA":
            passagens[19]=True

        if cliente.dia == "SA" and cliente.destino=="SP" and cliente.horario=="NO":
            passagens[20]=True
        
        if cliente.dia == "SA" and cliente.destino=="CA" and cliente.horario=="MA":
            passagens[21]=True

        if cliente.dia == "SA" and cliente.destino=="CA" and cliente.horario=="TA":
            passagens[22]=True
        
        if cliente.dia == "SA" and cliente.destino=="CA" and cliente.horario=="NO":
            passagens[23]=True
        
        if cliente.dia == "SA" and cliente.destino=="RI" and cliente.horario=="MA":
            passagens[24]=True
        
        if cliente.dia == "SA" and cliente.destino=="RI" and cliente.horario=="TA":
            passagens[25]=True
        
        if cliente.dia == "SA" and cliente.destino=="RI" and cliente.horario=="NO":
            passagens[26]=True
        
    
    return render(request,'agenda.html',{'passagens': passagens})