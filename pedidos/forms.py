from django import forms
from .models import Pedido, Plato

class PedidoForm(forms.ModelForm):
    platos = forms.ModelMultipleChoiceField(
        queryset=Plato.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Platos del pedido"
    )
    

    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'direccion', 'platos']

