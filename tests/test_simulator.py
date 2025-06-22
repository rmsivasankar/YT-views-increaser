import unittest
from core.utilities import validate_youtube_url, get_video_id

class TestYouTubeUtilities(unittest.TestCase):
    def test_url_validation(self):
        self.assertTrue(validate_youtube_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        self.assertTrue(validate_youtube_url("https://youtu.be/dQw4w9WgXcQ"))
        self.assertFalse(validate_youtube_url("https://example.com"))
        self.assertFalse(validate_youtube_url("https://www.youtube.com"))
    
    def test_video_id_extraction(self):
        self.assertEqual(get_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ"), "dQw4w9WgXcQ")
        self.assertEqual(get_video_id("https://youtu.be/dQw4w9WgXcQ"), "dQw4w9WgXcQ")

if __name__ == '__main__':
    unittest.main()