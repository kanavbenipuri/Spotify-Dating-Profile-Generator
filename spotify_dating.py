from spotify_api import SpotifyAPI
from typing import List, Dict


# Artist classifications based on listener demographics
RED_FLAG_ARTISTS = {
    'male': [
        'Taylor Swift', 'Olivia Rodrigo', 'Lana Del Rey',
        'Doja Cat', 
        'Ed Sheeran','Justin Bieber', 'BTS',
        'The Weeknd', 'Drake','Travis Scott','Post Malone','J. Cole'
        'Addison Rae', 'Dixie DAmelio',
        'Kanye West', 'Machine Gun Kelly', 'Eminem', 'XXXTentacion',
        'Clairo','Carseat Headrest','Juice WRLD'
        
    ],
    'female': [
        'Eminem', 'XXXTentacion','Juice WRLD'
        'Lana Del Rey','Taylor Swift', 'BTS', 'Jung Kook'
        'Doja Cat','Harry Styles',
        'Kanye West', 'Machine Gun Kelly','Anson Seabra','Sasha Alex Sloan','FINNEAS'
        ,'Laufey'
    ]
}

GREEN_FLAG_ARTISTS = {
    'male': [

        'Radiohead','Troye Sivan','The Beatles'
        'Arctic Monkeys', 'The Strokes', 'Red Hot Chili Peppers',
        
        'Kendrick Lamar', 'Tyler, The Creator',
        'Radiohead','The Smiths','Lorde',
        
        'Tame Impala', 'Mac DeMarco', 'Summer Walker', 'The Neighbourhood','Chappell Roan','bbno$'
        ,'Peter Cat Recording Co','Begum','Bruno Mars','The Japanese House'
    ],
    'female': [
        'SZA','Kendrick Lamar',
        
        'Mitski', 'Phoebe Bridgers',
        'Florence + The Machine', 'The Beatles',
        
        'HAIM', 'The 1975','Radiohead','Tame Impala',
        
        'H.E.R.', 'Summer Walker',
        'The Neighbourhood','The Smiths','Lorde',
        'Mac DeMarco','Chappell Roan','Peter Cat Recording Co','Begum','Bruno Mars','The Japanese House'
    ]
}

class SpotifyDating:
    def __init__(self):
        try:
            self.spotify = SpotifyAPI()
        except Exception as e:
            raise Exception("Failed to initialize Spotify API. Please check your credentials.") from e

    def calculate_dateability_score(self, top_artists: List[str], gender: str) -> Dict:
        """Calculate dateability score based on top artists and gender"""
        score = 50  # Base score
        red_flags = 0
        green_flags = 0

        # Count matches with red and green flag artists
        for artist in top_artists:
            if artist in RED_FLAG_ARTISTS[gender]:
                red_flags += 1
                score -= 5
            elif artist in GREEN_FLAG_ARTISTS[gender]:
                green_flags += 1
                score += 5

        # Ensure score stays within 0-100 range
        score = max(0, min(100, score))

        return {
            'score': score,
            'red_flags': red_flags,
            'green_flags': green_flags,
            'flag_status': 'GREEN' if score >= 60 else 'RED'
        }

    def get_dating_profile(self, gender: str) -> Dict:
        """Generate a dating profile based on Spotify data"""
        if not isinstance(gender, str):
            raise ValueError("Gender must be a string")
        
        gender = gender.lower()
        if gender not in ['male', 'female']:
            raise ValueError("Gender must be either 'male' or 'female'")
            
        try:
            top_artists = self.spotify.get_top_artists()
            if not top_artists:
                raise ValueError("No top artists found. Please make sure you have listening history on Spotify.")
        except Exception as e:
            raise Exception("Failed to fetch top artists from Spotify") from e
            
        results = self.calculate_dateability_score(top_artists, gender)
        
        return {
            'top_artists': top_artists[:5],  # Show top 5 artists
            'dateability_score': results['score'],
            'flag_status': results['flag_status'],
            'red_flags': results['red_flags'],
            'green_flags': results['green_flags']
        }

def main():
    try:
        print("Welcome to Spotify Dating Profile Generator!")
        print("This app will analyze your music taste and generate a dating profile.\n")
        
        # Get user's gender
        gender = input("Enter your gender (male/female): ").strip()
        while gender.lower() not in ['male', 'female']:
            print("\nError: Invalid gender input")
            print("Please enter either 'male' or 'female'")
            gender = input("Enter your gender (male/female): ").strip()

        # Initialize SpotifyDating
        spotify_dating = SpotifyDating()
        
        # Get dating profile
        profile = spotify_dating.get_dating_profile(gender)
        
        # Display results
        print("\n=== Your Dating Profile Based on Spotify ===\n")
        print(f"Top 5 Artists: {', '.join(profile['top_artists'])}")
        print(f"Dateability Score: {profile['dateability_score']}/100")
        print(f"Flag Status: {profile['flag_status']}")
        print(f"Number of Red Flags: {profile['red_flags']}")
        print(f"Number of Green Flags: {profile['green_flags']}")
        
        # Provide detailed feedback
        if profile['flag_status'] == 'GREEN':
            print("\nCongratulations! Your music taste suggests you're quite dateable!")
        else:
            print("\nYour music taste might raise some eyebrows in the dating scene...")
            
    except ValueError as e:
        print(f"\nValidation Error: {str(e)}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        print("Please make sure your Spotify credentials are properly configured.")
    finally:
        print("\nThank you for using Spotify Dating Profile Generator!")

if __name__ == "__main__":
    main()