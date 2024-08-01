#I wanted to add multiple videos together
#but I am yet to understand how to actually do it
#oh well guess it's more searching then
#aka give up and ask chat-gpt


import add_videos
import watermark 
import add_frame
from datetime import date


#used for adding 2 videos together
videos_file = r"video editing/videos.txt"
merged_video = r"video editing/phone_video.mp4"

#used for adding the border with text
boardered_video_path = r"video editing/framed_video.mp4"
text = str(date.today())
text_size = 50
text_color = "white"
x = "(w-text_w)/2"
y = "(h-text_h) - 10"
border_size = 50


#used for adding the watermark
watermark_path = r"video editing/Screenshot 2023-12-23 215257.png"
final_video_path = r"video editing/FinalVideo.mp4"
position = "(main_w-overlay_w)/2:(main_h-overlay_h)/2"
opacity = 0.5
scaling = 0.05

if __name__ == "__main__":
    add_videos.add_videos(videos_file, merged_video)
    print("videos merged successfully!!")

    add_frame.add_border(merged_video, boardered_video_path, text, text_color, text_size, border_size, x, y)
    print("border added successfully!!")

    watermark.add_watermark(boardered_video_path, watermark_path, final_video_path, opacity, position, scaling)
    print("watermark added successfully!!")

