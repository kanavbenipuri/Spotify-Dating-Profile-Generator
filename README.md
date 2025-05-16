# Spotify Dating Profile Generator

A fun Python application that generates a dating profile based on your Spotify listening history. The app analyzes your top artists and assigns you a "dateability score" based on predefined red and green flag artists.

## Features

- Connects to your Spotify account to fetch your top artists
- Calculates a dateability score based on your music taste
- Identifies potential red and green flags in your music preferences
- Provides a detailed dating profile with scores and feedback

## Prerequisites

- Python 3.6 or higher
- A Spotify account
- Spotify Developer credentials (Client ID and Client Secret)

## Installation

1. Clone the repository or download the source code

2. Install the required packages:
```bash
pip install spotipy
```

3. Set up your Spotify Developer credentials:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Get your Client ID and Client Secret
   - Set the redirect URI to `http://localhost:8888/callback`

4. Create a `.env` file in the project root with your Spotify credentials:
```plaintext
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
SPOTIFY_SCOPE=user-top-read
```

Note: Make sure to keep your `.env` file private and never commit it to version control.

## Usage

Run the application using Python:

```bash
python spotify_dating.py
```

Follow the prompts to:
1. Authenticate with your Spotify account
2. Enter your gender
3. View your dating profile based on your music taste

## How It Works

The application:
1. Fetches your top artists from Spotify
2. Compares them against predefined lists of red and green flag artists
3. Calculates a dateability score based on matches
4. Generates a detailed profile with your score and feedback

## Project Structure

- `spotify_api.py`: Handles Spotify API authentication and data fetching
- `spotify_dating.py`: Main application logic and dating profile generation

## Note

This is a fun project and shouldn't be taken too seriously! The red and green flag artists are arbitrarily chosen and are meant to be entertaining rather than a serious judgment of anyone's dating potential.

