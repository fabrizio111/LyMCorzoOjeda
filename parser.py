# Este es el alfabeto que contiene los elementos terminales del lenguaje
alfabeto = ["var", "PROC", "drop", "free", "walk","canWalk", "fi", "go", "GORP","do", "walk", "od", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else", "around"]
#El conjunto de elementos no terminales del lenguaje
metodos=["drop", "walk", "walk_d","walk_o","jump", "jumpTo", "veer", "look", "grab", "get", "free", "pop", "PROC", "do", "go",  "if_condicional", "loop", "repeat"]
condiciones =["isfacing", "isValid", "canWalk", "not"]
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
metodosnoconocidos=[]
variables=[]
parametros=[]
walkc=["north", "south", "east", "west","right", "left", "front", "back"]
puntos_cardinales=["north", "south", "east", "west"]
direccion=["right", "left", "front", "back"]
veer_to=["right", "left","around"]
objetos=['balloons','chips']




#Método para identificar una palabra del lenguaje y llamar a la funcion de verificacion.

def call_method(name,number):
    number2=0
    if name == "drop":
        number2=drop(number)
    elif name == "=":
        number2=assignment(number)
    elif name == 'walk':
        number2=walk(number)
    elif name == "walkm":
        number2=walk_d(number)    
    elif name == "jump":
        number2=jump(number)
    elif name == 'jumpTo':
        number2 == jumpTo(number)
    elif name == "veer":
        number2=veer(number)
    elif name == "look":
        number2=look(number)
    elif name == "grab":
        number2=grab(number)
    elif name == "get":
        number2=get(number)
    elif name == "free":
        number2=free(number)      
    elif name == "pop":
        number2=(number)
    elif name == "isfacing":
        number=isfacing(number)
    elif name == "isValid":
        number2=isValid(number)
    elif name == "canWalk":
        number2=canwalkmultiple(number)
    elif name == "not":
        number2=c_not(number)
    elif name ==' if_condicional':
        number2=if_condicional(number)
    elif name == "loop":
        number2=loop(number)
    elif name == "repeat":
        number2=repeat(number)
    else:
        number2 = 0
    return number2

#Funcion para saber cual condicional se va a usar y verificar si está sintacticamente correcto.
def compararcondicionales(name,number):
    number2=0
    if  name == "isfacing":
        number2=isfacing(number)
    elif name == "isValid":
        number2=isValid(number)
    elif name == "canWalk":
        number2=canwalkmultiple(number)
    elif name == "not":
        number2=c_not(number)
    else:
        number2 = 0 

    return number2

#COMANDOS

#'='
def assignment(name,number):
        result=0
        verificar=[]
        forma=[]
        resto=len(name)-(number+1)

        if resto>=3:
                
                verificar.append('=')
                contador = 1  
                

                while contador <= 4:

                   sub_number=number + contador
                   posicion=name[sub_number]
                   verificar.append(posicion)
                   contador += 1

                var_name=verificar[1]
                forma.append('=',var_name,numeros, ')')

                if len(verificar) == 4:
                        if verificar[-1] == forma[-1]:
                          encontrado = False
                          numero = 0 
                          while encontrado == False and numero <= len(numeros): 

                               if numeros[numero] in verificar[2]:
                                 encontrado = True
                                 result = 1
                               numero += 1
                           

        return result


#walk

def walk(name, number):

    result= 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 2:
        
        verificar.append('walk')
        forma.append('walk', numeros, ')')
        contador=1
        while contador <= 3:

            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 3:
            if verificar[-1] == forma[-1]:
                encontrado_numero= False
                encontrado_letra=False
                numero = 0
                letra = 0
                while encontrado_numero == False and numero <= len(numeros): 

                    if numeros[numero] in verificar[1]:
                        encontrado_numero = True
                        result = 1
                    numero += 1
                        
                while encontrado_letra == False and letra <= len(letras): 

                    if letras[letra] in verificar[1]:
                        encontrado_letra = True
                        result = 1
                    letra += 1 
                        

    return result

#walk_d
def walk_d(name, number):

    result = 0
    verificar = []
    forma = ['walk_d', numeros, ':', direccion, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('walk_d')
        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador +=1

        if len(verificar) == 5:
            if verificar[2] == forma[2]:
                if verificar[-1] == forma[-1]:
                     encontrado= False
                     numero = 0
                   
                     while encontrado == False and numero <= len(numeros): 

                      if numeros[numero] in verificar[1]:
                        elemento = 0
                        while encontrado == False and elemento <= len(direccion): 
                                if verificar[3] == direccion[elemento]:
                                    result = 1
                                    encontrado = True 
                                elemento +=1
                      numero += 1
            

    return result

#walk_o
def walk_o(name, number):

    result = 0
    verificar = []
    forma = ['walk_o', numeros, ':', direccion, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('walk_o')
        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador +=1

        if len(verificar) == 5:
            if verificar[2] == forma[2]:
                if verificar[-1] == forma[-1]:
                     encontrado= False
                     numero = 0
                   
                     while encontrado == False and numero <= len(numeros): 

                      if numeros[numero] in verificar[1]:
                        elemento = 0
                        while encontrado == False and elemento <= len(direccion): 
                                if verificar[3] == direccion[elemento]:
                                    result = 1
                                    encontrado = True 
                                elemento +=1
                      numero += 1
            

    return result

#jump
def jump(name, number):

    result= 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 2:
        
        verificar.append('jump')
        forma.append('jump', numeros, ')')
        contador=1
        while contador <= 3:

            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 3:
            if verificar[-1] == forma[-1]:
                encontrado_numero= False
                encontrado_letra=False
                numero = 0
                letra = 0
                while encontrado_numero == False and numero <= len(numeros): 

                    if numeros[numero] in verificar[1]:
                        encontrado_numero = True
                        result = 1
                    numero += 1
                        
                while encontrado_letra == False and letra <= len(letras): 

                    if letras[letra] in verificar[1]:
                        encontrado_letra = True
                        result = 1
                    letra += 1 
                        

    return result

#jumpTo
def jumpTo(name, number):

    result = 0
    verificar = []
    forma = ['jumpTo', numeros, ':', metodos, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('jumpTo')
        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador +=1

        if len(verificar) == 5:
            if verificar[2] == forma[2]:
                if verificar[-1] == forma[-1]:
                     encontrado= False
                
                     elemento = 0
                     while encontrado == False and elemento <= len(metodos): 
                                if verificar[3] == metodos[elemento]:
                                    result = 1
                                    encontrado = True 
                                elemento +=1
                  
            

    return result
#veer
def veer(name, number):

    result = 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 3:

        verificar.append('veer')
        forma.append('veer',':',veer_to, ')')
        contador=1
        while contador <= 4:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador +=1

        if len(verificar) == 4:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    encontrado_veer= False
                    veer= 0
                    while encontrado_veer == False and veer <= len(veer_to): 

                        if veer_to[veer] in verificar[2]:
                            encontrado_veer = True
                            result = 1
                        veer += 1

    return result

#look
def look(name, number):

    result = 0
    verificar = []
    forma = []
    resto = len(name) - (number + 1)

    if resto >= 3:

        verificar.append('look')
        forma.append('look', ':', puntos_cardinales, ')')
        contador=1
        while contador <= 4:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 4:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    encontrado_look= False
                    look= 0
                    while encontrado_look == False and look <= len(puntos_cardinales): 

                        if puntos_cardinales[look] in verificar[2]:
                            encontrado_look = True
                            result = 1
                        look += 1

    return result

#Grab
def grab(name, number):

    result = 0
    verificar = []
    forma = ['grab', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('grab')
        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 5:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                  if 'balloons' in verificar[2]:
                    encontrado  = False 
                    elemento = 0  
                    letra = 0
                    while encontrado == False and elemento <= len(objetos):

                        if verificar[2] == objetos[elemento]:
                            letra = 0
                            while encontrado == False and letra <= len(letras):

                                if letras[letra] in verificar[3]:
                                    result = 1
                                    encontrado == True
                                letra += 1
                        elemento += 1

    return result


#get
def get(name, number):

    result = 0
    verificar = []
    forma = ['get', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('get')
        contador=1
        while contador <= 4:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 4:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                  if 'chips' in verificar[2]:
                    encontrado  = False 
                    elemento = 0  
                    letra = 0
                    while encontrado == False and elemento <= len(objetos):

                        if verificar[2] == objetos[elemento]:
                            letra = 0
                            while encontrado == False and letra <= len(letras):

                                if letras[letra] in verificar[3]:
                                    result = 1
                                    encontrado == True
                                letra += 1
                        elemento += 1

    return result


#drop
def drop(name, number):

    result = 0
    verificar = []
    forma = ['drop', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('drop')

        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 5:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    if 'chips' in verificar[2]:
                        letra= 0
                        while encontrado_letra == False and letra <= len(letras): 

                         if letras[letra] in verificar[3]:
                           encontrado_letra = True
                           result = 1
                           letra += 1

    return result

#free
def free(name, number):

    result = 0
    verificar = []
    forma = ['free', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('free')

        contador=1
        while contador <= 5:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 5:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                    if 'balloons' in verificar[2]:
                        letra= 0
                        while encontrado_letra == False and letra <= len(letras): 

                         if letras[letra] in verificar[3]:
                           encontrado_letra = True
                           result = 1
                           letra += 1

    return result
#pop

def pop(name, number):

    result = 0
    verificar = []
    forma = ['pop', ':', objetos, letras, ')']
    resto = len(name) - (number + 1)

    if resto >= 4:
        verificar.append('pop')
        contador=1
        while contador <= 4:
            sub_number = number + contador
            posicion = name[sub_number]
            verificar.append(posicion)
            contador += 1

        if len(verificar) == 4:
            if verificar[1] == forma[1]:
                if verificar[-1] == forma[-1]:
                  if 'balloons' in verificar[2]:
                    encontrado  = False 
                    elemento = 0  
                    letra = 0
                    while encontrado == False and elemento <= len(objetos):

                        if verificar[2] == objetos[elemento]:
                            letra = 0
                            while encontrado == False and letra <= len(letras):

                                if letras[letra] in verificar[3]:
                                    result = 1
                                    encontrado == True
                                letra += 1
                        elemento += 1

    return result

#Condicionales
def isfacing(name,number):
  forma = False
  palabra =""
  number2 = number+1
  if name[number+1]=="(":
    while number2 <= number2+5 :
      for punto_cardinal in puntos_cardinales:
        palabra+=name[number2]
        if palabra == punto_cardinal:
          longitudactual = number[number2+len(palabra)]
          if name[len(longitudactual)+1]==")":
            forma = True
      number2+=1
  longitud = len(longitudactual+1)
  retorno =(longitud,forma)
  return retorno

def isValid(name, number):

  forma = False
  palabra =""
  number2 = number+1
  if name[number+1]=="(":
    while number2 <= number2+5 :
      for metodo in metodos:
        palabra+=name[number2]
        if palabra == metodo:
          longitudactual = number[number2+len(palabra)]
          if name[len(longitudactual)+1]==")":
            forma = True
      number2+=1
  longitud = len(longitudactual+1)
  retorno =(longitud,forma)
  return retorno

def canwalkmultiple(name, number):
  sintaxis = False
  palabra =""
  palabra2=""
  number2 = number+1
  if name[number+1]=="(":
    while number2 <= number2+5 :
      for indicewalk in walk:
        palabra+=name[number2]
        if palabra == indicewalk:
          longitudactual = name[number2+len(palabra)]
          if name[len(longitudactual)+1]==",":
            longitudactual3+=1
            while longitudactual3<=longitudactual+1:
              palabra2+=name[longitudactual]
              for indicevar in variables:
                for indicepar in parametros:
                  if palabra2 == indicepar or palabra2 == indicevar or palabra2.isdigit() == True:
                    longitudactual3 = name[longitudactual+len(palabra2)]
                    if name[len(longitudactual3)+1]==")":
                      sintaxis = True
              longitudactual3+=1          
      number2+=1
  longitud = len(longitudactual3+1)
  retorno =(longitud,sintaxis)
  return retorno

def c_not(name,number):
  if name[number+1] == "(":
    pass
  pass

def verificacion(verificar,lista):
    
    contador = 0
    while contador < len(verificar):
    
        if verificar[contador] == '=':
            retorno = assignment(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'walk':
            retorno = walk(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'jump':
            retorno = jump(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'jumpTo':
            retorno = jumpTo(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'veer':
            retorno = veer(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'look':
            retorno = look(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'drop':
            retorno = drop(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'grab':
            retorno = grab(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'get':
            retorno = get(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'free':
            retorno = free(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'pop':
            retorno = pop(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'walk_d':
            retorno = walk_d(verificar, contador)
            lista.append(retorno)
        elif verificar[contador] == 'walk_o':
            retorno = 'walk_o'(verificar, contador)
            lista.append(retorno)
     

        contador += 1
    return lista
    
#Estructuras de control
def if_condicional(name, number):

    result = 0
    verificar = ['if']
    lista = []
    contar = 0
    parentesis_izq = 1
    parentesis_der = 0
    sub_number = number

    while (parentesis_izq != parentesis_der):
        sub_number += 1
        if sub_number < len(name):
            ins = name[sub_number]
            verificar.append(ins)
            if ins == '(':
                parentesis_izq += 1
            elif ins == ')':
                parentesis_der += 1
        else:
            parentesis_der += 1
    lista_f=verificacion(verificar,lista)
    for element in lista_f:
        contar += element

    if contar == len(lista_f):
        result = 1

    return result

    
def loop(name, number):
    result = 0
    verificar = ['loop']
    lista = []
    cont = 0

    parentesis_izq = 1
    parentesis_der = 0
    sub_number = number

#Mientras los parentesis sean diferentes se va aumentando el indice(number)
    while (parentesis_izq != parentesis_der):
        sub_number += 1
        if sub_number < len(name):
            instruccion = name[sub_number]
            verificar.append(instruccion)
            if instruccion == '(':
                parentesis_izq += 1
            elif instruccion == ')':
                parentesis_der += 1
        else:
            parentesis_der += 1
    lista_f=verificacion(verificar,lista)
    for element in lista_f:
        cont += element

    if cont == len(lista_f):
        result = 1

    return result


def repeat(name, number):
    result = 0
    verificar = ['repeat']
    lista = []
    cont = 0

    parentesis_izq = 1
    parentesis_der = 0
    sub_number = number

#Mientras los parentesis sean diferentes se va aumentando el indice(number)
    while (parentesis_izq != parentesis_der):
        sub_number += 1
        if sub_number < len(name):
            instruccion = name[sub_number]
            verificar.append(instruccion)
            if instruccion == '(':
                parentesis_izq += 1
            elif instruccion == ')':
                parentesis_der += 1
        else:
            parentesis_der += 1
    lista_f=verificacion(verificar,lista)
    for element in lista_f:
        cont += element

    if cont == len(lista_f):
        result = 1

    return result


#Analizador
def Parser():
    ruta = input("\nIngrese la ruta del archivo: ")
    archivo = open(ruta, "r")
    retorno = True
    lineas = archivo.read().replace("\n", " ")
    archivo.close()
    lineas.strip()
    retorno = recorrer(lineas)
    if(retorno==True):
      print("\nEl programa está escrito sintácticamente correcto.\n")
    else:
      print("\nEl programa está escrito sintácticamente incorrecto.\n")
  

#Funcion para recorrer el archivo de texto y llamar a los metodos que verifican que la sintaxis esté correcta.
def recorrer(lineas):

  palabra = ""
  enum=0
  enum2=0
  retorno=True

  if lineas[0]=="P" and lineas[1]=="R" and lineas[2]=="O" and lineas[3]=="G":  
    if lineas[-1]=="P" and lineas[-2]=="R" and lineas[-3]=="O" and lineas[-4]=="G":
        retorno=True
    else:
        retorno=False
  else:
      retorno=False

  enum=4    
  while enum2< len(lineas)-5: 
    palabra+=lineas[enum2]
    if lineas[enum2+1]==",":
      variables.append(palabra)
      palabra=""
      enum2+=1
    elif lineas[enum2-1]=="," and lineas[enum2+1]==";":
      variables.append(palabra2)
      palabra2=""     
    enum2+=1  
    resto=enum2-enum
    enum+=resto
    enum+=1
  return retorno

#Donde empieza toda la magia
print("\n********Bienvenido*******")
Parser()
