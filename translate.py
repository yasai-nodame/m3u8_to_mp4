import ffmpeg 
import os

m3u8_file = os.environ.get('M3U8_FILE')


m3u8_input = ffmpeg.input(m3u8_file)

output = (
    ffmpeg.output(m3u8_input, 'output.mp4', c='copy')
)

# m3u8ファイルをテキストで参照した結果、tsファイルセグメントがリモートにあるので、Protocol 'https' not on whitelist 'file,crypto,data'エラーがでた。
# なので、ffmpegコマンドで、ホワイトリストコマンドを追加。
ffmpeg.run(output, cmd=['ffmpeg', '-protocol_whitelist', 'file,crypto,data,https,tls,tcp'])