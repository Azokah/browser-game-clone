from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView,DetailView
from game.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin ##Login required
##Signup
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.forms import ModelForm
##Correos
from django.shortcuts import get_object_or_404

##Index redirect
def IndexView(request):
    if request.user.is_authenticated:
        return redirect('main_game')
    else:
        return redirect('login')

#Game views
## Headquarters
class Game(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game.html"

##Campamento
class GameCampView(LoginRequiredMixin, ListView):
    model = Aldea
    fields = "__all__"
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game_camp.html"

    def get_queryset(self):
        self.aldea = Aldea.objects.filter(jugador=Jugador.objects.filter(user=self.request.user.username)[0])
        return self.aldea

class GameSeeCamp(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game_see_camp.html"
    success_url = "/game"

    def get_queryset(self):
        self.aldea = Aldea.objects.filter(id=self.kwargs['pk'])
        return self.aldea

## Mapa
class GameMapView(LoginRequiredMixin, ListView):
    model = Mapa
    fields = "__all__"
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game_map.html"

    def get_queryset(self):
        return Mapa.objects.filter(name="Patagonia")

## Centro de correos
class GameSeeMessage(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game_see_message.html"
    success_url = "/game"

    def get_queryset(self):
        self.mensaje = Mensaje.objects.filter(id=self.kwargs['pk'])
        return self.mensaje

class GameDeleteMessage(LoginRequiredMixin, DeleteView):
    model = Mensaje
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game_delete_message.html"
    fields = "__all__"
    success_url = "/game"

class GameViewMessage(LoginRequiredMixin, ListView):
    model = Mensaje
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game_messages.html"
    fields = "__all__"
    success_url = "/game"

    def get_queryset(self):
        return Mensaje.objects.filter(receptor=Jugador.objects.filter(user=self.request.user.username)[0])


class GameSendMessage(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'main_game'
    template_name = "web/game_send_message.html"
    success_url = "/game"
    model = Mensaje
    fields = ['titulo', 'mensaje', 'receptor']

    def form_valid(self, form):
        form.instance.emisor = Jugador.objects.filter(user=self.request.user).first()
        return super().form_valid(form)


# Signup
class ExtendedForm(ModelForm):
    class Meta:
        model = Jugador
        # temporary exclude user field to pass the validation
        fields = "__all__"
        exclude = ('user',)
            

def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        extra_form = ExtendedForm(request.POST)

        if form.is_valid() and extra_form.is_valid():
            # create a new user first
            new_user = form.save()
             # create an object in memory but not save it
            new_extended_obj = extra_form.save(commit=False)
            # assign the user to the extended obj
            new_extended_obj.user = new_user.username
            # write to database
            new_extended_obj.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
        extra_form = ExtendedForm()
    return render(request, 'web/signup.html', {'form': form,'extra_form': extra_form})


##Debug Only
### Para popular la db
def Start(request):
    Civilizacion.objects.create(nombre="Argentinos")
    Civilizacion.objects.create(nombre="Indigenas")

    map = Mapa(name="Patagonia",width=4,height=4,mapSize=16)
    map.save()
    for Y in range(0, 4):
        for X in range(0, 4):
            Celda.objects.create(ocupada=False,x=X,y=Y,mapa=map)
    
    map.celdas.all()
    print("Todo se ha creado, celdas totales del mapa: " + map.celdas.count())
    return redirect('login')

