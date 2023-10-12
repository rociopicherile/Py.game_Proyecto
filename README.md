Jugabilidad:
El juego consta de un personaje (el astronauta), y de enemigos (los ovnis, que están en constante movimiento). Se debe disparar hacia a estos últimos presionando la tecla T para hacerlos desaparecer, mientras se mueve al personaje utilizando las flechas izquierda-derecha del teclado. Tiene un menú principal (que se visualiza al ejecutar el programa, y se puede ver presionando ESC) y dentro de este se puede acceder al juego, a la ventana de help, o también se puede elegir salir.

---

Código:
\*Los png dentro de la carpeta assets fueron descargados de la página OpenGamerArt.com

Para la funcionalidad del juego hay 4 clases creadas:
-class Astronauta
Se necesita para luego inicializar al jugador que utilizamos.
Dentro de su función UPDATE() se guarda la lógica para realizar el movimiento derecha-izquierda con el teclado, teniendo en cuenta el límite del ancho de la ventana (600px). También cuenta con la función DISPARO() donde se instancia un objeto de la clase Disparos, esta tiene que acompañar a la posición del jugador mientras esté en movimiento, para simular que está disparando.
-class Disparos
Se necesita para instanciar disparos en la clase Astronauta.
Dentro de su función **init** se reciben como argumentos las posiciones X e Y del jugador y se igualan a las de las balas, como ya antes mencionado, para que se dispare desde donde está nuestro personaje. La función UPDATE () sirve para que las balas se muevan en dirección vertical.
-class Ovnis
Se necesita para instanciar a los enemigos.
Aparecen en posiciones aleatorias entre 10-300 del eje y, y se mueven sobre todo el eje x de izquierda a derecha.
-class Boton
Se necesita para instanciar botones dentro del menú principal.
Dentro de su función **init** se reciben como argumentos el png del botón (image) y la posición (pos) de donde se desea que aparezca. En la función UPDATE() se carga la imagen a la pantalla con el valor pedido. Y en la función CHECKFORINPUT() se realiza la parte lógica, donde se recibe la posición del mouse para verificar si esta coincide con la posición del rectángulo del botón, y devuelve True si es así.

También se cuenta con 3 funciones para cada ventana:
+def juego()
Aquí ocurre el juego principal
+def menu()
Menú principal con objetos del tipo Boton
+def help()
Ventana ayuda con información del juego
