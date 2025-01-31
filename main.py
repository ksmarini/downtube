import yt_dlp
import argparse
import os

def parse_arguments():
    """Configura e retorna os argumentos da linha de comando."""
    parser = argparse.ArgumentParser(description="Baixar vídeos do YouTube usando yt_dlp.")
    parser.add_argument('url', type=str, help="URL do vídeo ou playlist do YouTube")
    parser.add_argument('--output_dir', type=str, default='downloads', help="Diretório de saída")
    parser.add_argument('--audio-only', action='store_true', help="Baixar apenas o áudio em MP3")
    parser.add_argument('--playlist', action='store_true', help="Baixar todos os vídeos de uma playlist")
    return parser.parse_args()

def download_video(url, output_dir, audio_only=False, playlist=False):
    """Baixa um vídeo ou playlist do YouTube."""
    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else 'best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': not playlist,  # Se `playlist=False`, baixa apenas um vídeo
    }

    if audio_only:
        ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Erro ao baixar: {e}")

def main():
    """Função principal do script."""
    args = parse_arguments()  # Chama a função que processa os argumentos

    os.makedirs(args.output_dir, exist_ok=True)  # Garante que a pasta de saída existe

    download_video(args.url, args.output_dir, args.audio_only, args.playlist)

if __name__ == "__main__":
    main()
