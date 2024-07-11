# YouTube Subtitle Extractor

This script extracts subtitles from a YouTube video and saves them to a text file.

## Installation

1. Clone this repository:
   - `git clone <repository_url>`
   - `cd <repository_directory>`

2. Create and activate a virtual environment:
   - `python -m venv myenv`
   - `.\myenv\Scripts\activate`

3. Install the required package:
   - `pip install youtube_transcript_api`

## Usage

The script can be run with the following command:

`python getText.py <video_URL> [<output_file>] [<language>]`

### Arguments

- `<video_URL>`: The URL of the YouTube video to extract subtitles from.
- `<output_file>`: (Optional) The name of the file to save the subtitles to. Defaults to `output.txt`.
- `<language>`: (Optional) The language code of the subtitles. Defaults to `es` (Spanish).

### Examples

1. Show help:
   - `python getText.py --help`

2. Extract subtitles with default output file and language:
   - `python getText.py "https://www.youtube.com/watch?v=U23lNFm_J70&ab_channel=midulive"`

3. Extract subtitles with specified output file and language:
   - `python getText.py "https://www.youtube.com/watch?v=U23lNFm_J70&ab_channel=midulive" "subtitles.txt" "es"`

## Notes

- The script defaults to extracting subtitles in Spanish (`es`). You can specify a different language code if needed.
- Make sure the YouTube video has subtitles available in the specified language.
