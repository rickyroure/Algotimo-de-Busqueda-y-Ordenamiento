from Funciones import generate_random_list
from Funciones import busqueda_lineal
from Funciones import busqueda_binaria
from Funciones import bubble_sort
from Funciones import insertion_sort
from Funciones import selection_sort
from Funciones import quicksort
import timeit


menu_principal=True
submenu2=False

base_datos_grande=(generate_random_list(14530))

base_datos_chica=(generate_random_list(100))            
while True:
    
    if menu_principal:
        n=int(input('Por favor elija la opcion de busqueda:\n' '1 Busqueda lineal\n' '2 Busqueda binaria\n' '3 Salir\n''Opción: '))
        tipo_de_busqueda={
            1:'Busqueda lineal',
            2:'Busqueda binaria',
            3:'Salir'
            }
        if n in tipo_de_busqueda:
            print(f'Elijió la opción de "{tipo_de_busqueda[n]}"')
        else:
            print ('Opción invalida elija una opción entre el 1 y el 3')
            continue    
     

        if n==1:
            base_datos=int(input('Ingrese la base de datos con la que quiere trabajar\n' '1 Base de datos chica \n' '2 Base de datos grande \n' '3 Volver al menú principal\n'))
            opcion_de_busqueda={
                1:'Base de datos chica',
                2:'Base de datos grande',
                3:'Menu principal'
                }
            if base_datos==1:
                base_datos=base_datos_chica                              
                print (f'Se trabaja con la siguiente base de datos \n {base_datos}')    
                num=int(input('Ingrese el valor que desea buscar: '))
                print (f'El número que busca se encuentra en la posición {busqueda_lineal(base_datos,num)+1}')
                inicio= timeit.default_timer()
                resultado_busqueda=busqueda_lineal(base_datos,num)
                fin = timeit.default_timer()
                print("Tiempo de busqueda en linea:", fin - inicio)

            elif base_datos==2:
                base_datos=base_datos_grande
                print (f'Elijió trabajar con la base de datos grande')
                mostrar_lista=input('¿Quiere ver la lista ordenada? (S/N)').upper()
                if mostrar_lista=="S":
                    print(f"Lista ordenada:{base_datos}")
                else:
                    print("La lista ordenada no se muestra")
                print (f'Intentaremos buscar el valor ubicado en la posicion 7649 que es el N° {base_datos[7649]}')   
                num=base_datos_grande[7649]
                print(f'Buscaremos el valor {base_datos_grande[7649]}')

                
                inicio= timeit.default_timer()
                resultado_busqueda=busqueda_lineal(base_datos,num)
                fin = timeit.default_timer()
                print (f'El número que busca se encuentra en la posición {resultado_busqueda}')
                print("Tiempo de busqueda en linea:", fin - inicio)
            elif base_datos==3:
                continue
            else:
                print('Opcion Incorrecta, regresando al menu principal')    
        elif n==2:
           
            menu_principal=False    
            submenu =True

        elif n==3:
                break
                   
        else:
            print('Ingrese una opciòn correcta')        
            
                
    elif  submenu:     
        ordenar={
            1:'Ordenamiento burbuja',
            2:'Inserción',
            3:'Seleccion',
            4:'Quicksort',
            5:'Regresar al menú principal'
            }
        print('Antes de buscar el elemento debemos ordenar cada uno de ellos elija el metodo de ordenamiento')
        orden=int(input(f'1.Ordenamiento burbuja:\n''2.Inserción:\n' '3.Selección:\n' '4.Quicksort:\n' '5.Regresar al menú principal\n''Opcion: '))
        base_datos=list(base_datos_grande)

        if orden==1:
            
            #vamos a medir el tiempo que tarda en ordenar la lista
            start_time = timeit.default_timer()
            lista_ordenada=bubble_sort(base_datos)
            end_time = timeit.default_timer()
            
            print("Tiempo para ordenamiento del tipo burbuja", end_time - start_time, 'segundos') 

            mostrar_lista=input('¿Quiere ver la lista ordenada? (S/N)').upper()
            if mostrar_lista=="S":
                print(f"Lista ordenada:{lista_ordenada}")
            else:
                print("La lista ordenada no se muestra")

            #Ingresamos el valor que buscaremos en la lista. 
            print (f'Intentaremos buscar el valor ubicado en la posicion 7649 que es el N° {base_datos[7649]}')
            num=int(input('Ingrese el valor que desea buscar\n'))
            valor=busqueda_binaria(base_datos,num)
            print(f'El número que busca se encuentra en la posición {valor}')
            #tiempo que tarda en buscar el elemento
            inicio= timeit.default_timer()
            resultado_busqueda=busqueda_binaria(base_datos,num)
            fin = timeit.default_timer()
            print("Tiempo de busqueda de forma binaria:", fin - inicio)
        
        elif orden==2:
            start_time = timeit.default_timer()
            lista_ordenada=insertion_sort(base_datos)
            end_time = timeit.default_timer()
            # Mostramos la lista ya ordenada tipo Insercion
            mostrar_lista=input('¿Quiere ver la lista ordenada? (S/N)').upper()
            if mostrar_lista=="S":
                print(f"Lista ordenada:{lista_ordenada}")
            else:
                print("La lista ordenada no se muestra")

            #print(base_datos)
            print("Tiempo para ordenar con inserción:", end_time - start_time, "segundos")
            # Ingreso del número a buscar
            print (f'Intentaremos buscar el valor ubicado en la posicion 7649 que es el N° {base_datos[7649]}')
            num = int(input('Ingrese el valor que desea buscar: '))
            # Ejecutamos búsqueda binaria
            valor = busqueda_binaria(base_datos, num)
            print(f'El número que busca se encuentra en la posición {valor}')
            # Medimos el tiempo de búsqueda binaria
            inicio = timeit.default_timer()
            resultado_busqueda = busqueda_binaria(base_datos, num)
            fin = timeit.default_timer()
            print("Tiempo de búsqueda de forma binaria:", fin - inicio)
        
        elif orden==3:
            start_time = timeit.default_timer()
            lista_ordenada=selection_sort(base_datos)
            end_time = timeit.default_timer()
            # Mostramos la lista ya ordenada
            mostrar_lista=input('¿Quiere ver la lista ordenada? (S/N)').upper()
            if mostrar_lista=="S":
                print(f"Lista ordenada:{lista_ordenada}")
            else:
                print("La lista ordenada no se muestra")
            
            print("Tiempo para ordenar con selección:", end_time - start_time)
            # Ingreso del número a buscar
            print (f'Intentaremos buscar el valor ubicado en la posicion 7649 que es el N° {base_datos[7649]}')
            num = int(input('Ingrese el valor que desea buscar: '))
            # Ejecutamos búsqueda binaria
            valor = busqueda_binaria(base_datos, num)
            print(f'El número que busca se encuentra en la posición {valor}')
            # Medimos el tiempo de búsqueda binaria
            inicio = timeit.default_timer()
            resultado_busqueda = busqueda_binaria(base_datos, num)
            fin = timeit.default_timer()
            print("Tiempo de búsqueda de forma binaria:", fin - inicio) 
        
        elif orden==4:
            start_time = timeit.default_timer()
            lista_ordenada=quicksort(base_datos)
            end_time = timeit.default_timer()
             # Mostramos la lista ya ordenada
            mostrar_lista=input('¿Quiere ver la lista ordenada? (S/N)').upper()
            if mostrar_lista=="S":
                print(f"Lista ordenada:{lista_ordenada}")
            else:
                print("La lista ordenada no se muestra")
            print("Tiempo para ordenar con Quicksorce:", end_time - start_time)
            # Ingreso del número a buscar
            print (f'Intentaremos buscar el valor ubicado en la posicion 7649 que es el N° {lista_ordenada[7649]}')
            num = int(input('Ingrese el valor que desea buscar: '))
            # Ejecutamos búsqueda binaria
            valor = busqueda_binaria(lista_ordenada, num)
            print(f'El número que busca se encuentra en la posición {valor}')
            # Medimos el tiempo de búsqueda binaria
            
            inicio = timeit.default_timer()
            resultado_busqueda = busqueda_binaria(lista_ordenada, num)
            fin = timeit.default_timer()
            print("Tiempo de búsqueda de forma binaria:", fin - inicio)
        
        elif orden==5:
            menu_principal=True
            submenu=False
        else:
            print('Ingrese una opcion correcta')