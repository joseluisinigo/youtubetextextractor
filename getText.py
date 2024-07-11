from youtube_transcript_api import YouTubeTranscriptApi
import sys

def get_video_id(url):
    # Extract the video ID from the YouTube URL
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL")

def save_subtitles(video_id, output_file="output.txt", language="es"):
    try:
        # Get the transcript in the specified language
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        
        # Combine the transcript text
        combined_text = " ".join([entry['text'] for entry in transcript])
        
        # Save the transcript to a text file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(combined_text)
        
        print(f"Subtitles saved to {output_file}")
    except Exception as e:
        print(f"Error retrieving subtitles: {str(e)}")

def print_help():
    help_text = """
    Usage: python getText.py <video_URL> [<output_file>] [<language>]
    
    <video_URL>       The URL of the YouTube video to extract subtitles from.
    <output_file>     (Optional) The name of the file to save the subtitles to. Defaults to 'output.txt'.
    <language>        (Optional) The language code of the subtitles. Defaults to 'es' (Spanish).
    
    Example:
    python getText.py "https://www.youtube.com/watch?v=U23lNFm_J70&ab_channel=midulive" "subtitles.txt" "es"
    """
    print(help_text)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print_help()
        sys.exit(1)
    
    video_url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.txt"
    language = sys.argv[3] if len(sys.argv) > 3 else "es"
    
    video_id = get_video_id(video_url)
    save_subtitles(video_id, output_file, language)
