ffmpeg -i clip.mp4 \
  -vcodec libx264 -crf 30 -preset slow \
  -c:a aac -b:a 128k \
  clip_compressed.mp4
