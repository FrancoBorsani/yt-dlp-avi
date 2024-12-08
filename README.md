# yt-dlp-avi

Software que utiliza el paquete "yt_dlp" e integra "ffmpeg" para convertir a .avi el video obtenido.
Se incluye un setup para poder generar un archivo ejecutable y que el programa pueda ser utilizado desde cualquier equipo.

Para generar el ejecutable para cualquier usuario se utilizó el biblioteca "cx_Freeze". La misma integra la herramienta "ffmpeg" para que no haga falta tenerla instalada.

> [!Important]
> Comando para crear archivo ejecutable a partir del código y de la configuración establecida.

```
python build_setup.py build
```

> [!Important]
> Paquetes utilizados para el desarrollo.

```
python -m pip install cx_Freeze

python -m pip install yt-dlp
```
