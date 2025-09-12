### **Ayudantía 2** -  *Física computacional II*
#### **Actividad: How to LaTeX+git**
Una vez se hayan familiarizado un poco con el ambiente de git y sus maravillosas herramientas, les surgirá cierta duda de, bueno ¿Para que sirve esto aparte de código? y si bien la respuesta es para lo que quieran, dentro del semestre les será de interés (obligación, jaja) el aprender a utilizar git/github para escribir sus documentos en LaTeX y manejarlos mediante commits, versiones, comentarios, etc, aparte de ser la forma más popular de compartir proyectos/portafolios. 

A continuación les dejaré una guía básica de cómo instalar de forma exitosa LaTex en su máquina e integrarlo dentro de su editor de código favorito.
Lo primero que necesitan instalar será las dependencias de LaTex propiamente tal, los que usen GNU/Linux lo tendrán más fácil (esto es un guiño para los que no usan aún, que se cambien); 

Paquete de distribución de TexLive que incluye de por sí algunos paquetes importantes;
```bash 
$ sudo pacman -S texlive-most
```
Algunos paquetes de lenguages y fonts, Español y fonts científicos;
```bash
$ sudo pacman -S texlive-langspanish texlive-science texlive-fontsextra texlive-formatsextra
```
Instalar un compilador automático;
```bash
$ sudo pacman -S texlive-core
```
Todo esto tiene que ser con el gestor de packetes de su distribución de Linux, en mi caso es Arch.

Ahora necesitan checkear si los paquetes fueron instalados on éxito y en qué versión se encuentran.

Versión de pdfLaTeX
```bash
$ pdflatex --version
```
Versión de latexmk
```bash
$ latexmk --version
```
En caso que no les aparezca la versión de alguno de estos paquetes, consulten la respectiva Wiki de su distribución de Linux por si se necesita alguna otra dependencia o no está incluido por defecto en los paquetes listados acá. 


Luego, en este repositorio encontrarán una carpeta con un archivo .tex que les he subido de ejemplo (el primer pdf decente que pillé y que use hartas funciones de interés), para copiarlo pueden usar el siguiente comando;

```bash
$ git clone --no-checkout --depth=1 https://github.com/FmellaA/Ayudantias-compu-2 && cd Ayudantias-compu-2 && git sparse-checkout init --cone && git sparse-checkout set "LaTeX example" && git checkout && cd ..
```
o descargar directamente la carpeta de "LaTeX examples" desde el [github](https://github.com/FmellaA/Ayudantias-compu-2 ) como se indica a continuación;
```bash
$ git clone https://github.com/FmellaA/Ayudantias-compu-2.git
```
y luego simplemente entrar a la carpeta con el documento .tex;
```bash
$ cd Ayudantias-compu-2/LaTeX\ example
```
Para compilar un archivo, como se acordarán de su hermoso curso de Computación Científica, es haciendo uso del comando;
```bash
$ pdflatex tu-archivo.tex
```

Pero en esta guía les enseñaré una herramienta mucho más útil para de verdad compilar documentos en los que trabajen seriamente, haciendo uso de la herramienta que acaban de instalar;

Para compilar una vez se usa;
```bash
$ latexmk -pdf tu-archivo.tex
```
Para limpiar los archivos auxiliares;
```bash
$ latexmk -c
```
Por último y más importante, la función de compilar continuamente con detección de cambios al guardar;
```bash
$ latexmk -pdf -pvc tu-archivo.tex
```
Ahora, como ya han aprendido a inicializar un proyecto en git/github es importante configurar un archivo .gitignore, esto sirve para que todos los archivos auxiliares que aparezcan al compilar en local no se suban a su bonito repositorio en github o proyecto en git y se vea mucho mas limpio, un ejemplo de archivo .gitignore es el siguiente;

```txt
# LaTeX auxiliary files
*.aux
*.log
*.out
*.toc
*.blg
*.bbl
*.bcf
*.run.xml
*.synctex.gz
*.fdb_latexmk
*.fls
*.lof
*.lot
*.nav
*.snm
*.vrb

# PDF output (optional - include if you don't want to track PDFs)
*.pdf

# Backup files
*~
*.backup

# Editor files
.vscode/
.idea/
```
Al cual le pueden añadir y quitar tipos de archivo según las necesidades de su proyecto. 

#### ***Implementación dentro de editores de texto/código***
Existen varios editores especializados para escribir y compilar en LaTeX que seguramente ya conocen, pero, en este curso ustedes estarán constantemente viendo su código en .py o .ipynb a la vez que escriben su pdf, con lo cual es útil el tener una buena configuración de compilación de LaTeX dentro de su editor. 

Recomiendo fuertemente, ya que a la larga es buena práctica, el que revisen con calma la wiki de su editor de código, en donde seguramente en contrarán una muy buena guía de las dependencias e implementación de compilación de LaTex.

#### ***Implementación en Windows y VS Code***

En este documento, por ahora solo se ha mencionado el procedimiento en GNU/Linux para una buena instalación básica de LaTeX, pero, una elección popular de sistema operativo también es Windows, a lo cual aquí tienen un [link](https://www.tug.org/texlive/windows.html) para la correcta instalación de TeX Live en Windows. Asegurarse de realizar la instalación completa de latexmk y los paquetes como los que mencioné en la instalación anterior.

Después, pueden verificar en la CMD o PowerShell que los paquetes estén correctamente instalados con los siguientes comandos;

```cmd
$ pdflatex --version
$ latexmk --version
```

#### ***Configuración e implementación en VS Code***

Para utilizar estas herramientas en el editor más popular y diría que más intuitivo, aunque con sus drawbacks, la implementación en VS Code y VS Codium, es bastante directa, y la misma tanto en GNU/Linux como en Windows.

Para ello solo será necesario que busquen el paquete de LaTeX Workshop, por James Yu e instálenla.

Dentro de la configuración de LaTeX Workshop, en Preferences > Settings (Ctrl +,), buscar "LaTeX" y luego editar el archivo de settings.json, les recomiendo la siguiente configuración, aunque siempre es bueno leer la Wiki y hacerlo ustedes mismos;

```json
`"latex-workshop.latex.autoBuild.run": "onSave", // Compila automáticamente al guardar
"latex-workshop.latex.recipe.default": "latexmk", // Usa latexmk por defecto
"latex-workshop.latex.tools": [
  {
    "name": "latexmk",
    "command": "latexmk",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-pdf",
      "-outdir=%OUTDIR%",
      "%DOC%"
    ]
  }
],
"latex-workshop.view.pdf.viewer": "tab", // Abre el PDF en una pestaña dentro de VS Code
"latex-workshop.latex.clean.fileTypes": [ // Define qué archivos limpiar
    "*.aux", "*.bbl", "*.blg", "*.idx", "*.ind", "*.lof", "*.lot",
    "*.out", "*.toc", "*.acn", "*.acr", "*.alg", "*.glg", "*.glo",
    "*.gls", "*.ist", "*.fls", "*.log", "*.fdb_latexmk", "*.snm", "*.nav", "*.vrb"
],
```
#### ***Flujo de trabajo en VS Code***
Cuando abran su proyecto LaTeX en VS Code verán un ícono de TeX, haciendo click en él se desplegará el panel de LaTeX Workshop, desde este panel es posible compilar el proyecto, ver el PDF y limpar los archivos auxiliares.

La idea es que con latexmk su proyecto sea compilado cada vez que se guarde, si ha logrado esto, tendrá a su disposición un muy útil flujo de trabajo en uno de los editores de código con más support que existen.


