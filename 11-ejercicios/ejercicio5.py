"""
ejercicio 5
- crear lista con el contenido de la tabla:
   -accion-   -aventura-      -deportes-
    GTA-IV     crash           fifa
     COD       assesin         moto gp
- mostrar informacion ordenada    
"""

videoJuegos = [
    {'categoria' : 'accion','juego' : ['GTA', 'COD']},
    {'categoria' : 'aventura', 'juego' : ['crash', 'assein']},
    {'categoria' : 'deportes', 'juego' : ['fifa', 'moto gp']},
]

for videoJuego in videoJuegos:
    print(f'### {videoJuego["categoria"]} ###')
    for juego in videoJuego["juego"]:
        print(f'{videoJuego["juego"].index(juego) + 1}. {juego}')
        pass
    pass
