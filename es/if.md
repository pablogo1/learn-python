# Sentencia `if`-`else`

La sentencia `if` nos permite modificar el control de flujo de un programa al ejecutar una o más instrucciones de forma condicionada. Permitiendo ejecutar otro código como alternativa:

![alt text][if-else]

En pseudocódigo:
```
if (condicion es True):
    (consecuencia)
else:
    (alternativa)
```

Esto es que, si `condicion` es evaluada a `True`, las instrucciones dentro de la *consecuencia* serán ejecutadas. En cambio si `condicion` es evaluada a `False` las instrucciones dentro del bloque *consecuencia* **no** se ejecutarán y sólo se ejecutarán las instrucciones de la *alternativa*.

## Sentencia `if` sencilla

La forma más sencilla del bloque `if` permite ejecutar las instrucciones dentro del *Bloque 1* sólo si `condicion` es `True` para después ejecutar las intrucciones del *Bloque 2*. Por tanto, las instrucciones del *Bloque 2* (que se encuentran fuera del bloque `if`) son ejecutadas siempre.

```python
if condicion:
    # Bloque 1
# Bloque 2
```

El siguiente diagrama de flujo muestra como se comporta este:

![alt text][if-1]

## Sentencia `if-else`
Tal como se explicó al inicio de esta sección, permite ejecutar de forma condicionada dos bloques de código diferentes. Ya sea *Bloque 1* cuando la `condicion` sea `True` **o** *Bloque 2* cuando la `condicion` sea `False`.

```python
if condicion:
    # Bloque 1
else:
    # Bloque 2
```

El siguiente diagrama de flujo muestra como se comporta este:

![alt text][if-2]

## Sentencia `if-elif-else`
Esta forma de la sentencia `if` permite evaluar un sin-fin de condiciones y ejecutar el código especificado por condición. Opcionalmente, puede ejecutarse una *alternativa* si es que ninguna de las condiciones especificadas se cumplió.

```python
if condicion:
    # Bloque 1
elif condicion_1:
    # Bloque 2
elif condicion_2:
    # Bloque 3
else:
    # Alternativa
```
El siguiente diagrama de flujo muestra como se comporta este:

![alt text][if-3]

[if-else]: ../img/if-else.png "if-else block"
[if-1]: ../img/if-1.png "Simple if block"
[if-2]: ../img/if-2.png "Simple if/else block"
[if-3]: ../img/if-3.png "Simple if/elif/else block"