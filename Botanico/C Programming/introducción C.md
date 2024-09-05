	Cuando alguien dice "Quiero un lenguaje de programación en el que solo necesite decir lo que se deseo que se haga", dale una paleta.



¿Qué es C? la respuesta simple (un lenguaje de programación ampliamente utilizado desarrollado a principios de la década de 1970 en los laboratorios Bell) transmite poco del sabor especial de C. Antes de sumergirnos en lv os detalles del lenguaje, echemos un vistazo a de dónde vino C, para qué fue diseñado y cómo ha cambiado a lo largo de los años (sección 1.1). También analizaremos las fortalezas y debilidades de C y veremos cómo aprovechar al máximo el lenguaje.



1. Historia de C 
		Echemos un vistazo rápido a la historia de C, desde sus orígenes hasta su madurez 
		como lenguaje estandarizado y su influencia en los lenguajes recientes.
			C es un subproducto del sistema operativo UNIX, que fue desarrollado en los laboratorios Bell por Ken Thompson, Dennis Ritchie y otros. Thompson escribió solo la versión original de UNIX, que se ejecutaba en la computadora DEC PDP-7, una de las primeras minicomputadoras con solo 8K palabras de memoria principal (¡después de todo, esto era 1969!).
			Como otros sistemas operativos de la época. UNIX fue escrito en lenguaje ensamblador. Los programas escritos en lenguaje ensamblador suelen ser complicados de depurar y difíciles de mejorar; UNIX no fue la excepción. Thompson decidió que un nivel superior

2. Introducción a C.
			El lenguaje era necesario para el desarrollo posterior de UNIX. Por lo que se diseñí un pequeño lenguaje llamado B. Thompson basado e B en BCPL, una lan de programación de lenguajes desarrolladps a mediados de la década de 1960. BCPL, a su vez, remonta su ascedencia a algol 60, uno de los primeros (y más influyentes) lenguajes de programación.
				Ritchie pronto se unió al proyecto UNIX y comenzó a programar en B. En 1970, Bell Labs adquirió un PDP-11 para el proyecto UNIX. una vez que B estaba funcionando en la PDP-11, Thompsong reescribió una parte de UNIX en B. Para 1971, se hizo evidente que b no se adaptaba bien a pdp-11, por lo que ritchie comenzó a desarrolar una versión extendida de B. Llamó a su lenguaje NB ("Nuevo B") al principio, y luego, como comenzó a divergir más de B, cambió el nombre a C. El idioma era lo suficientemente estable para 1973, para que UNIX se pudiera reescribir en C. El cambio a C proporcionó un beneficio importante: POrtabilidad. Escribiendo compiladores C para otras computadores en Bell Labs, el equipo también podría ejecutar UNIX en esas máquinas. 
	Normalización:
			C continuó evolucionando durante la década de 1970, especialmente entre 1977 y 979. Fue durante este período cuando apareció el primer libro sobre C. El lenguaje de Programación C, escrito por Brian Kernighan y Dennis Rtchie y Publiseh en 1978, se cnvirtió rapidamente en la biblia de los programadores en C. En ausencia de un estándar oficial para C, este libro, conocido como K&R o el "libro blanco" para los aficionados, sirvió como un estándar de factos (XD)
				Durante la década de 1970, había relativamente pocos programadores de C, y la mayoría de ellos eran usuarios de UNIX. EN la década de 1980, sin embargo, se había expandido más allá de los estrechos confines del mundo UNIX. Las compilaciones de C estuvieron disponibles en una variedad de máquinas que se ejecutaban bajo diferentes SO. En particular, C comenzó a establecerse en la plataforma de rápido crecimiento IBM. 
					Con la creciente popularidad de C llegaron los Problemas. Los programadores que escribían nuevos compiladores de C se basaron en K&R como referencia. Des-afortunadamente, K&R era confuso acerca de algunas características del lenguaje, por lo que los compiladores a menudo trataban estas características de manera diferente, además K&R no pudo hacer una distinción clara entre qué características pertenecían a C y cuáles eran parte de UNIX. para empeorar las cosas, C comenzó a cambiar después de que se publicara K&R, con la adición de nuevas características y la eliminación de algunas características más antiguas. Pronto se hizo evidente la necesidad de una descripción precisa y actualizada de la lengua. Sin e. Sin este estándar, habrían surgido numerosos dialectos, amenazando la portabilidad de los programas C, una de las principales fortalezas del lenguaje.
						El desarrollo de un es´tandar estadounidense para C comenzó en 1983 bajo los auspicios del American National Standars Institute (ANSI). Después de muchas revisiones, la norma se completó en 1988 y se aprobó formalmente en diciembre de 1989 como norma ANSI X3.159-1989. en 1990, fue aprobado por la organización Internacional para la Estandarización (ISO) como normal internacional ISO/IEC 9899:1990, esta versión del lenguaje generalmente se conoce como c89 o c90, para distinguirla de la versión original de c, a menudo llamada K&R C. 
						Apéndice C resume las principales diferencias entre c89 y K&R C 
							Debido a que c00 aún no es universal, y debido a la necesidad de mantener millones (si no miles de millones) de lineas de código escritas en versiones anteriores de C, usaré un icono especial (que se muestra en el margen izquierdo) para marcar las discusiones de las caracteristicas que se agregaron en c99. Un compilador que no reconoce estas características, "no es compatible con c99" Si la historia sirve de guía, pasarán algunos años antes de que todos los compiladores de C sean compatibles con c99, si es que alguna vez lo son. En el apéndice B se enumeran las principales diferencias entre C99 y C
							89
			Lenguajes C-basados:
				C ha tenido una gran influencia en los lenguajes de programación modernos, muchos de los cuales toman prestado mucho de él. De los muchos lenguajes basados en C, varios son especialmente prominentes:
					1. C++: 
						Incluye todas las características de C, pero agrega clases y otras características para admitir la programación orientada a objetos.
					2. Java:
						Está basado en c++ y, por lo tanto, hereda muchas características de C.
					3. C#:
						Es un lenguaje más reciente derivado de C++ y Java
					4. Perl:
						Era originalmente un lenguaje de Scripting bastante simple; con el tiempo ha crecido y adoptado muchas de las características de C 
			Teniendo en cuenta la popularidad de estos nuevos idiomas, es lógico preguntarse si vale la pena aprender C. Creo que sí, por varias razones. En primer lugar, el aprendizaje de C puede dar una mayor compresión de las características de c++, java, c, perl y los otros lenguajes basados en C. Los programadores que aprenden primero uno de estos idiomas, a menudo no logran dominar las características básicas que se heredaron de C. En segundo lugar, hay muchos programas C más antiguos; es posible que necesite leer y mantener código. En tercer lugar, C sigue siendo ampliamente utilizado para desarrollar nuevo software, especialmente en estudios en lo que la memoria o la potencia de procesamiento son limitadas o en los que se desea la simplicidad de C.
				Si aún no ha utilizado uno de los nuevos lenguajes basados en C, encontrará que este libro es una excelente preparación para aprender estos idiomas. Enfatiza la abstracción de datos, la ocultación de información y otros principios que juegan un papel importante en la programación orientada a objetos. C++ incluye todas las caracteristicas de C, por lo que podrás usar todo lo que aprendas en este libro si luego abordas en C++. Muchas de las características de C también se pueden encontrar en los otros lenguajes basados en C.
						
						
						