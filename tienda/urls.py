from django.urls import path
from .views import v_list, v_login, v_logout

urlpatterns = [
    path('', v_list),
    path('cerrar-sesion', v_logout),
    path('iniciar-sesion', v_login),
]