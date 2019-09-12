# Las Bases

## Expresiones
La instrucción más sencilla que Python puede ejecutar se conoce como *expresión*. 
```
>>> 1 + 2
3
```
Una *expresión* consiste de *valores* (como el `2`) y operadores (como el `+`) y siempre se pueden *evaluar* a un solo valor (que en este caso es `3`). Un solo valor sin operadores en considerado una *expresión* que se evalúa a si mismo.
```
>>> 2
2
```

## Operadores
| Operador | Operación | Ejemplo |
| :------: | --------- | ------- |
| `**` | Exponente | `2 ** 2 = 4` |
| `%` | Módulo (Restante de la división) | `2 % 2 = 0` |
| `//` | División Entera | `22 // 8 = 2` |
| `/` | División | `22 / 8 = 2.75` |
| `*` | Multiplicación | `2 * 8 = 16` |
| `-` | Resta | `22 - 2 = 20` |
| `+` | Suma | `2 + 8 = 10` |

Esta es la lista de operadores usados en Python (ordenados en orden de precedencia de mayor a menor). Las expresiones se evalúan de izquierda a derecha y se pueden "agrupar" términos para cambiar la precedencia de evaluación usando paréntesis.

## Sentencias de Python
Las instrucciones que Python ejecuta se les conoce como *sentencias*. Ejemplo, `a = 1` es una sentencia de asignación.

Por lo general, las sentencias van en una sola línea por sentencia, pero cabe la posibilidad de tener una sola sentencia ocupando varias líneas o incluso de incluir varias sentencias en una sola línea:

### Una sola línea:
```python
sum = 1 + 2
```
### Multi-línea:

Se usa el caracter **\\** para indicar explícitamente multiples líneas para la sentencia:
```python
sum = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        8 + 9 + 10
```
O cuando se usan paréntesis **( )**, corchetes **[ ]** o llaves **{ }** se puede usar multi-línea de forma implícita sin tener que usar la diagonal (**\\**):
```python
sum = (1 + 2 + 3 +
        4 + 5 + 6 +
        8 + 9 + 10)
```

### Múltiples sentencias por línea
Al usar el caracter de punto y coma (**;**) podemos indicarle al intérprete de Python que se trata de sentencias separadas y que se tienen que ejecutar una por una (en lugar de la línea completa). 
```python
a = 1; b = 2; c = 3
```

## Tipos de Datos
Recordamos que las expresiones son sólo valores combinados con operadores que evalúan a un sólo valor. Un *tipo de dato* es una categoría para lo valores, y cada valor pertenece a un sólo tipo de dato. Los tipo de dato más comunes en Python:

| Tipo de Dato | Ejemplos |
| ------------ | -------- |
| Enteros (`int`) | `-2, -1, 0, 1, 2, 3` |
| Decimales o Punto flotante (`float`) | `-1.25, -2.15, 3.14159268` |
| Cadenas (`str`) | `'a', 'b', 'esta es una cadena.', '', ' '` |

Los tipos de dato en Python determinan como se comportan los diferentes operadores al ser evaluados en una expresión. 
```python
>>> 'Alice' + 'Bob'
'AliceBob'
```
En el anterior ejemplo, a la presencia de dos valores `string` el operador `+` realiza una *concatenación* de ambas cadenas para producir una nueva incluyendo los valores en ambos lados del operador.

Pero cuando Python no pueda determinar (por los tipos de datos involucrados) qué hacer, el intérprete lanza un error:
```
>>> 'Alice' + 72
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    'Alice' + 42
TypeError: can only concatenate str (not "int") to str
```

En el anterior, el error se debe a que Python no puede concatenar dos cadenas cuando uno de los operandos _no es_ una cadena. En este caso el valor `int` de `72` no se puede concatenar a la cadena `'Alice'`.

## Referencias
1. [Python Statements, Identation and Comments](https://www.programiz.com/python-programming/statement-indentation-comments)
2. [Automate the Boring Stuff - Chapter 1](https://automatetheboringstuff.com/chapter1/)