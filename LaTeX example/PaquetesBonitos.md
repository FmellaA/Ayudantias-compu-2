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
    literate={á}{{\'a}}1
        {ã}{{\~a}}1
        {é}{{\'e}}1
        {ó}{{\'o}}1
        {í}{{\'i}}1
        {ñ}{{\~n}}1
        {¡}{{!`}}1
        {¿}{{?`}}1
        {ú}{{\'u}}1
        {Í}{{\'I}}1
        {Ó}{{\'O}}1
}
```
### [2] Para usar sub-archivos y un archivo principal

```latex
\usepackage{subfiles} [2]
```
Este paquete se usa creando un archivo principal, de preferencia algo como main.tex, el cual alojará todos sus paquetes y sus subfiles de la misma forma;
```latex
\documentclass{lo usual}
\usepackage{subfiles}

\begin{document}
\subfile{ruta/al/archivo} %sin el .tex
\end{document}
```
Luego de ello, la idea es trabajar el archivo por partes, como secciones o capítulos, tal que sean organizados como, en tu archivo archivo.tex, debiera verse algo como;
```latex
\documentclass[rout/to/main.tex]{subfiles}

\begin{document}

Lorem ipsum

\end{document}
```
Con lo cual su documento podrá ser compilado en su totalidad y además se modficiado por secciones según se ordene.
### [3] TikZ para crear imágenes vectoriales en LaTeX
Este paquete es súmanente útil a la hora de crear imágenes simples de caracter vectorial, como es usual en programas como Inkscape, sin embargo, su curva de aprendizaje es algo empinada, se recomienda buscar un tutorial de como usarlo en youtube o en internet, les dejo un ejemplo de una figura simple creada con TikZ.
```latex
\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1.0]
    % Dibujar la barra
    \fill[blue!30] (0,0) rectangle (4,0.3);
    \draw[thick] (0,0) rectangle (4,0.3);
    
    % Marcar los extremos
    \draw[thick] (0,0) -- (0,-0.1);
    \draw[thick] (4,0) -- (4,-0.1);
    
    % Etiquetas de posición
    \node[below] at (0,-0.1) {-m};
    \node[below] at (4,-0.1) {m};
    
    % Indicar la longitud
    \draw[<->, thick] (0,-0.7) -- node[below] {Longitud $L = 2$m} (4,-0.7);
    
    % Etiqueta de densidad
    \node at (2,0.7) {Densidad lineal $\sigma = \frac{m}{L} = \frac{1}{2}$ kg/m};
    
    % Eje coordenado
    \draw[->, thick] (-0.5,0.15) -- (4.5,0.15) node[right] {$x$ (m)};
    
    % Masa total
    \node at (2,-2.0) {Masa total: $m = \sigma \cdot L = \frac{1}{2} \cdot 2 = 1$ kg};
\end{tikzpicture}
\caption{Barra uniforme de longitud $L = 2$ m con densidad lineal constante $\sigma = \frac{1}{2}$ kg/m.}
\label{fig:barra_uniforme}
\end{figure}
```
Abran un documento de LaTeX y añadan el siguiente preámbulo;
```latex
\usepackage{tikz} [3]
```
