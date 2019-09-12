# Estructuras de Control

De la [Wikipedia](https://es.wikipedia.org/wiki/Estructuras_de_control):
> En lenguajes de programación, las **estructuras de control** permiten modificar el flujo de ejecución de las instrucciones de un programa.
>
> Con las estructuras de control se puede:
> * De acuerdo con una condición, ejecutar un grupo u otro de sentencias (`if-then-else`)
> * De acuerdo con el valor de una variable, ejecutar un grupo u otro de sentencias (`switch-case`)
> * Ejecutar un grupo de sentencias **mientras** se cumpla una condición (`do-while`)
> * Ejecutar un grupo de sentencias **hasta** que se cumpla una condición (`do-until`)
> * Ejecutar un grupo de sentencias un número determinado de veces (`for-next`)
>
> Todas las estructuras de control tienen un único punto de entrada. Las estructuras de control se pueden clasificar en: secuenciales, iterativas y de control avanazadas. Esta es una de las cosas que permiten que la programación se rija por los principios de la programación estructurada.

De acuerdo a los [principios de Python](https://www.python.org/dev/peps/pep-0020/): 
> Sólo puede haber una, y preferentemente sólo una, forma obvia de hacer las cosas.

Algunas de las formas listadas anteriormente no están provistas de forma natural en el lenguaje (es decir, que existan palabras clave como `do-while` , `do-until` o `switch-case`). Esto no quiere decir que en Python no se puedan usar tales estructuras de control. Simplemente que hay otras maneras de implementarlos usando los bloques básicos (`if-else` o `while`).

## if-then-else
*Véase [`if`](if.md)*

## switch-case
En Python no se dispone, como en otros lenguajes, una sentencia `switch` o `select case`. En tal caso, ésto mismo se puede realizar usando [`if-elif-else`](if.md#sentencia-if-elif-else). Ejemplo:

```python
print ('Elija su bebida preferida:')
print ('1. Café')
print ('2. Refresco')
print ('3. Agua')

eleccion = int(raw_input()) # Lee el número que ingresa el usuario por medio de un teclado
if eleccion == 1:
    print ('Preparando un café...')
elif eleccion == 2:
    print ('Despachando una coca...')
elif eleccion == 3:
    print ('Sirviendo un vaso de agua...')
else:
    print ('Elección no válida.')
```