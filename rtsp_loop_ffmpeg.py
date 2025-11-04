import os
import subprocess
import sys



video = "Untitled.mov"

# Loop playback forever (-stream_loop -1) and stream via RTSP
cmd = [
    "ffmpeg",
    "-re",
    "-stream_loop", "-1",
    "-i", video,
    "-c:v", "libx264",
    "-f", "rtsp",
    "-rtsp_flags", "listen",
    "-rtsp_transport", "tcp",
    "rtsp://0.0.0.0:8554/stream"
]

print("Starting RTSP stream at rtsp://localhost:8554/stream")
subprocess.run(cmd)