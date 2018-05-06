from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views, login ## Login auth_view
from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'), # Index
    url(r'^login/$', auth_views.login, {'template_name': 'web/login.html'}, name='login'), # login
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'), #Logout
    url(r'^register/$',views.SignUp, name='register'), #Logout

    ##Game

    url(r'^game/$',views.Game.as_view(), name='main_game'),
    ###Mapa
    url(r'^game/map/$', views.GameMapView.as_view(), name='main_game_map'),
    
    ###Correo
    url(r'^game/send_message/$', views.GameSendMessage.as_view(), name='main_game_send_message'),
    url(r'^game/message/$', views.GameViewMessage.as_view(), name='main_game_message'),
    url(r'^game/delete_message/(?P<pk>\d+)$', views.GameDeleteMessage.as_view(), name='main_game_delete_message'),
    url(r'^game/see_message/(?P<pk>\d+)$', views.GameSeeMessage.as_view(), name='main_game_see_message'),

    ###Campamento
    url(r'^game/camp/$', views.GameCampView.as_view(), name='main_game_camp'),
    url(r'^game/see_camp/(?P<pk>\d+)$', views.GameSeeCamp.as_view(), name='main_game_see_camp'),

    ##Debug Only
    url(r'^start/$', views.Start, name='start'),
]