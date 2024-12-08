from cx_Freeze import setup, Executable
import os

# Ruta a FFmpeg
ffmpeg_bin_path = os.path.join("ffmpeg/bin")

build_options = {
    'packages': ['yt_dlp'],
    'include_files': [(os.path.join(ffmpeg_bin_path, "ffmpeg.exe"), "ffmpeg.exe")],
}

setup(
    name="Descargador de Videos de YouTube",
    version="1.0",
    description="Descargador de videos en formato MP4 desde YouTube.",
    options={'build_exe': build_options},
    executables=[Executable("yt_dlp_mp4.py")],
)