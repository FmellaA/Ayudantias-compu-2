Para paquetes de $\LaTeX$ que les puedan servir para utilizar son: 

```latex
\usepackage{listings} [1]

```
Para configurar cada uno les recomendamos buscar la documentación de cada paquete o utilizar su Inteligencia Artificial de preferencia para hacerlo. 

### [1] Para poner códigos en $\LaTeX$: Listings 

```latex
\lstset{
    language=Python,                % Lenguaje del código
    basicstyle=\ttfamily,           % Estilo de fuente básico
    keywordstyle=\color{red},      % Color de las palabras clave
    stringstyle=\color{cyan},        % Color de las cadenas de texto
    commentstyle=\color{gray},     % Color de los comentarios
    numbers=left,                   % Números de línea en la izquierda
    numberstyle=\tiny\color{black}, % Estilo de los números de línea
    breaklines=true,                % Romper líneas largas automáticamente
    frame=trBL,
    frameround=fttt,                   % Colocar un marco alrededor del código
    rulecolor=\color{black},        % Color del marco
    backgroundcolor=\color{white}, % Color de fondo del bloque de código
    captionpos=b,                   % Posición de los títulos
}
```
