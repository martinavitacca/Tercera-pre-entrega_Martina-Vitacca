from django.shortcuts import render
from django.http import HttpResponse # Se importa para la respuesta
# from django.contrib.auth import login, authenticate
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html") 

def adventure(request):
    contexto = {'juegos': Adventure.objects.all()}
    return render(request, "aplicacion/adventure.html", contexto) 

def puzzle(request):
    contexto = {'juegos': Puzzle.objects.all()}
    return render(request, "aplicacion/puzzle.html", contexto) 

def retro(request):
    contexto = {'juegos': Retro.objects.all()}
    return render(request, "aplicacion/retro.html", contexto) 

def rpgHorror(request):
    contexto = {'juegos': RPGHorror.objects.all()}
    return render(request, "aplicacion/rpg_horror.html", contexto) 

def stealth(request):
    contexto = {'juegos': Stealth.objects.all()}
    return render(request, "aplicacion/stealth.html", contexto) 

def survival(request):
    contexto = {'juegos': Survival.objects.all()}
    return render(request, "aplicacion/survival.html", contexto) 

def user(request):
    contexto = {'players': Player.objects.all()}
    return render(request, "aplicacion/user.html", contexto) 
  

# Formulario para agregar en Categoria 1
def adventureForm(request):
    if request.method == "POST":
        formAdventure = AdventureForm(request.POST) # Toma los datos del formulario
        if formAdventure.is_valid(): # Consulta si es valido
            adventureTitle = formAdventure.cleaned_data.get('title') # Información limpia que viene por ser valido el formulario
            adventureDeveloper = formAdventure.cleaned_data.get('developer')
            adventurePlatform = formAdventure.cleaned_data.get('platform')
            adventureMode = formAdventure.cleaned_data.get('mode')
            # Se crea un objeto con los datos ingresados por el usuario
            juego = Adventure(title=adventureTitle,
                              developer=adventureDeveloper,
                              platform=adventurePlatform,
                              mode=adventureMode)
            juego.save()
            return render(request, "aplicacion/home.html")
    else:
        formAdventure = AdventureForm() # Se crea formulario vacio desde la clase Adventure creada en forms.py
    
    return render(request, 'aplicacion/form.html', {"form": formAdventure})

# Busqueda Categoría 1
def adventureSearch(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        juegos = Adventure.objects.filter(title__icontains=patron)
        contexto = {'juegos': juegos}
        return render(request, 'aplicacion/adventure.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

# 
# 
# 
# Formulario para agregar en Categoria 2
def puzzleForm(request):
    if request.method == "POST":
        formPuzzle = PuzzleForm(request.POST) 
        if formPuzzle.is_valid(): 
            puzzleTitle = formPuzzle.cleaned_data.get('title') 
            puzzleDeveloper = formPuzzle.cleaned_data.get('developer')
            puzzlePlatform = formPuzzle.cleaned_data.get('platform')
            puzzleMode = formPuzzle.cleaned_data.get('mode')
            juego = Puzzle(title=puzzleTitle,
                              developer=puzzleDeveloper,
                              platform=puzzlePlatform,
                              mode=puzzleMode)
            juego.save()
            return render(request, "aplicacion/home.html")
    else:
        formPuzzle = PuzzleForm()
    
    return render(request, 'aplicacion/form2.html', {"form2": formPuzzle})

# Busqueda Categoría 2
def puzzleSearch(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        juegos = Puzzle.objects.filter(title__icontains=patron)
        contexto = {'juegos': juegos}
        return render(request, 'aplicacion/puzzle.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

# 
# 
# 
# Formulario para agregar en Categoria 3
def retroForm(request):
    if request.method == "POST":
        formRetro = RetroForm(request.POST) 
        if formRetro.is_valid():
            retroTitle = formRetro.cleaned_data.get('title') 
            retroDeveloper = formRetro.cleaned_data.get('developer')
            retroPlatform = formRetro.cleaned_data.get('platform')
            retroMode = formRetro.cleaned_data.get('mode')
            juego = Retro(title=retroTitle,
                              developer=retroDeveloper,
                              platform=retroPlatform,
                              mode=retroMode)
            juego.save()
            return render(request, "aplicacion/home.html")
    else:
        formRetro = RetroForm()
    
    return render(request, 'aplicacion/form3.html', {"form3": formRetro})

# Busqueda Categoría 3
def retroSearch(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        juegos = Retro.objects.filter(title__icontains=patron)
        contexto = {'juegos': juegos}
        return render(request, 'aplicacion/retro.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

# 
# 
# 
# Formulario para agregar en Categoria 4
def rpgForm(request):
    if request.method == "POST":
        formRpg = RpgForm(request.POST) 
        if formRpg.is_valid():
            rpgTitle = formRpg.cleaned_data.get('title') 
            rpgDeveloper = formRpg.cleaned_data.get('developer')
            rpgPlatform = formRpg.cleaned_data.get('platform')
            juego = RPGHorror(title=rpgTitle,
                              developer=rpgDeveloper,
                              platform=rpgPlatform)
            juego.save()
            return render(request, "aplicacion/home.html")
    else:
        formRpg = RpgForm() 
    
    return render(request, 'aplicacion/form4.html', {"form4": formRpg})

# Busqueda Categoría 4
def rpgSearch(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        juegos = RPGHorror.objects.filter(title__icontains=patron)
        contexto = {'juegos': juegos}
        return render(request, 'aplicacion/rpg_horror.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

# 
# 
# 
# Formulario para agregar en Categoria 5
def stealthForm(request):
    if request.method == "POST":
        formStealth = SurvivalForm(request.POST) 
        if formStealth.is_valid():
            stealthTitle = formStealth.cleaned_data.get('title') 
            stealthDeveloper = formStealth.cleaned_data.get('developer')
            stealthPlatform = formStealth.cleaned_data.get('platform')
            stealthMode = formStealth.cleaned_data.get('mode')
            juego = Stealth(title=stealthTitle,
                              developer=stealthDeveloper,
                              platform=stealthPlatform,
                              mode=stealthMode)
            juego.save()
            return render(request, "aplicacion/home.html")
    else:
        formStealth = StealthForm()
    
    return render(request, 'aplicacion/form5.html', {"form5": formStealth})

# Busqueda Categoría 5
def stealthSearch(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        juegos = Stealth.objects.filter(title__icontains=patron)
        contexto = {'juegos': juegos}
        return render(request, 'aplicacion/stealth.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

# 
# 
# 
# Formulario para agregar en Categoria 6
def survivalForm(request):
    if request.method == "POST":
        formSurvival = SurvivalForm(request.POST) 
        if formSurvival.is_valid():
            survivalTitle = formSurvival.cleaned_data.get('title') 
            survivalDeveloper = formSurvival.cleaned_data.get('developer')
            survivalPlatform = formSurvival.cleaned_data.get('platform')
            survivalMode = formSurvival.cleaned_data.get('mode')
            juego = Survival(title=survivalTitle,
                              developer=survivalDeveloper,
                              platform=survivalPlatform,
                              mode=survivalMode)
            juego.save()
            return render(request, "aplicacion/home.html")
    else:
        formSurvival = SurvivalForm()
    
    return render(request, 'aplicacion/form6.html', {"form6": formSurvival})

# Busqueda Categoría 6
def survivalSearch(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        juegos = Survival.objects.filter(title__icontains=patron)
        contexto = {'juegos': juegos}
        return render(request, 'aplicacion/survival.html', contexto)
    return HttpResponse("No se ingreso ningun dato")

# 
# 
# 
# Formulario para agregar jugador
def userForm(request):
    if request.method == "POST":
        formUser = PlayerForm(request.POST) 
        if formUser.is_valid():
            userName = formUser.cleaned_data.get('name') 
            userSurname = formUser.cleaned_data.get('surname')
            userUser_name = formUser.cleaned_data.get('user_name')
            userEmail = formUser.cleaned_data.get('email')
            player = Player(name=userName,
                            surname=userSurname,
                            user_name=userUser_name,
                            email=userEmail)
            player.save()
            return render(request, "aplicacion/home.html")
    else:
        formUser = PlayerForm()
    
    return render(request, 'aplicacion/form_user.html', {"form_user": formUser})


# def sign_in(request):
#     if request.method == 'GET':
#         form_user = LoginForm()
#         return render(request, 'aplicacion/user.html', {'form_user': form_user})
#     elif request.method == 'POST':
#         form_user = LoginForm(request.POST)
        
#         if form_user.is_valid():
#             username = form_user.cleaned_data['user_name']
#             password = form_user.cleaned_data['password']
#             user = authenticate(request,username=username,password=password)
#             if user:
#                 login(request, user)
#                 print(request,f'Hi, welcome back!')
#                 return render(request, "aplicacion/home.html")
        
#         # form is not valid or user is not authenticated
#         print(request,f'Invalid username or password')
#         return render(request,'aplicacion/user.html',{'form_user': form_user})

