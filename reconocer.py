num1 = 42 #Variable numero entero
num2 = 2.3 #Variable numero flotante
boolean = True #Variable booleano
string = 'Hello World' #Variable string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Diccionario
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #Imprime en la consola los elementos de tuple
print(pizza_toppings[1]) #Imprime en la consola en indice 1 de las lista
pizza_toppings.append('Mushrooms') #Incluye Mushrooms como último elemento de la lista
print(person['name']) #Imprime en la consola el elemento Name del Diccionario
person['name'] = 'George' #Sustituye el valor de name 
person['eye_color'] = 'blue' #Incluye un nuevo valor al diccionario
print(fruit[2]) #Imprime en la consola el indice 2 de tuple

#Condicionales If, elseif, else
''' 
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
'''
#Loops for y while
'''
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
'''

pizza_toppings.pop() #Elimina el ultimo elemento de la lista
pizza_toppings.pop(1) #Elimina el elemento ubicado en el inice 1 de la lista

print(person) #Imprime en la consola el diccionario
person.pop('eye_color') #Elimina de diccionario el valor indicado
print(person) #Imprime en la consola el nuevo diccionario

for topping in pizza_toppings: #Loop for 
    if topping == 'Pepperoni': #si la variable es igual a pepperoni
        continue #el loop continua
    print('After 1st if statement') #imprime en la consola lo indicado
    if topping == 'Olives': #si la variable es igual a olives
        break #se detiene el Loop

def print_hello_ten_times(): #Se declara una funcion
    for num in range(10): #Loop for que inicia en 0 y llega hasta 10
        print('Hello') #Imprimir lo indicado en la consola tantas veces lo indique el Loop for

print_hello_ten_times() #Se llama a la funcion

def print_hello_x_times(x): #Se declara una funcion
    for num in range(x): #Loop for que inicia en 0 y llega hasta que se le indique el parametro
        print('Hello') #Imprimir lo indicado en la consola tantas veces lo indique el Loop for

print_hello_x_times(4) #Se llama a la funcion para que se imprima en la consola 4 veces lo indicado


def print_hello_x_or_ten_times(x = 10): #Se declara una funcion donde se indica el parametro
    for num in range(x): #Loop for que inicia en 0 y finaliza en 10

        print_hello_x_or_ten_times() #Imprimir lo indicado en la consola 10 veces 
        print_hello_x_or_ten_times(4) #Imprimir lo indicado en la consola 4 veces 


"""
Bonus section
"""

# print(num3) no esta definido
# num3 = 72 la variable esta definida despues de la solucitud de impresion a la consola por lo que no reconoce el valor de la misma
# fruit[0] = 'cranberry' no se puede por ser tuple
# print(person['favorite_team']) no se puede imprimir porque no es un elemento del diccionario
# print(pizza_toppings[7]) la lista solo cuenta con 5 elementos y 4 indices, no exite un indice 7
# print(boolean) no esta definido
# fruit.append('raspberry') no se puede por ser tuple
# fruit.pop(1) no se puede por ser tuple