import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Specify the folder containing the videos
input_folder = 'C:/Users/4a Freeboard/Videos/VideosFol/'
output_folder = "C:/Users/4a Freeboard/Videos/"
output_filename = 'Concadinate_video.mp4'

# Get a list of all video files in the input folder
video_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

# Sort the video files (optional, depending on desired order)
video_files.sort()

# Load all video files as VideoFileClip objects
video_clips = [VideoFileClip(video) for video in video_files]

# Concatenate all video clips
final_clip = concatenate_videoclips(video_clips)

# Save the final concatenated video to the output folder
final_clip.write_videofile(os.path.join(output_folder, output_filename))

# Close all clips to release resources
for clip in video_clips:
    clip.close()
