import time
import webbrowser
import random
import string
from urllib.parse import urlparse, parse_qs, urlencode
from fake_useragent import UserAgent

class ViewSimulator:
    def __init__(self):
        self.ua = UserAgent()
        self.settings = {
            'min_watch_time': 3,
            'max_watch_time': 10,
            'min_interval': 3,
            'max_interval': 10,
            'max_views_per_run': 100
        }

    def validate_youtube_url(self, url):
        """Validate YouTube URL format"""
        youtube_domains = ['youtube.com', 'www.youtube.com', 'youtu.be', 'www.youtu.be']
        parsed = urlparse(url)
        
        if parsed.netloc not in youtube_domains:
            return False
        if 'youtube.com' in parsed.netloc and 'watch?v=' not in parsed.query:
            return False
        if 'youtu.be' in parsed.netloc and not parsed.path[1:]:
            return False
        return True

    def generate_random_parameters(self, video_id):
        """Generate random URL parameters to make each view appear unique"""
        return {
            'v': video_id,
            't': str(random.randint(0, 30)),
            'ab': ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
            'feature': random.choice(['share', 'youtu.be', '']),
            'pp': random.choice(['', 'ygU']),
        }

    def get_video_id(self, url):
        """Extract video ID from URL"""
        parsed = urlparse(url)
        if 'youtu.be' in parsed.netloc:
            return parsed.path[1:]
        return parse_qs(parsed.query).get('v', [''])[0]

    def simulate_view(self, video_url, view_count):
        """Main simulation method"""
        if not self.validate_youtube_url(video_url):
            raise ValueError("Invalid YouTube URL")

        video_id = self.get_video_id(video_url)
        
        for i in range(view_count):
            try:
                params = self.generate_random_parameters(video_id)
                unique_url = f"https://www.youtube.com/watch?{urlencode(params)}"
                
                webbrowser.open_new_tab(unique_url)
                watch_time = random.randint(
                    self.settings['min_watch_time'],
                    self.settings['max_watch_time']
                )
                time.sleep(watch_time)
                
                if i < view_count - 1:
                    interval = random.randint(
                        self.settings['min_interval'],
                        self.settings['max_interval']
                    )
                    time.sleep(interval)
                    
            except Exception as e:
                print(f"Error occurred: {e}")
                time.sleep(60)