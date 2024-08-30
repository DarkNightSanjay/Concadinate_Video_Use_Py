# Video Concatenation Script

This Python script concatenates all video files in a specified input folder and saves the resulting video to a specified output folder. The script uses the `moviepy` library for video processing.

## Requirements

- Python 3.x
- `moviepy` library

## Installation

1. **Clone the Repository** (if applicable) or Download the Script:
   - Clone this repository using:
     ```sh
     git clone https://github.com/your-username/your-repo.git
     ```
   - Alternatively, you can directly download the script from your preferred location.

2. **Install Required Python Packages**:
   - You can install the required Python packages using pip:
     ```sh
     pip install moviepy
     ```

## Usage

1. **Edit the Script**:
   - Modify the `input_folder` and `output_folder` variables in the script to specify the paths where your input videos are located and where you want the concatenated video to be saved.

   ```python
   input_folder = 'c:/Users/4a Freeboard/Videos/VideosFol'
   output_folder = 'C:/Users/4a Freeboard/Videos/'
   output_filename = 'Concatenated_video.mp4'


Run the Script:

After configuring the paths, run the script using Python:

      python3 Concatenate.py
      
Output:

The script will concatenate all video files in the specified input_folder and save the resulting video as Concatenated_video.mp4 in the specified output_folder.
Notes
Video Formats Supported: This script works with .mp4, .avi, .mov, and .mkv video formats. You can add more formats by modifying the file extensions in the video_files list comprehension.
Order of Concatenation: The videos are concatenated in alphabetical order by filename. You can modify this by changing how the video_files list is sorted.
Troubleshooting
ModuleNotFoundError: If you encounter ModuleNotFoundError: No module named 'moviepy', ensure that the moviepy library is installed by running pip install moviepy.
File Not Found: Ensure the input_folder path is correct and that the folder contains video files with supported extensions.
License
This project is licensed under the MIT License - see the LICENSE file for details.



### How to Use:

1. Replace the `input_folder` and `output_folder` paths with the correct paths where your videos are stored and where you want the final video to be saved.
2. Run the script in your preferred Python environment.
3. The resulting video will be saved in the output folder specified.

This `README.md` provides a clear overview of the script, how to install the necessary dependencies, how to use the script, and what to do in case of common issues.





