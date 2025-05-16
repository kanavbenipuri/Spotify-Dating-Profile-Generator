import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SpotifyAPI:
    def __init__(self, client_id: str = None, client_secret: str = None, redirect_uri: str = None, scope: str = None):
        """Initialize Spotify API client with credentials"""
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id or os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=client_secret or os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri=redirect_uri or os.getenv('SPOTIFY_REDIRECT_URI'),
            scope=scope or os.getenv('SPOTIFY_SCOPE')
        ))

    def get_top_artists(self, limit: int = 20) -> List[str]:
        """Get user's top artists"""
        results = self.sp.current_user_top_artists(limit=limit, time_range='medium_term')
        return [artist['name'] for artist in results['items']]