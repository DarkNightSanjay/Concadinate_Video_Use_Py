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
