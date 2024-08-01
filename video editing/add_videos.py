import subprocess


def fix_fps(initial_video, final_video, fps):
    command = [
        "ffmpeg",
        "-i", initial_video,
        "-filter:v", f"fps={fps}",
        "-c:v", "libx264",
        "-preset", "fast",
        "-c:a", "libopus",
        "-b:a", "192k",
        final_video,
        "-f", "mp4"
    ]
    subprocess.run(command, check=True)

video_1 = r'C:\vs code projects\new project\video editing\landscape_video.mp4'
final_video_1 = r"video editing/fixedLandscapeVideo.mp4"

video_2 = r'C:\vs code projects\new project\video editing\NewLandscapeVideo.mp4'
final_video_2 = r"video editing/fixedNewLandScapeVideo.mp4"


fix_fps(video_1, final_video_1, 25)
fix_fps(video_2, final_video_2, 25)


def add_videos(video_file, final_video_path):
    command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", video_file,
        "-fps_mode", "cfr",
        "-c", "copy",
        final_video_path
    ]

    subprocess.run(command, check=True)