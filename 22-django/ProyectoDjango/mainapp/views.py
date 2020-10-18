from django.shortcuts import render

# Create your views here.
def index(req):
    """
   vista index
    """
    return render(req, 'mainapp/index.html',{
        'title': 'Inicio'
    })
    pass

def about(req):
    """
    vista about
    """
    return render(req, 'mainapp/about.html',{
        'title': 'Sobre Nosotros'
    })
    pass