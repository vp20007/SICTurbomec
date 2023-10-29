from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput
from django.utils.translation import gettext_lazy as _
from .models import *
from smart_selects.form_fields import ChainedModelChoiceField

class tipotransaccionForm(forms.ModelForm):
    class Meta:
        model = TipoTransaccion
        fields = '__all__'
        exclude = []
        widgets = {
            'id_tipoTransaccion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_tipoTransaccion': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class ClasecuentaForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'
        exclude = []
        widgets = {
            'id_clase': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_clase': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class GrupocuentaForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
        exclude = []
        widgets = {
            'id_grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'id_clase': forms.TextInput(attrs={'class': 'form-control'}),  
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = '__all__'
        exclude = []
        widgets = {
            'id_cuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_cuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'id_grupo': forms.TextInput(attrs={'class': 'form-control'}),  
        }

class SubcuentaForm(forms.ModelForm):
    class Meta:
        model = SubCuenta
        fields = '__all__'
        exclude = ['debe','haber']
        widgets = {
            'id_subCuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_subCuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'id_cuenta': forms.TextInput(attrs={'class': 'form-control'}),  
        }

class DateInput(forms.DateInput):
    input_type = 'date'


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__'
        exclude = ['id_partida', ]
        widgets = {
            'fecha_transaccionT': DateInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
        }


class TransaccionIVAForm(forms.Form):
    transaccion_iva = forms.ModelChoiceField(queryset=Transaccion.objects.filter(id_partida=1), label='Seleccione una transaccion', )


class CalculoIVAForm(forms.ModelForm):
    subCuenta_id = forms.ModelChoiceField(queryset=SubCuenta.objects.filter(id_subCuenta=1), label='Sub-Cuenta')

    class Meta:
        model = Transaccion
        fields = ['fecha_transaccionT', 'subCuenta_id', 'descripcion_transaccionT', 'id_tipoTransaccion', 'monto']
        widgets = {
            'fecha_transaccionT': DateInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
        }

class OrdendeProduccionForm(forms.ModelForm):
    class Meta:
        model = OrdendeProduccion
        fields = '__all__'
        exclude = ['id_OrdendeProduccion', ]
        widgets = {
            'fecha_Actual': DateInput(attrs={'class': 'form-control'}),
        }

class ManodeObraForm(forms.ModelForm):
    class Meta:
        model = ManodeObra
        fields = '__all__'
        exclude = ['id_OrdendeProduccion','costo']
        widgets = {
            'fecha_manodeObra': DateInput(attrs={'class': 'form-control'}),
        }
class ProrrateoForm(forms.ModelForm):
    class Meta:
        model = Prorrateo
        fields = '__all__'
        exclude = ['id_Prorrateo','totalCIF','tasapredeterminadaCIF','id_OrdendeProduccion' ]
        widgets = {
            'manodeObraIndirecta': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'segurosEquipo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'depreciacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'energia': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'amortizacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'otrosGastos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
        }

class costosIndirectosForm(forms.ModelForm):
    class Meta:
        model = CostosIndirectos
        fields = '__all__'
        exclude = ['id_costosIndirectos','id_Prorrateo','tasa','id_OrdendeProduccion','costoAplicado' ]
        widgets = {
            'pagoManodeObra': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'fecha_costosIndirectos': DateInput(attrs={'class': 'form-control'})
        }

class AjusteForm(forms.ModelForm):
    class Meta:
        model = Ajuste
        fields = '__all__'
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
        }
