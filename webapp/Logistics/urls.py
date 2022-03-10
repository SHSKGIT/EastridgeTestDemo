from django.urls import path
from .views import invoice

app_name = 'Logistics'

urlpatterns = [
    path("home/", invoice.HomeView.as_view(), name="home"),
    path("invoice_display/", invoice.InvoiceDisplayView.as_view(), name="invoice_display"),
    path("invoiceitem_display/", invoice.InvoiceItemDisplayView.as_view(), name="invoiceitem_display"),
    path("invoice_form/", invoice.InvoiceFormView.as_view(), name="invoice_form"),
    path("invoiceitem_form/", invoice.InvoiceItemFormView.as_view(), name="invoiceitem_form"),
]