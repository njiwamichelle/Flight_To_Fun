"""The questionnaire, the destinations, and the rules for who wins what."""

# type "text"   -> the user types anything (name, age)
# type "choice" -> multiple choice, click an option
QUESTIONS = [
    {"key": "name", "type": "text", "max": 24,
     "text": "First, what is your name?"},
    {"key": "age", "type": "text", "max": 3,
     "text": "How old are you?"},
    {"key": "interests", "type": "choice",
     "text": "Which of these best describes your interests?",
     "options": [
         "I enjoy the water and the ocean",       # -> Maldives
         "I like thrifty, trendy items",          # -> Thailand
         "I love historical sightseeing",         # -> England
         "I love to relax and get pampered",      # -> Maldives + bonus Japan
     ]},
    {"key": "hobbies", "type": "choice",
     "text": "What is your favorite kind of hobby?",
     "options": [
         "Swimming, snorkeling or surfing",
         "Shopping and trying new foods",
         "Reading, museums and photography",
         "Spa days, yoga and meditation",
     ]},
    {"key": "enjoy", "type": "choice",
     "text": "What do you enjoy most on a normal weekend?",
     "options": [
         "Being outdoors in the sun",
         "Browsing markets and vintage shops",
         "Visiting castles, landmarks or old towns",
         "Doing absolutely nothing at all",
     ]},
    {"key": "family", "type": "choice",
     "text": "How big is your family (who is coming along)?",
     "options": [
         "Just me",
         "2 people",
         "3 to 4 people",
         "5 or more people",
     ]},
    {"key": "recent", "type": "choice",
     "text": "What is the most recent place you traveled?",
     "options": [
         "A beach or island",
         "A big, busy city",
         "Somewhere in the countryside",
         "I have not traveled in a long time",
     ]},
    {"key": "lookforward", "type": "choice",
     "text": "What do you look forward to most on your trip?",
     "options": [
         "The food",
         "The sights and scenery",
         "Making memories with people I love",
         "Total rest and relaxation",
     ]},
    {"key": "why", "type": "choice",
     "text": "Why do you want to take this trip?",
     "options": [
         "To celebrate something special",
         "To escape and recharge",
         "To explore and learn something new",
         "Just for fun!",
     ]},
]

DESTINATIONS = {
    "maldives": {
        "name": "The Maldives",
        "tagline": "Crystal lagoons, coral reefs and overwater bungalows",
        "blurb": ("Snorkel with manta rays, dive over glowing coral reefs and "
                  "sleep in a bungalow built right on the turquoise water. "
                  "Best time to visit: November to April."),
        "image": "maldives",
    },
    "thailand": {
        "name": "Thailand",
        "tagline": "Night markets, golden temples and street food",
        "blurb": ("Hunt for trendy finds at the Bangkok night markets, ride a "
                  "longtail boat, eat pad thai from a street cart and visit "
                  "golden temples. Best time to visit: November to February."),
        "image": "thailand",
    },
    "england": {
        "name": "England",
        "tagline": "Castles, palaces and centuries of history",
        "blurb": ("See Big Ben and Buckingham Palace, wander the Tower of "
                  "London, visit Stonehenge and ride a red double-decker "
                  "bus. Best time to visit: May to September."),
        "image": "england",
    },
    "japan": {
        "name": "Japan  (BONUS TRIP!)",
        "tagline": "Hot springs, temples, cherry blossoms and Mount Fuji",
        "blurb": ("Soak in a traditional onsen, stay at a ryokan inn, stroll "
                  "past pagodas under cherry blossoms and see Mount Fuji. "
                  "Best time to visit: March to May or October to November."),
        "image": "japan",
    },
}

FAMILY_LINES = {
    0: "your solo adventure",
    1: "you and your travel buddy",
    2: "your family of 3 to 4",
    3: "your big family of 5 or more",
}


def destinations_for(interest_index):
    """Return the list of trips won, based on the choice picked for 'interests'."""
    if interest_index == 0:      # water and ocean
        return ["maldives"]
    if interest_index == 1:      # thrifty, trendy items
        return ["thailand"]
    if interest_index == 2:      # historical sightseeing
        return ["england"]
    return ["maldives", "japan"]  # relax and get pampered -> Maldives + bonus Japan