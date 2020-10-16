from django.shortcuts import HttpResponse, redirect, render
"""
MVC - modelo vista controlador[Acciones(metodos)]
MVT - modelo template vista[Acciones(metodos)]
"""

# HttResponse -> para peticion http

# Create your views here.

layout = """
<h1> Web whith Django | Francisco Monleon </h1>
<hr/>
<ul>
    <li> 
        <a href='/inicio'>Inicio</a>
    </li>
    <li>
        <a href='/hola-django'>Django</a> 
    </li>
    <li>
         <a href='/page'>Pagina</a>
    </li>
     <li>
         <a href='/contact'>Contacto</a>
    </li>
</ul>
<hr/>
"""

def index(req):
    """
    inicio page
    """
    year= 2021
    suma= 0
    listaYear = []
    while year < 2031:
        listaYear.append(year)
        year+=1
        suma+=1
        pass
    else:
        sumaTotal = f'FIN DEL LISTADO, total años {suma}'
        pass
   
    curso = 'Aprendiendo Django'
    lenguajes = ['python', 'php','javascrip', 'c++']
    # return HttpResponse(layout + html)
    return render(req, 'index.html', {
        'title': 'index | miApp Django',
        'mi_variable': 'soy un dato de la vista',
        'curso': curso,
        'lenguajes':lenguajes,
        'sumaTotal': sumaTotal,
        'listaYear': listaYear
    })
    pass
def hola_mundo(req, redirigir = 0):
    """
    accion / metodo
    """
    
    if redirigir == 1:
       # return redirect('/page/python/django')
        return redirect('page', nombre='python', secciones='django')
        pass
    else:
        return render(req, 'hola_mundo.html')
        pass
    
   
    pass
# (req, nombre= 'python', secciones= 20)
def pagina(req, nombre='', secciones=''):
    """
    page 
    """
  
    """
    return HttpResponse(layout + "
        <h1>Nueva Pagina web</h1>
        <h3>Django framework Python</h3>
        <br/>
    "+ html)
    """
    return render(req, 'pagina.html',{
        'nombre': nombre.upper(),
        'secciones': secciones.upper()
    })
    pass
def contacto(req):
    """
    contact page
    """
    html = """
    <h3>Contacto formulario</h3>
    <form>
        <div>
            <label for="Name">Your name</label>
            <div>
                <input type="text" name="Name" required>
            </div>
        </div>
        <div>
            <label for="Email">Your email address</label>
            <div>
                <input type="email" name="Email" required>
            </div>
        </div>
        <div>
            <label for="Message">Your message</label>
            <div>
                <textarea name="Message" rows="6" maxlength="3000" required></textarea>
            </div>
        </div>
        <div>
            <button type="submit">Send Message</button>
        </div>
        <div>
        Simple HTML email form provided by: <a href="https://www.freecontactform.com" target="_blank">FreeContactForm.com</a>
        </div>
    </form>
    """
    return HttpResponse(layout + html)
    pass
