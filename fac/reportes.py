from django.shortcuts import render
from .models import FacturaEnc, FacturaDet
from django.utils.dateparse import parse_date

from datetime import timedelta

def imprimir_factura_recibo(request,id):
    template_name="fac/factura_one.html"

    enc = FacturaEnc.objects.get(id=id)
    det = FacturaDet.objects.filter(factura=id)

    context={
        'request':request,
        'enc':enc,
        'detalle':det
    }

    return render(request,template_name,context)



def imprimir_factura_list(request, f1, f2):
    template_name = "fac/facturas_print_all.html"

    # Convertimos la fecha que viene como texto a tipo fecha
    f1 = parse_date(f1)
    f2 = parse_date(f2)
    f2 = f2 + timedelta(days=1)
    
    enc = FacturaEnc.objects.filter(fecha__gte=f1, fecha__lt=f2).order_by('id')
    f2 = f2 - timedelta(days=1)

    context = {
        'request': request,
        'f1': f1,
        'f2': f2,
        'enc': enc
    }

    return render(request, template_name, context)
