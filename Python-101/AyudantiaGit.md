## **Ayudantía 2** -  *Física computacional II*

#### **Actividad: GitHub 101**

Teniendo git instalado en el computador, podremos configurarlo con GitHub para colaborar con otros creadores. Si no tienen git instalado pueden ver la documentación para instalarlo en diferenets sistemas operativos [acá](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 

#### **Git**

Para configurar su correo, y username pueden simplemente: 

```console
$ git config --global user.name "Juanito Perez"
$ git config --global user.email juanitoperez@gmail.com
```

Pueden revisar eventualmente que su configuración este bien con:

```console
$ git config --list
```

Y ver todas las configuraciones que tienen guardadas. 

Para iniciar un repositorio deberán simplemente ir a la carpeta que quieran convertir en un repositorio y en su terminal correr: 

```console
$ git init
```

Ahora que tienen creado el repositorio, git al final les ayudará a dejar un registro del trabajo que vayan desarrollando. Funciona en base a **"commits"**. Que serán comentarios que podrán hacer a los avances que vayan haciendo. 

Luego de hacer un avance pueden agregarlo con: 

```console
$ git add archivo_agregado.py
```

Y hacer un comentario, como: *"Hola mundo"*

```console
$ git commit -m "Hola mundo"
```

Finalmente, en cualquier momento podrán revisar el status del git (que documentos añadieron, si hicieron commit o no, etc) para corroborar el trabajo que llevan haciendo, utilizando: 

```console
$ git status
```

Hasta ahora solo se ha trabajado de forma local en sus computadores. Pero para añadir el repositorio creado a una plataforma remota como GitHub deben hacerlo con: 

```console
$ git remote add origin https://github.com/nombre-suario/nombre-del-repositorio.git
```
**Nota: El repositorio en GitHub ya debe estar creado, para hacerlo*


#### **Como primera actividad configuren su git y creen un repositorio en GitHub de prueba.**


Por otro lado, si quieren clonar un repositorio para colaborar con otros, pueden hacerlo mediante una clave ssh: 

```console
$ git clone git@github.com:FmellaA/Ayudantias-compu-2.git
```

Y si tienen el permiso para trabajar dentro del repositorio, podrán hacerlo. 

Ahora para colaborar con otros funcionará en terminos de "pulls" y "pushs" tal que ustedes podrán "subir" sus commits a la plataforma usando: 

```console
$ git push
```

Y otros podrán "bajar" los commits a su repositorio local usando: 

```console
$ git pull
```

Por lo que la **fórmula fundamental de todo esto es:**

```console
$ git pull
$ git add archivo_agregado.py
$ git commit -m "Hola Mundo"
$ git push
```

**Si estan colaborando, antes de empezar a trabajar, **SIEMPRE** recuerden hacer **git pull***
