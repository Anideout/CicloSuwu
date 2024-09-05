continuación de  [[introducción C]]

	"La constante de un hombre es la variable de otro hombre"


El siguiente programa al que llamaremos pun.C 

int  main (void)
{
	printf("To C, or not to C: that is the question.\n");
	return 0;
}

#DESCONSTRUYENDO 

include <stdio.h>

es necesario "incluir" información sobre la biblioteca de I/O estándar de C (entrada/salida). EL codigo ejecutable del programa va dentro de main, que representa el programa "principal". La única línea dentro de main es un comando para mostrar el mensjae deseado. Printf es una función de la biblioteca I/O estandar que puede producir muy bien para la salida mateada. El codigo \n le dice a printf que avance a la línea siguiente despúes de impirmir el mensaje. La linea 

return 0;

indica que el programa "devuelve" el valor () al sistema operativo cuando finaliza.


Compilación y vinculación.

A pesar de su brevedad. Conseguir que pun.c se ejecute es más complicado de lo que cabría esperar. En primer lugar, necesitamos crear un archivo llamado pun.c que contenga el programa que cualquier editor de texto hará) 

Ahora. Tenemos que convertir el programa a una forma que la máquina pueda ejecutar. Para un programa C, eso generalmente implica tres pasos:

1. Preprocesamiento: 
	El programa se da primero a un preprocesador, que obedece órdenes que comienzan con # (conocidas como directivas). Un preprocesador es un poco como un editor, puede agregar cosas al programa y hacer modificaciones.
2. Compilación:
	El programa modificado ahora va a un compilador, que lo traduce en instrucciones de máquina (código objeto). Sin embargo, el programa aún no está listo para ejecutarse.

3. Vinculación:
	En el paso final, un enlazador combina el código objeto producido por el compilador con cualquier código adicional necesario para producir un programa ejecutable completo. Este código adicional incluye funciones de biblioteca (como printf) que se utilizan en el programa.  
	
Afortunadamente, este proceso suele estar automatizado, por lo que no le resultará demasiado oneroso. De hecho, el preprocesador suele estar integrado con el compilador, por lo que probablemente ni siquiera lo notarás en funcionamiento. Los comandos necesarios para cumplir y vincular varían, según el compilador y el sistema operativo. En UNIX, el compilador de C suele denominarse cc. Para compilar y vincular el programa pun.c, ingrese el siguiente comando en una terminal o ventana de línea de comandos: 

cc pun.c

el carácter % es el símbolo del sistema UNIX, no es algo que deba ingresar). La vinculación es automática cuando se usa cc; No es necesario ningún comando de enlace independiente. Después de compilar y vincular el programa, cc deja el programa ejecutable en un archivo llamado a.out de forma predeterminada. CC tiene muchas opciones; Una de ellas (la opción -o) nos permite elegir el nombre del fichero que contiene el programa ejecutable. Por ejemplo, si queremos que la versión ejecutable de pun.c se llame pun, ingresaríamos el siguiente comando: 

cc -o pun pun.c

el compilador GCC 

Uno de los compiladores de C más populares es el compilador GCC, que se suministra con Linux pero también está disponible para muchas otras plataformas. El uso de este compilador es similar al uso del compilador cc tradicional de UNIX. Por ejemplo, para compilar el programa pun.c, usaríamos el siguiente comando: 
gcc -o pun  pun.c


Entornos de desarrollo integrados

Hasta ahora, hemos asumido el uso de un compilador de "línea de comandos" que se invoca ingresando un comando en una ventana especial proporcionada por el sistema operativo. La alternativa es utilizar un entorno de desarrollo integrado (IDE), un paquete de software que nos permite editar, compilar, enlazar, ejecutar e incluso depurar un programa sin salir del entorno. Los componentes de un IDE están diseñados para funcionar juntos. Por ejemplo, cuando el compilador detecta un error en un programa, puede hacer que el editor resalte la línea que contiene el error. Hay una gran variación entre los IDE, por lo que no los discutiré más en este libro. Sin embargo, te recomiendo que compruebes qué IDE están disponibles para tu plataforma.

La forma general de un programa simple Echemos un vistazo más de cerca a pun.c y veamos cómo podemos generalizarlo un poco. Los programas de tamaño C tienen la forma


directives

int main(void)
{
	statements
}
en esta plantilla, y en plantillas similares en otras partes de este libro, los artículos impresos en courier aparecerían en un programa C exactamente como se muestra; Los elementos en cursiva representan el texto que debe proporcionar el programador. Observe cómo las llaves muestran dónde comienza y termina main. C usa {y} de la misma manera que algunos otros idiomas usan palabras como begin y end. Esto ilustra un punto general sobre C: se basa en gran medida en abreviaturas y símbolos especiales, una de las razones por las que los programas de C son concisos (o, menos caritativamente, cryp-tic).

Incluso los programas C más simples se basan en tres características clave del lenguaje: directivas (comandos de edición que modifican el programa antes de la compilación), funciones (bloques con nombre de código ejecutable, de los cuales main es un ejemplo) y declaraciones (comandos que se ejecutan cuando se ejecuta el programa). Ahora echaremos un vistazo más de cerca a estas características



Directivos

antes de compilar un programa C, primero es editado por un preprocesador. Los comandos destinados al preprocesador se denominan directivas. Los capítulos 14 y 15 detallan las directivas. Por ahora, solo nos interesa la directiva #include. El programa pun.c comienza con la línea #include Esta directiva establece que la información en debe "incluirse" en el programa antes de que se compile. contiene información sobre la biblioteca de E/S estándar de C. C tiene una serie de encabezados como ; cada uno contiene información sobre alguna parte de la biblioteca estándar. la razón por la que incluimos.
Las directivas siempre comienzan con un #character, lo que las distingue de otros elementos de un programa C. De forma predeterminada, las directivas tienen una línea de longitud; No hay punto y coma ni otro marcador especial al final de una directiva.


funciones

Las funciones son como "procedimientos" o "subrutinas" en otros lenguajes de programación, son los bloques de construcción a partir de los cuales se construyen los programas. De hecho, un programa C es poco más que una colección de funciones. Las funciones se dividen en dos categorías: las escritas por el programador y las proporcionadas como parte de la implementación de C. Me referiré a estas últimas como funciones de biblioteca, ya que pertenecen a una "biblioteca" de funciones que se suministran con el compilador. El término "función" proviene de las matemáticas. Donde una función es una regla para calcular un valor cuando se le dan uno o más argumentos:


f(x) = x + 1
g(y, z) = y² - z²

C usa el término "función" de manera más vaga. En C, una función es simplemente una serie de enunciados que se han agrupado y se les ha dado un nombre. Algunas funciones calculan un valor; otros no. Una función que calcula un valor utiliza la instrucción return para especificar qué valor "devuelve". Por ejemplo, una función que agrega I a su argumento podría ejecutar la instrucción

return x + 1;

mientras que una función que calcula la diferencia de los cuadrados de sus argumentos podría ejecutar la instrucción

return y * y - z * z;

aunque un programa C puede constar de muchas funciones, sólo la función principal es obligatoria. Main es especial: se llama automáticamente cuando se ejecuta el programa. Hasta el capítulo 9, donde aprenderemos a escribir otras funciones, main será la única función en nuestros programas.


aunque un programa C puede constar de muchas funciones, sólo la función principal es obligatoria. Main es especial: se llama automáticamente cuando se ejecuta el programa. Hasta el capítulo 9, donde aprenderemos a escribir otras funciones, main será la única función en nuestros programas.

el nombre main es fundamental; NO puede ser begin o start o incluso main


Si main es una función, ¿devuelve un valor? Sí: devuelve un código de estado que se le da al sistema operativo cuando finaliza el programa. Echemos otro vistazo al programa pun.c:


#include <stdio.h>

int main(void)
{
	printf(2To C, or not to C: that is the quesiton. \n);
	return 0;
}

La palabra int justo antes de main indica que la función main devuelve un valor entero. La palabra void entre paréntesis indica que main no tiene argumentos.


La declaración

return 0;

Tiene dos efectos: hace que la función principal termine (terminando así el programa) e indica que la función principal devuelve un valor de 0. Tendremos más que decir sobre el valor de retorno de main en un capítulo posterior. Por ahora, siempre haremos que main devuelva el valor 0, que indica la terminación normal del programa

Si no hay una instrucción return al final de la función principal, el programa terminará de todos modos. Sin embargo, muchos compiladores producirán un mensaje de advertencia (porque se suponía que la función debía devolver un número entero pero no lo hizo).

Declaración

Una declaración es un comando que se ejecuta cuando se ejecuta el programa. Exploraremos las declaraciones más adelante en el libro, principalmente en los capítulos 5 y 6. El programa pun.c utiliza solo dos tipos de declaraciones. Una es la declaración de retorno; La otra es la llamada a la función. Pedirle a una función que realice su tarea asignada se conoce como llamar a la función. El programa pun.c, por ejemplo, llama a la función printf para mostrar una cadena en la pantalla:

printf("Es C o no es C: esa es la pregunta.\n");

C requiere que cada instrucción termine con un punto y coma. (Como con cualquier buena regla, hay una excepción: la declaración compuesta, que encontraremos más adelante). El punto y coma muestra el compilador donde termina la instrucción; Dado que las declaraciones pueden continuar a lo largo de varias líneas, no siempre es obvio dónde terminan. Las directivas, por otro lado, normalmente tienen una línea y no terminan con un punto y coma

imprimir strings

printf es una función poderosa que examinaremos en el capítulo 3. Hasta ahora, solo hemos usado printf para mostrar un literal de cadena una serie de caracteres encerrados entre comillas dobles. Cuando printf muestra un literal de cadena, no muestra las comillas.

printf no avanza automáticamente a la siguiente línea de salida cuando termina de imprimirse. Para indicar a printf que avance una línea, debemos incluir \n (el carácter de nueva línea) en la cadena que se va a imprimir. Al escribir un nuevo carácter de línea, se termina la línea de salida actual; La salida subsiguiente pasa a la siguiente línea. Para ilustrar este punto, considere el efecto de reemplazar la declaración

printf("es c, o no es c: esa es la pregunta.\n");

con 2 llamadas de printf:

printf("Es C, o no es C: ");
printf("Esa es la pregunta")


la primera llamada de printf escribe a C, o no a C: la segunda llamada escribe que esa es la cuestión. Y avanza a la siguiente línea. El efecto neto es el mismo que el de la impresión original: el usuario no puede notar la diferencia. 
	El nuevo carácter de línea puede aparecer más de una vez en un literal de cadena. Para mostrar el mensaje

"La brevedad es el alma del ingenio"
--
Podríamos escribir

printf("La Brevedad es el alma del ingenio. \n --Shakespeare\n");


A nuestro programa PUN.C todavía le falta algo importante: documentación. Cada programa debe contener información identificativa: el nombre del programa, la fecha en que se escribió, el autor. El propósito del programa, y así sucesivamente. En C, esta información se coloca en los comentarios. El símbolo /* marca el comienzo de un comentario y el símbolo */ marca el final:

/* El comentario */

Los comentarios pueden aparecer en casi cualquier parte de un programa. Ya sea en líneas separadas o en las mismas líneas que otro texto del programa. Este es el aspecto que podría tener pun.c con los comentarios añadidos al principio

Declaraciones 

Las variables deben declararse (describirse para el beneficio del compilador) antes de que puedan usarse. Para declarar una variable, primero especificamos el tipo de la variable, luego su nombre. (Los nombres de las variables son modificados por el programador, sujetos a las reglas descritas en la sección 2,7) Por ejemplo, podríamos declarar las variables height y profit de la siguiente manera;

int height;
float profit;

La primera declaración indica que height es una variable de tipo int, lo que significa que height puede almacenar un valor entero. La segunda declaración dice que el beneficio es una variable de tipo float. Si varias variables tienen el mismo tipo, sus declaraciones se pueden combinar

int height, length, width, volume;
float profit, loss;

Observe que cada declaración completa termina con un punto y coma. Nuestra primera plantilla para main no incluía declaraciones.Cuando main contiene declaraciones, estas deben preceder a las declaraciones:

int main (void)
{
	declarations
	statements
}

Como veremos en el capítulo 9, esto es cierto para las funciones en general, así como para los bloques (sentencias que contienen declaraciones incrustadas). Como cuestión de estilo, es una buena idea dejar una línea en blanco entre las declaraciones y las declaraciones.
	En c99, las declaraciones no tienen por qué ir antes de las declaraciones. Por ejemplo, main puede contener una declaración, luego una instrucción y, a continuación, otra declaración. Por compatibilidad con compiladores más antiguos, los programas de este libro no se aprovechan de esta regla. Sin embargo, es común en los programas C++ y Java no declarar variables hasta que se necesiten por primera vez, por lo que se puede esperar que esta práctica también se vuelva popular en los programas C99

Asignación
A una variable se le puede dar un valor por medio de la asignación. Por ejemplo, las sentencias:

altura = 8;
largo = 12;
ancho = 10;

Asignar valores a la altura, la longitud y la anchura Se dice que los números 8, 12 y 10 son constantes
	Antes de que a una variable se le pueda asignar un valor, o usarse de cualquier otra manera, primero debe declararse. Así, podríamos escribir

int height;
height = 8;

but not 
height = 8; /*** WRONG *** /
int height;

Una constante asignada a una variable float suele contener un separador decimal. Por ejemplo, si el profit es una variable float, podríamos escribir

profit = 2150,48;


Es mejor agregar la letra F (para "float") a una constante que contenga una pinta decimal si el número está asignado a una variable float:

profit = 2150.48f;

Si no se incluye la f, es posible que el compilador emita una advertencia. A una variable int normalmente se le asigna un valor de tipo int, y a una variable float normalmente se le asigna un valor de tipo float. Tipos de mezcla (como asignar un valor int a una variable float o asignar un valor float a una variable int) es posible, pero no siempre seguro, como veremos en la sección 4.2

Una vez que a una variable se le ha asignado un valor, se puede utilizar para ayudar a calcular el valor de otra variable:
Una vez que a una variable se le ha asignado un valor, se puede utilizar para ayudar a calcular el valor de otra variable:

height = 8;
lengh = 12;
width = 10;
volume = height * lenght * width;  

Imprimir el valor de una variable Podemos usar printf para mostrar el valor actual de una variable. Por ejemplo, para escribir el mensaje

height: h

donde h es el valor actual de la variable height, usaríamos la siguiente llamada de printf:

printf("Height: %d\n", height);leng
