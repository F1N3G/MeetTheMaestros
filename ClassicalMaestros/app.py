import os
import logging
from flask import Flask, render_template

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "classical-music-secret-key")

# Composer data with biographical information and key compositions
composers_data = {
    'mozart': {
        'name': 'Wolfgang Amadeus Mozart',
        'period': 'Classical Period',
        'birth_death': '1756-1791',
        'portrait': 'https://pixabay.com/get/g5504eb0374d523887d46b214850dd4c802b85712214166b25dc5b586a7228f8ee9d97121c7a58d0f336b1c10d5c6bfcf_1280.jpg',
        'biography': 'Wolfgang Amadeus Mozart was an Austrian composer and child prodigy who began composing at age five. He created over 600 works during his short 35-year life, including symphonies, operas, and chamber music. His music perfectly embodies the Classical style with its clarity, balance, and formal perfection. Mozart\'s genius lay in his ability to combine technical mastery with profound emotional expression.',
        'key_compositions': [
            'Symphony No. 40 in G minor',
            'The Magic Flute (Die Zauberflöte)',
            'Piano Concerto No. 21',
            'Requiem Mass in D minor',
            'The Marriage of Figaro'
        ],
        'youtube_embed': 'https://www.youtube.com/embed/JTc1mDieQI8'
    },
    'beethoven': {
        'name': 'Ludwig van Beethoven',
        'period': 'Classical/Romantic Period',
        'birth_death': '1770-1827',
        'portrait': 'https://pixabay.com/get/g72b66e10ed8b4530da4933b29a62e0bd29214025a718c682937edab15ede9ab8d9258e1ced05865e014267b4732bbdcf_1280.jpg',
        'biography': 'Ludwig van Beethoven was a German composer who bridged the Classical and Romantic periods of Western music. Despite losing his hearing in his twenties, he continued to compose some of the most powerful and influential music ever written. His works expanded the scope and emotional range of classical music, inspiring generations of composers. Beethoven\'s legacy includes nine symphonies, numerous piano sonatas, and string quartets that remain cornerstones of the classical repertoire.',
        'key_compositions': [
            'Symphony No. 9 "Choral"',
            'Symphony No. 5',
            'Moonlight Sonata',
            'Piano Concerto No. 5 "Emperor"',
            'Fidelio Opera'
        ],
        'youtube_embed': 'https://www.youtube.com/embed/t3217H8JppI'
    },
    'bach': {
        'name': 'Johann Sebastian Bach',
        'period': 'Baroque Period',
        'birth_death': '1685-1750',
        'portrait': 'https://pixabay.com/get/g8c2fc055d491afd07783be5ca205f8b5003a543730742da2654afb4b1f11d9ba6dc133ad10ba589c3f8105f4cf9601a2d74527bb52218a2adce2b8e5e137508a_1280.jpg',
        'biography': 'Johann Sebastian Bach was a German composer and organist of the Baroque period, widely regarded as one of the greatest composers of all time. He mastered virtually every musical form of his era and created works of extraordinary technical complexity and spiritual depth. Bach\'s music demonstrates perfect mathematical structure combined with profound emotional expression. His influence on subsequent generations of composers cannot be overstated, earning him the title "the father of modern music."',
        'key_compositions': [
            'Brandenburg Concertos',
            'The Well-Tempered Clavier',
            'Mass in B minor',
            'Goldberg Variations',
            'Toccata and Fugue in D minor'
        ],
        'youtube_embed': 'https://www.youtube.com/embed/ho9rZjlsyYY'
    },
    'tchaikovsky': {
        'name': 'Pyotr Ilyich Tchaikovsky',
        'period': 'Romantic Period',
        'birth_death': '1840-1893',
        'portrait': 'https://pixabay.com/get/ge1ab3d08197ceb018b66c688ccc3acf8ec6692a6c4397309ba20de7487f074733a1bd1946ab55232bb08612985042cc776948dcb1d31c952aa498313134998d3_1280.jpg',
        'biography': 'Pyotr Ilyich Tchaikovsky was a Russian composer whose music perfectly captured the emotional intensity of the Romantic era. Known for his lush orchestrations and memorable melodies, he created some of the most beloved works in classical music. His ballets, symphonies, and concertos remain staples of concert halls worldwide. Tchaikovsky\'s ability to convey deep emotion through music has made his works eternally popular with audiences of all ages.',
        'key_compositions': [
            'Swan Lake Ballet',
            'The Nutcracker Ballet',
            'Symphony No. 6 "Pathétique"',
            'Piano Concerto No. 1',
            '1812 Overture'
        ],
        'youtube_embed': 'https://www.youtube.com/embed/BDHz7g3cK0Y'
    },
    'chopin': {
        'name': 'Frédéric Chopin',
        'period': 'Romantic Period',
        'birth_death': '1810-1849',
        'portrait': 'https://pixabay.com/get/g52d6ffcee1c25420363632e9b173602f5d737e161b4863001bfa285ec735014d98b4d8b64e2440e9d9c48bfd8da6f1d75a99379f1764ddafe98bf4163f401c4b_1280.jpg',
        'biography': 'Frédéric Chopin was a Polish composer and virtuoso pianist of the Romantic era, known primarily for his solo piano works. His compositions are characterized by their poetic expressiveness, technical brilliance, and innovative harmonic language. Chopin expanded the possibilities of piano music, creating works that are both technically challenging and emotionally profound. His influence on piano composition and performance technique continues to this day, making him one of the most important figures in piano literature.',
        'key_compositions': [
            'Nocturnes',
            'Études Op. 10 and Op. 25',
            'Ballades',
            'Piano Concerto No. 1',
            'Polonaise in A-flat major'
        ],
        'youtube_embed': 'https://www.youtube.com/embed/9E6b3swbnWg'
    }
}

@app.route('/')
def index():
    """Main page displaying all composers"""
    return render_template('index.html', composers=composers_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
