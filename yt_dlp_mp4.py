import yt_dlp
import os
import subprocess

def descargar_video(url):
    # Opciones para yt-dlp, se descarga el mejor video y el mejor audio disponible
    opciones = {
        'format': 'bestvideo+bestaudio/best',  # Descargar el mejor video y audio disponible
        'outtmpl': 'Video_descargado.%(ext)s',
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        try:
            info = ydl.extract_info(url, download=True)
            video_name = f"Video_descargado.{info['ext']}"
            print(f"Video descargado: {video_name}")
            return video_name
        except Exception as e:
            print(f"Error al descargar el video: {e}")
            return None

def convertir_a_avi(video_name):
    if video_name is None:
        return

    try:
        # Obtener la ruta completa del archivo descargado
        video_path = os.path.abspath(video_name)  # Ruta completa del archivo
        print(f"Ruta completa del archivo: {video_path}")
        
        # Verificar si el archivo descargado realmente existe
        if not os.path.exists(video_path):
            print(f"El archivo {video_name} no se encuentra en el directorio.")
            return
        
        # Convertir el video descargado a formato AVI usando FFmpeg
        output_name = video_name.rsplit('.', 1)[0] + ".avi"  # Cambiar la extensión a .avi
        output_path = os.path.abspath(output_name)  # Ruta absoluta del archivo de salida
        print(f"Convirtiendo {video_path} a {output_path}...")
        
        # Ejecutar FFmpeg con la ruta completa del archivo
        result = subprocess.run(
            ['ffmpeg', '-i', video_path, output_path],
            check=True, capture_output=True, text=True
        )
        
        # Ver la salida del comando FFmpeg
        print(f"FFmpeg salida:\n{result.stdout}")
        print(f"FFmpeg errores (si los hay):\n{result.stderr}")
        
        print(f"Video convertido a AVI: {output_path}")
        os.remove(video_path)  # Eliminar el video descargado (previo a la conversión)
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir el video: {e}")
        print(f"Detalles del error: {e.stderr}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del video: ").strip()
    video_name = descargar_video(url)
    convertir_a_avi(video_name)