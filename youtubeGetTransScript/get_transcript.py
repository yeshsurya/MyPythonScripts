import requests
from bs4 import BeautifulSoup

def get_youtube_transcript(video_url):
    # Fetch the YouTube video page
    response = requests.get(video_url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the transcript box element
        transcript_element = soup.find('div', {'id': 'transcript'})

        # Extract the text from the transcript box
        if transcript_element:
            transcript_text = transcript_element.get_text(separator='\n')
            return transcript_text.strip()

    return None

# Example usage
video_url = 'https://www.youtube.com/watch?v=yUISwV4LE20'
transcript = get_youtube_transcript(video_url)
if transcript:
    print(transcript)
else:
    print("Transcript not found.")
