from django.shortcuts import render
from tienda.models import Salesorderheader
from datetime import datetime
import zoneinfo
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required


def traer_fecha_valida(fecha, conzonahoraria=False):
    if fecha is None:
        return None

    partes = fecha.split("-")
    if len(partes) != 3:
        return None

    try:
        year = int(partes[0])
        month = int(partes[1])
        day = int(partes[2])
        ff = datetime(year, month, day)
    except Exception:
        return None

    if conzonahoraria:
        return ff.astimezone(zoneinfo.ZoneInfo("America/Santiago"))
    return ff


@login_required(login_url="/iniciar-sesion")
@permission_required("tienda.view_salesorderheader", login_url="/iniciar-sesion")
def v_list(request):
    orderCode = request.GET.get("orderCode", "")
    city = request.GET.get("city", "")
    postalCode = request.GET.get("postalCode", "")
    shipDate = request.GET.get("shipDate", "")

    consulta = Salesorderheader.objects.all().order_by('salesorderid')

    if len(orderCode) > 0:
        consulta = consulta.filter(salesorderid=orderCode)
    if len(city) > 0:
        consulta = consulta.filter(shiptoaddressid__city__icontains=city)
    if len(postalCode) > 0:
        consulta = consulta.filter(shiptoaddressid__postalcode=postalCode)
    if len(shipDate) > 0:
        shipDate = traer_fecha_valida(shipDate, conzonahoraria=True)
        consulta = consulta.filter(shipdate__gte=shipDate)
        shipDate = shipDate.strftime("%Y-%m-%d")

    paginator = Paginator(consulta, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    active_filter = request.GET.copy()
    if active_filter.get("page"):
        active_filter.pop("page")

    context = {
        "salesorder": page_obj,
        "orderCode": orderCode,
        "city": city,
        "postalCode": postalCode,
        "shipDate": shipDate,
        "active_filter": active_filter,
    }
    return render(request, "list.html", context)


def v_login(request):
    from .forms import LoginForm
    from django.contrib.auth import authenticate, login

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    else:
        context = {"form": LoginForm(request.POST)}
        return render(request, "login.html", context)


def v_logout(request):
    from django.contrib.auth import logout

    if request.user.is_authenticated:
        logout(request)

    return HttpResponseRedirect("/")
