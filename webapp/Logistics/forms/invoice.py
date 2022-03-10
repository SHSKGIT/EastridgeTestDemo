from django import forms

from bootstrap_datepicker_plus.widgets import DatePickerInput

from ..models.invoice import Invoice, InvoiceItem


#=======================================================================================================================
class InvoiceForm(forms.ModelForm):

    class Meta:

        model = Invoice
        fields = ['date']
        widgets = {
            'date': DatePickerInput(),
        }

    def __init__(self, *args, **kwargs):

        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['date'].required = True


#=======================================================================================================================
class JerryModelChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):

        return obj.date


#=======================================================================================================================
class InvoiceItemForm(forms.ModelForm):

    invoice = JerryModelChoiceField(
        Invoice.objects.all(),
    )

    # invoice = forms.ModelChoiceField(
    #     queryset=Invoice.objects.values_list('date', flat=True).order_by('-date'),
    #     to_field_name='date',
    #     initial=Invoice.objects.all().order_by('-date')[0],
    #     empty_label=None,
    # )

    class Meta:

        model = InvoiceItem
        fields = '__all__'
        # exclude = ('invoice',)
