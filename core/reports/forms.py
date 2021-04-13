from django.forms import *
from core.erp.models import Category, Product, Client, Sale


class ReportForm(Form):

    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))
