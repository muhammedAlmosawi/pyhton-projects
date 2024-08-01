import subprocess


def get_video_dimensions(video_path):
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        '-of', 'csv=p=0',
        video_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    output = result.stdout.decode('utf-8').strip().split(',')
    width = int(output[0])
    height = int(output[1])
    return width, height


def add_border(video_path, new_video_path, text, text_color, text_size, border_size, x, y):
    width, height = get_video_dimensions(video_path)

    new_width = width + 2 * border_size
    new_height = height + 2 * border_size

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"pad={new_width}:{new_height}:{border_size}:{border_size}, drawtext=text='{text}':fontcolor={text_color}:fontsize={text_size}:x={x}:y={y}",
        "-c:a", "copy",
        new_video_path
    ]

    subprocess.run(command)
