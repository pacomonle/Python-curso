from django.shortcuts import HttpResponse, redirect, render
from miApp.models import Article, Category
# para hacer consultas OR
from django.db.models import Q
# import del formulario de django
from miApp.forms import FormArticle
# import mensajes flash
from django.contrib import messages

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
        return render(req, 'hola_mundo.html', {
            'texto': '',
            'lista': ['uno', 'dos', 'tres']
        })
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

def articulo(req):
    """
    sacar datos de articulo de la database
    """
    try:
        # get devuelve un registro, filtrar por pk, id, title ....
        articulo = Article.objects.get(pk=5, public= True)
        response = f'Articulo: {articulo.title}'
        pass
    except Exception as error:
        error = 'no existe ese articulo'
        response =f'{error}'
        pass
    
    
    return HttpResponse(response)
    pass

def editar_articulo(req, id):
    """
    Actualizar registro database
    """
    articulo = Article.objects.get(pk=id)
    articulo.title = 'Sexto articulo'
    articulo.content = 'Contenido 6º articulo'
    articulo.public = True

    articulo.save()
    return HttpResponse(f'ARticulo actualizado {articulo.id}: {articulo.title}')
    pass

def articulos(req):
    """
    listar articulos
    """
    # orden inverso -> ('-title') / todos los regostros .all() / intervalo [3:6] # [limit]
    articulos = Article.objects.order_by('id') # [limit]
    articulos_filter = Article.objects.filter(title__exact = 'Tercer articulo', content__contains='todo' ) # __lookups
    # lookups: -sin case sensitive __iexact, 
    #   id__gt= 12(greather than), __gte = 12 (greater than equal) 
    #   __lt (menor) __lte (menor o igual)   
    # 
    articulos_exclude = Article.objects.all().exclude(public = False)  
     # consultas SQL AND con Django
    articulos_SQL = Article.objects.raw('SELECT * FROM miApp_article WHERE title= " articulo" AND public = 0')
    # consultas OR con Django
    articulos_OR = Article.objects.filter(
        Q(title__contains = 'Tercer') | Q(id = 10)
    )
    return render(req, 'articulos.html', {
        'articulos': articulos,
        'articulos_SQL': articulos_SQL,
        'articulos_filtrados': articulos_filter,
        'articulos_exclude': articulos_exclude,
        'articulos_OR': articulos_OR
    })
    pass
   

def borrar_articulo(req, id):
    """
    eliminar articulo
    """
    articulo = Article.objects.get(pk = id)
    articulo.delete()
    return redirect('articulos')
    pass

def crear_articulo(req, title, content, public):
    """
   crear articulo en la data base
    """
    articulo = Article( 
        title = title,
        content = content,
        public = public
    )
         # para crear tambien hay otros metodos como el create()
    articulo.save()
    return HttpResponse(f'Articulo creado: <i>{articulo.title}</i> - <i>{articulo.content}</i>')
    # return HttpResponse('hola mundo')
    pass

def create_article(req):
    """
   crear articulo en la data base -
   usando FORMULARIOS
    """
    return render(req, 'create_article.html')
    pass

def save_article(req):
    """
   crear articulo en la data base
    """
    if req.method == 'POST':
        title = req.POST['title']
        # validaciones 
        if len(title) < 5:
            return HttpResponse('<h2>La longitud del titulo minimo 5 caracteres</h2>')
            pass
        content = req.POST['content']
        public = req.POST['public']

        articulo = Article( 
            title = title,
            content = content,
            public = public
        )
         # para crear tambien hay otros metodos como el create()
        articulo.save()
        return HttpResponse(f'Articulo creado: <i>{articulo.title}</i> - <i>{articulo.content}</i>')
        pass
    else:
        return HttpResponse('<h2>El articulo no se ha podido grabar correctamente</h2>')
        pass 
   
    pass

def create_full_article(req):
    """
    vista para crear articulos con el form de django
    - importar el form creado en miApp
    """
    if req.method == 'POST':
        formulario = FormArticle(req.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form['public']
            
            articulo = Article( 
            title = title,
            content = content,
            public = public
            )
         # para crear tambien hay otros metodos como el create()
            articulo.save()

            # crear mensaje flash (sesion se muestra 1 sola vez)
            messages.success(req, f'El articulo se guardo correctamente, su id es {articulo.id}')

            return redirect('articulos')
            pass
        # return HttpResponse(articulo.title + ' - ' + articulo.content + ' - '+ str(articulo.public))
        pass
    else:
        formulario = FormArticle()
        pass
    
    return render(req, 'create_full_article.html', {
        'form': formulario,
    })
    pass

