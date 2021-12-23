from django.urls import path

from . import views

app_name = "whitebox"

urlpatterns = [
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('LogoutPage', views.LogoutPage, name='LogoutPage'),
    path('character_generate/<str:name>/', views.character_generate),
    path('character_list', views.character_list),
    path('my_character_list', views.my_character_list),
    #supports GET, DELETE, and PUT
    path('characters/<int:pk>/', views.character_detail),
    path('get_username', views.get_username),
    path('vue_test', views.vue_test),
    path('', views.vue_test)
]