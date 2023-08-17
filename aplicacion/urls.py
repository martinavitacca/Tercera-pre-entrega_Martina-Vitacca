from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', home, name="home"), #Cuando no llegue nada a la ruta, invoca a home
    path('adventure/', adventure, name="adventure"),
    path('puzzle/', puzzle, name="puzzle"),
    path('retro/', retro, name="retro"),
    path('rpg_horror/', rpgHorror, name="rpg_horror"),
    path('stealth/', stealth, name="stealth"),
    path('survival/', survival, name="survival"),
    path('user/', user, name="user"),


    path('form/', adventureForm, name="form"),
    path('found_adventure_game/', adventureSearch, name="found_adventure_game"),

    path('form2/', puzzleForm, name="form2"),
    path('found_puzzle_game/', puzzleSearch, name="found_puzzle_game"),

    path('form3/', retroForm, name="form3"),
    path('found_retro_game/', retroSearch, name="found_retro_game"),

    path('form4/', rpgForm, name="form4"),
    path('found_rpg_game/', rpgSearch, name="found_rpg_game"),

    path('form5/', stealthForm, name="form5"),
    path('found_stealth_game/', stealthSearch, name="found_stealth_game"),

    path('form6/', survivalForm, name="form6"),
    path('found_survival_game/', survivalSearch, name="found_survival_game"),

    path('form_user/', userForm, name="form_user"),

    # path('login/', sign_in, name="login"),
]
