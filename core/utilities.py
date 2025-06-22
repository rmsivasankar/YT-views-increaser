import time
import webbrowser
from fake_useragent import UserAgent
from .utilities import (
    validate_youtube_url,
    generate_random_parameters,
    get_video_id
)
from config.settings import DEFAULT_SETTINGS

class ViewSimulator:
    def __init__(self):
        self.ua = UserAgent()
        self.settings = DEFAULT_SETTINGS

    def simulate_view(self, video_url, view_count):
        """Simulate natural viewing behavior"""
        if not validate_youtube_url(video_url):
            raise ValueError("Invalid YouTube URL")

        if not 1 <= view_count <= self.settings['max_views_per_run']:
            raise ValueError(f"View count must be between 1 and {self.settings['max_views_per_run']}")

        video_id = get_video_id(video_url)
        results = []

        for i in range(view_count):
            try:
                # Generate unique view parameters
                params = generate_random_parameters(video_id)
                unique_url = f"https://www.youtube.com/watch?{urlencode(params)}"
                
                # Get random user agent
                headers = {'User-Agent': self.ua.random}
                
                # Calculate random durations
                watch_time = random.randint(
                    self.settings['min_watch_time'],
                    self.settings['max_watch_time']
                )
                
                # Simulate view
                browser = webbrowser.get()
                browser.open_new_tab(unique_url)
                
                # Store results
                results.append({
                    'view_number': i + 1,
                    'url': unique_url,
                    'user_agent': headers['User-Agent'],
                    'watch_time': watch_time,
                    'success': True
                })
                
                # Wait for watch time
                time.sleep(watch_time)
                
                # Random interval between views
                if i < view_count - 1:
                    interval = random.randint(
                        self.settings['min_interval'],
                        self.settings['max_interval']
                    )
                    time.sleep(interval)
                    
            except Exception as e:
                results.append({
                    'view_number': i + 1,
                    'error': str(e),
                    'success': False
                })
                time.sleep(60)
        
        return results