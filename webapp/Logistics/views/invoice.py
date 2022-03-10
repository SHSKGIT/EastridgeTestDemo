from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.views import generic
from django.views import View

from ..models.invoice import Invoice, InvoiceItem
from ..forms.invoice import InvoiceForm, InvoiceItemForm

from datetime import datetime


#=======================================================================================================================
class HomeView(View):

    def get(self, request):
        template = 'Logistics/home.html'
        return render(request, template)


#=======================================================================================================================
class InvoiceDisplayView(View):

    def get(self, request):
        data_list = Invoice.objects.all().order_by('id')
        template = 'Logistics/invoice_display.html'
        return render(request, template, context={'data_list': data_list})


#=======================================================================================================================
class InvoiceItemDisplayView(View):

    def get(self, request):
        data_list = InvoiceItem.objects.select_related('invoice').values(
            'units', 'description', 'amount', 'invoice__date').order_by('id')
        template = 'Logistics/invoice_item_display.html'
        return render(request, template, context={'data_list': data_list})


#=======================================================================================================================
class InvoiceFormView(generic.edit.CreateView):

    model = Invoice
    fields = ['date']

    def get(self, request):
        form = InvoiceForm()
        form.fields['date'].widget = DatePickerInput()
        template = 'Logistics/invoice.html'
        return render(request, template, context={'form': form})

    def post(self, request):
        form = InvoiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            form.save()
            return redirect("Logistics:invoice_form")
        else:
            template = 'Logistics/error.html'
            msg = 'The date already exists. Please pick another date.'
            return render(request, template, context={'error_msg': msg})


#=======================================================================================================================
class InvoiceItemFormView(generic.edit.CreateView):

    model = InvoiceItem
    fields = ['units', 'description', 'amount', 'invoice']

    def get(self, request):
        form = InvoiceItemForm()
        template = 'Logistics/invoice_item.html'
        return render(request, template, context={'form': form})

    def post(self, request):
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            form.save()
            return redirect("Logistics:invoiceitem_form")
        else:
            template = 'Logistics/error.html'
            msg = 'Invalid data.'
            return render(request, template, context={'error_msg': msg})


#=======================================================================================================================
def _flt(v, dflt=0.0):
    try:
        return float(v)
    except:
        return dflt


def _int(v, dflt=0):
    try:
        return int(v)
    except:
        return dflt