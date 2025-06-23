import locale
from datetime import datetime

def get_system_language():
    """Récupère la langue du système"""
    try:
        current_locale = locale.getdefaultlocale()[0].lower()
        if current_locale.startswith('fr'):
            return 'fr'
        elif current_locale.startswith('es'):
            return 'es'
        else:
            return 'en'
    except:
        return 'en'

def get_greeting():
    current_hour = datetime.now().hour
    language = get_system_language()
    
    if language == 'fr':
        return "Bonjour" if current_hour < 18 else "Bonsoir"
    elif language == 'es':
        return "Buenos días" if current_hour < 12 else "Buenas tardes" if current_hour < 18 else "Buenas noches"
    else:  # English
        return "Good morning" if current_hour < 12 else "Good afternoon" if current_hour < 18 else "Good evening"

def get_goodbye():
    current_hour = datetime.now().hour
    language = get_system_language()
    
    if language == 'fr':
        if current_hour < 18:
            return "Au revoir"
        elif current_hour < 22:
            return "Bonne soirée"
        else:
            return "Bonne nuit"
    elif language == 'es':
        if current_hour < 18:
            return "Adiós"
        elif current_hour < 22:
            return "Buenas tardes"
        else:
            return "Buenas noches"
    else:
        if current_hour < 18:
            return "Goodbye"
        elif current_hour < 22:
            return "Good evening"
        else:
            return "Good night"