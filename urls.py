from django.urls import path

from . import views

app_name = "whitebox"

urlpatterns = [
    #AUTH stuff
    path('get_username', views.get_username),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('LogoutPage', views.LogoutPage, name='LogoutPage'),
    
    #CharacterList and Character stuff
    path('character_generate/<str:name>/', views.character_generate),
    path('CharacterList', views.CharacterListView.as_view()),
    path('MyCharacterList', views.MyCharacterListView.as_view()),
    #supports GET, DELETE, and PUT
    path('characters/<int:pk>/', views.character_detail),
    
    #MeleeWeaponList and MeleeWeapon stuff
    path('MeleeWeaponList', views.MeleeWeaponListView.as_view()),
    #POST used for buying
    path('MeleeWeaponTransaction', views.MeleeWeaponTransaction),
    
    #MeleeWeapon stuff
    
    #single page application URLs
    path('vue_test', views.vue_test),
    path('', views.vue_test)
]
