from django import forms
from django.core import validators

"""
Formularios
basados en clases
"""

class FormArticle(forms.Form):
    """
    formulario pra articulos
    """
    title = forms.CharField(
        label = "Titulo",
        max_length= 40,
        # min_length= 5, 
        strip=True, 
        required = True,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Escribe el titulo...',
                'class': 'titulo_form_article'
            }
        ),
        
       validators = [
           validators.MinLengthValidator(5, 'Longitud minima del titulo 6 caracteres'),
           validators.RegexValidator('^[A-Z a-z 0-9]*$', 'Los caracteres especiales no son admitidos', 'invalid_title')
       ]
        
    )

    content = forms.CharField(
        label = "Contenido",
        required = True,
        widget = forms.Textarea,
        validators = [
            validators.MaxLengthValidator(100, 'Maximo 100 caracteres')
        ]
    )
    # actualizar atributos
    content.widget.attrs.update({'placeholder': 'Escribe el contenido...',  'class': 'contenido_form_article',})

    public_options = [
        # (value, label)
        ('none', '--- selecciona una opcion ---'),
        ('0', 'privado'),
        ('1', 'publlico')
    ]
    public = forms.TypedChoiceField(
       label = '¿Publicado?',
       choices = public_options
    )
    pass