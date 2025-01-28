import os
import subprocess

# Define the full paths for the files
video_filename = r"C:\Users\Yashyashsvi\Downloads\sample2.mp4"
audio_filename = r"C:\Users\Yashyashsvi\Downloads\sample2song.mp3"
cropped_audio_filename = r"C:\Users\Yashyashsvi\Downloads\sample_audio.mp3"
output_filename = r"C:\Users\Yashyashsvi\Downloads\finals2.mp4"

# Ensure FFmpeg path is correct
ffmpeg_path = r"C:\Program Files\ffmpeg\ffmpeg-2025-01-05-git-19c95ecbff-full_build\bin\ffmpeg.exe"

# Step 1: Ensure both video and audio files exist
if not os.path.exists(video_filename):
    print(f"Error: Video file {video_filename} not found.")
    exit()

if not os.path.exists(audio_filename):
    print(f"Error: Audio file {audio_filename} not found.")
    exit()

# Step 2: Crop the audio between 0:11 and 0:16 seconds
start_time = "00:01:01"
end_time = "00:01:03"
print("Cropping the audio...")
subprocess.run([
    ffmpeg_path, "-i", audio_filename, "-ss", start_time, "-to", end_time, 
    "-c", "copy", cropped_audio_filename
], check=True)
print(f"Cropped audio saved as {cropped_audio_filename}")

# Step 3: Combine the video and cropped audio
print("Combining video and cropped audio...")
subprocess.run([
    ffmpeg_path, "-i", video_filename, "-i", cropped_audio_filename,
    "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", "-shortest",
    output_filename
], check=True)

print(f"Final video with cropped audio saved as {output_filename}")
