import subprocess


def get_video_dimensions(video_path):
    command = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-of", "csv=s=x:p=0",
        video_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout.strip().split('x')
    width, height = map(int, output)
    return width, height

def add_watermark(original_video_path, watermark_path, new_video_path, opacity, position, scale_factor):
    video_width, video_height = get_video_dimensions(original_video_path)

    scale_factor = 0.5
    video_width = int(video_width) * scale_factor
    video_height = int(video_height) * scale_factor

    if video_width == 0 or video_height == 0:
        print("Invalid overlay dimensions. Scale factor might be too small.")
        return 
    

    command = [
        "ffmpeg",
        "-i", original_video_path,
        "-i", watermark_path,
        "-filter_complex", f"[1]scale={video_width}:{video_height}[ovr];[ovr]format=rgba,colorchannelmixer=aa={opacity}[watermark];[0][watermark]overlay={position}",
        "-c:a", "copy",
        new_video_path
    ]

    subprocess.run(command, check=True)
