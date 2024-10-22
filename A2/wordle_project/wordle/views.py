from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from random import choice

WORDS = ["apple", "bread", "grape", "plane", "house"]  # You can expand this list

def index(request):
    word = request.session.get('word')  # Get the word stored in session
    guesses = request.session.get('guesses', [])
    message = ""

    if request.method == "POST":
        guess = request.POST.get('guess').lower()
        
        # Check if it's a valid guess
        if len(guess) != 5 or guess not in WORDS:
            message = "Invalid guess! Must be a 5-letter word."
        else:
            # Check if the guess is correct
            if guess == word:
                message = "You got it!"
                request.session.flush()  # Clear the session and reset the game
            else:
                guesses.append(guess)
                request.session['guesses'] = guesses

    # Generate a new word if none exists in session
    if not word:
        word = choice(WORDS)
        request.session['word'] = word

    context = {
        'word': word,
        'guesses': guesses,
        'message': message,
    }

    return render(request, 'wordle/index.html', context)
