# Django REST Framework API - Vote APIView
This is a simple Django REST Framework API project that includes a custom APIView to handle voting functionality.

# Installation
Clone the repository to your local machine using git clone https://github.com/UTCH-Centinel-videogame/landing-api

Create a virtual environment using py -m venv env (for Windows) or python3 -m venv env (for Unix-based systems)

Activate the virtual environment using env\Scripts\activate (for Windows) or source env/bin/activate (for Unix-based systems)

Install the required packages using pip install -r requirements.txt

Run the migrations using python manage.py migrate

Start the development server using python manage.py runserver

# Usage
The API has one endpoint for voting, which can be accessed at http://localhost:8000/vote/. The endpoint accepts POST requests and expects the following data in the request body:
```python
{
    "gameplay": 5,
    "music": 5,
    "art": 4,
    "story": 3,
    "difficulty": 2
}
```
gameplay, music, art, story, and difficulty are required integer fields that represent the user's rating for each category.
The APIView returns a JSON response containing the average rating for each category:
```python
{
    "gameplay_avg": 5.0,
    "music_avg": 5.0,
    "art_avg": 4.0,
    "story_avg": 3.0,
    "difficulty_avg": 2.0
}
