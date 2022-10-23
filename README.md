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


    $ docker run app IMAGE_ID
    
(Remplaza IMAGE_ID por el valor que obtuviste previamente.

Revisa que tu imagen está ejecutándose en un contenedor con el siguiente comando:

    $ docker ps
    
Fíjate que docker le ha asignado un nombre a tu contendor (está debajo de la columna NAMES).

Puedes "entrar" al contenedor usando este comando:

    $ docker exec -it NOMBRE_DEL_CONTENEDOR bash
    
Reemplaza NOMBRE_DEL_CONTENEDOR con el nombre que docker asigno a tu contenedor.

Estando ahí puedes chequear que python está instalado en ese entorno:

    $ python --version
    
O puedes revisar que el programa se encuentra inslado:

    $ ls -l
    
Fíjate que además te encuentras en la carpeta `app`. 


Para salir de esta sesión en el contenedor escribe `exit`.

Detén el contendor:

    $ docker stop CONTAINER_ID
    
    
# Paso 2
    
Vamos a crear un archivo docker-compose.yaml` con este contenido:

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

    $ docker-compose up --build
    
Si todo sale bien la aplicación va a estar disponible en el puerto 8080: http://127.0.0.1:8080/

