# Laboratorio docker-compose

Este repo contiene la app que vimos en la segunda clase.

Recuerda que en nuestro ejercicio en replit usamos un servicio externo para la base de datos (ElephantSQL).

Vamos a modificar este proyecto para distribuirlo usando docker-compose.

Para esto ejecuta los pasos de este laboratorio

## Paso 1:

Este repo contiene un archivo Dockerfile, revísalo y discute su contenido con tus compañeros de grupo.

Luego ejecuta este comando:

```
$  docker build -t lab7-app .
```


La opcion `-t` sirve para etiquetar (tag) las imágenes.

Al finalizar el comando anterior ejecuta:

```
$ docker images lab7-app
```

Deberías obtener el `IMAGE ID` de nuestra imagen que hemos creado.


Ejecuta la imagen con este comando:


    $ docker run IMAGE_ID
    
(Remplaza IMAGE_ID por el valor que obtuviste previamente.

Revisa que tu imagen está ejecutándose en un contenedor con el siguiente comando:

    $ docker ps -a
    
Fíjate que docker le ha asignado un nombre a tu contendor (está debajo de la columna NAMES).



Detén el contendor:

    $ docker stop CONTAINER_ID
    
    
# Paso 2
    
Vamos a crear un archivo `docker-compose.yaml` con este contenido:

```
version: "3"

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: app
    container_name: my-app
    command: "bash ./runapp.sh"
    environment:
      - CONNECTION_STRING
    expose:
      - 8000
    ports:
      - "8080:8080"
```

Preocúpate de setear la variable de entorno `CONNECTION_STRING` con el valor de la url en ElephantSQL:

    $ export CONNECTION_STRING=URL_DE_ELEPHANT
    
Copia la URL que usaste en tu Replit, si no tienes una pídele la URL al profesor:

Luego ejecuta docker-compose de este modo:

    $ docker-compose up -d --build
    
Si todo sale bien la aplicación va a estar disponible en el puerto 8080: http://127.0.0.1:8080/

Puedes "entrar" al contenedor `app` usando este comando:

    $ docker exec -it my-app bash
    
Fijate que `my-app` es el nombre que asignamos en el archivo `docker-compose.yaml`.

Estando ahí puedes chequear que python está instalado en ese entorno:

    $ python --version
    
O puedes revisar que el programa se encuentra inslado:

    $ ls -l
    
Fíjate que además te encuentras en la carpeta `app`. 


Para salir de esta sesión en el contenedor escribe `exit`.


# Paso 3

Vamos a agregar un servicio para base datos, para esto modifica el archivo `docker-compose.yaml`.

Debería quedar así:

```
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: app
    container_name: my-app
    command: "bash ./runapp.sh"
    environment:
      - CONNECTION_STRING
    expose:
      - 8080
    ports:
      - "8080:8080"
    depends_on:
      - db

  db:
    image: postgres:14-alpine
    container_name: postgres
    restart: always
    environment:
      - POSTGRES_USER
      - POSTGRES_DB
      - POSTGRES_PASSWORD
    expose:
      - "5432"
```

Con esto tenemos dos servicios: `app` y `db`. Nota que `app` depende de `db`.

Ahora configura las variables: `POSTGRES_USER`, `POSTGRES_DB`y `POSTGRES_PASSWORD`:

    $ export POSTGRES_USER=user
    $ export POSTGRES_PASSWORD=pass
    $ export POSTGRES_DB=movies
    
Por último modifica la variable de entorno `CONNECTION_STRING` para que use el servicio `db` que acabamos de definir:

    $ export CONNECTION_STRING=postgres://user:pass@db/movies
    

Puedes cambiar los valores apra `user`, `pass` o `movies`. Pero debes preocuparte que el valor entre `@` y `/` sea `db` que es el nombre del servicio de base de datos.

NOTA: si usas Mac debes setear esta variable de ambiente también:

    export DOCKER_DEFAULT_PLATFORM=linux/amd64
    
Ahora, reinicia todo ejecutando:

    $ docker-compose up -d --build
    
Si todo sale bien la aplicación va a estar disponible en el puerto 8080: http://127.0.0.1:8080/

Ahora entra al container `postgres`:

    $ docker exec -it postgres bash
    
Dentro del container postgres puedes revisar la base de datos:

    $ psql -U user movies
    bash-5.1# psql -U user movies
    psql (14.5)
    Type "help" for help.
    movies=# select * from movies;
    ....
    
    movies=# \q
    
    $ exit
    
Puedes tratar de agregar algunos registros a la tabla `movies`.

Detén los contenedores:

    $ docker-compose down
    

# Paso 4:

Ejecuta el comando:
    $ docker scan app
    
Es posible que te pida hacer un `login` a docker-hub, hazlo con tus credenciales.

Revisa el reporte y comenta con tus compañeros luego revisa con el profesor.

# Propuesto

Averigua cómo agregar volúmenes persistentes al servicio db.



