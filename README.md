# Como usar o script?

### 📥 Baixar um único vídeo
```bash
python script.py "https://www.youtube.com/watch?v=VIDEO_ID"
```
### 🎵 Baixar apenas o áudio do vídeo
```bash
python script.py "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only
```
### 📂 Baixar todos os vídeos de uma playlist
```bash
python script.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist
```
### 🎶 Baixar apenas o áudio de uma playlist
```bash
python script.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist --audio-only
```
### 📌 Opções disponíveis
Argumento	Descrição	Padrão
url	URL do vídeo ou da playlist do YouTube	Obrigatório
--output_dir	Diretório de saída para salvar o arquivo	downloads/
--audio-only	Baixar apenas o áudio em MP3	False
--playlist	Baixar todos os vídeos de uma playlist	False

### 💡 Exemplo completo
Baixar apenas o áudio de uma playlist e salvar na pasta meus_audios:
```bash
python script.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist --audio-only --output_dir "meus_audios"
```
