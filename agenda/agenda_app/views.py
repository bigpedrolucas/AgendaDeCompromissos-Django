from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from datetime import datetime
from .models import Compromisso
from .forms import formCompromisso

def listaCompromissos(request):
    option = request.GET.get('filter', False)
    if option:
        listaCompromissos = Compromisso.objects.all().filter(status=option)
    else:
        listaCompromissos = Compromisso.objects.all().order_by('data')
    return render(request, 'agenda_app/home.html', {'listaCompromissos': listaCompromissos})

def compromissoView(request, id):
    compromisso = get_object_or_404(Compromisso, pk=id)
    return render(request, 'agenda_app/compromisso.html', {'compromisso': compromisso})

def novoCompromisso(request):
    if request.method == 'POST':
        formulario = formCompromisso(request.POST)
        dataForm = datetime.strptime(request.POST.get('data'), "%Y-%m-%d").date()
        inicioForm = datetime.strptime(request.POST.get('hora_Inicio'), "%H:%M").time()
        fimForm = datetime.strptime(request.POST.get('hora_Fim'), "%H:%M").time()

        listaCompromissos = Compromisso.objects.all()
        
        for compromisso in listaCompromissos:
            if (dataForm == compromisso.data and 
            (compromisso.hora_Inicio <= inicioForm <= compromisso.hora_Fim or
            compromisso.hora_Inicio <= fimForm <= compromisso.hora_Fim) or
            (inicioForm < compromisso.hora_Inicio and fimForm > compromisso.hora_Fim)):
                    messages.info(request, 'Choque de horário com o evento "{}"'.format(compromisso.titulo))
                    return render(request, 'agenda_app/novoCompromisso.html', {'form': formulario})

        if formulario.is_valid():
            compromisso = formulario.save(commit=False)
            compromisso.save()
            return HttpResponseRedirect('/')
    else:
        formulario = formCompromisso()
    return render(request, 'agenda_app/novoCompromisso.html', {'form': formulario})

def editarCompromisso(request, id):
    compromisso = get_object_or_404(Compromisso, pk=id)
    formulario = formCompromisso(instance=compromisso)

    if(request.method == 'POST'):
        formulario = formCompromisso(request.POST, instance=compromisso)
        tituloForm = request.POST.get('titulo')
        dataForm = datetime.strptime(request.POST.get('data'), "%Y-%m-%d").date()
        inicioForm = datetime.strptime(request.POST.get('hora_Inicio'), "%H:%M:%S").time()
        fimForm = datetime.strptime(request.POST.get('hora_Fim'), "%H:%M:%S").time()

        listaCompromissos = Compromisso.objects.all()
        comp = get_object_or_404(Compromisso, pk=id)
        
        for comp in listaCompromissos:
            if (tituloForm != comp.titulo and dataForm == comp.data and 
            (comp.hora_Inicio <= inicioForm <= comp.hora_Fim or
            comp.hora_Inicio <= fimForm <= comp.hora_Fim) or
            (inicioForm < comp.hora_Inicio and fimForm > comp.hora_Fim)):
                    messages.info(request, 'Choque de horário com o evento "{}"'.format(comp.titulo))
                    return render(request, 'agenda_app/editarCompromisso.html', {'form': formulario})
            else:
                break

        if(formulario.is_valid()):
            compromisso.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'agenda_app/editarCompromisso.html', {'form': formulario, 'compromisso': compromisso})
    else:
        return render(request, 'agenda_app/editarCompromisso.html', {'form': formulario, 'compromisso': compromisso})

def excluirCompromisso(request, id):
    compromisso = get_object_or_404(Compromisso, pk=id)
    compromisso.delete()

    messages.info(request, '"{}" excluído com sucesso'.format(compromisso.titulo))
    return HttpResponseRedirect('/')