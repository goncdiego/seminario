### Seminario de Lenguajes Formales - TP1

Definir una gramática para poder crear conjuntos numéricos y realizar distintas operaciones.

### Conjuntos

1) Establecer la forma de crear conjuntos numericos.
2) Establecer el conjunto de referencia (o universal).

### Ejemplos:

    A = conjunto[0..5]      //Define el conjunto {0,1,2,3,4,5} - del 0 al 5
    B = conjunto[0..10, 2]  //Define el conjunto {0,2,4,6,8,10} - del 0 al 10, salteando de a dos

### Operaciones:

1) Asignación

2) Mostrar

3) Pertenece Elemento

4) Sumar Elementos

5) Promediar Elementos

6) Longitud 

7) Complemento

8) Unión

9) Intersección

10) Diferencia

### Ejemplos:

    A = set[1,10,2]      // {1,3,5,7,9}
    A.belong(3)          // Return True
    A.belong(15)         // Return False
    C = A.intersect(B)   // Intersección
    C = A inter B        // Intersección
    A                    // Muestra el conjunto A
    res = A.sum          // Obtengo resultado de la suma

### Herramientas:
[antlr4](http://www.antlr.org/)

[python](https://www.python.org/)







