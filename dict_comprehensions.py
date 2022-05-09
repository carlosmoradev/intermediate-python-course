'''
Crear por medio de dictionary comprehensions un diccionario cuyas llaves sean 
los 100 primeros numeros naturales y cuyos valores sean esos numeros elevados
al cubo.
'''


def run():
#    cube_dict = {}
#
#    for i in range(1, 101):
#        if i % 3 != 0:
#            cube_dict[i] = i**3

    cube_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(cube_dict)

    
'''
    cube_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    ---\/---     --\/--  ---------\/----------  ------\/-----
  Nombre dict  llave:valor  ciclo simplificado  condicion opcional
'''



if __name__ == '__main__':
    run()