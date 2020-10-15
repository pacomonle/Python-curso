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
    html = """
        <h1>Inicio</h1>
        <h3><strong>Te encuentras en la Home Page</strong></h3>
        <p>Años hasta el 2030 : </p>
        <ul>
    """
    year= 2021
    suma= 0
    while year < 2031:
        if year%2 == 0:
            html += "<li> Año Par -> " 
            pass
        else:
            html += "<li> Año Impar -> " 
            pass
        html += f" {str(year)}</li>"
        year += 1
        suma += 1
        pass
    else:
        html += f"""
        <ul>
        <hr>
        <p>FIN DEL LISTADO, {str(suma)} total años</p>
        """
        pass
    return HttpResponse(layout + html)
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
        return HttpResponse(layout + """
        <h1>Hola desde Django</h1>
        <h3>FRancisco MOnleon</h3>
        """)
        pass
    pass
# (req, nombre= 'python', secciones= 20)
def pagina(req, nombre='', secciones=''):
    """
    page 
    """
    html= '<h2>PARAMETROS: </h2><br>'
    if nombre and secciones:
        html  += f"""<strong>Parametro 1º por la url str : {nombre.upper()}</strong>
        <br/>
        <strong>Parametro 2ª por la url str : {secciones.upper()}</strong>"""
        pass
    else:
        html  += f"<strong>No has enviado ninguno parametro por la url</strong>"
        pass
    return HttpResponse(layout + """
        <h1>Nueva Pagina web</h1>
        <h3>Django framework Python</h3>
        <br/>
    """+ html)
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
