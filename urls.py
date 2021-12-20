from django.urls import path

from . import views

app_name = "whitebox"

urlpatterns = [
    # ex: /whitebox/
    path('', views.index, name='index'),
    # ex: /whitebox/GenerateForm
    path('GenerateForm', views.GenerateForm, name='GenerateForm'),
    path('generate', views.generate, name='generate'),
    # ex: /whitebox/RegisterForm
    path('RegisterForm', views.RegisterForm, name='RegisterForm'),
    path('register', views.register, name='register'),
    # ex: /whitebox/LoginForm
    path('LoginForm', views.LoginForm, name='LoginForm'),
    path('signin', views.signin, name='signin'),
    # ex: /whitebox/LogoutPage
    path('LogoutPage', views.LogoutPage, name='LogoutPage'),
    # ex: /whitebox/ViewAll
    path('ViewAll', views.ViewAll, name='ViewAll'),
    # ex: /whitebox/ViewMine
    path('ViewMine', views.ViewMine, name='ViewMine'),
    # ex: /whitebox/5/ViewDetail
    path('<int:character_id>/ViewDetail', views.ViewDetail, name='ViewDetail'),
    # ex: /whitebox/5/FinalizeForm
    path('<int:character_id>/FinalizeForm', views.FinalizeForm, name='FinalizeForm'),
    # ex: /whitebox/5/finalize
    path('<int:character_id>/finalize', views.finalize, name='finalize'),
    # ex: /whitebox/5/delete
    path('<int:character_id>/delete', views.delete, name='delete'),
    # REST views
    path('character_generate/<str:name>/', views.character_generate),
    path('character_list', views.character_list),
    path('characters/<int:pk>/', views.character_detail),
    path('vue_test', views.vue_test)
]