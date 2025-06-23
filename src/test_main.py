import sys
import pytest
from main import main  # On importe la fonction principale à tester

def test_main(capsys):
    
    # Redirige la sortie standard pour capturer les prints
    sys.stdin = open('src/test_input.txt', 'r')  # On simule l'entrée utilisateur depuis un fichier

    main()  # Appelle la fonction principale

    captured = capsys.readouterr()  # Capture la sortie standard

    # Vérifie que le message de bienvenue est affiché
    assert "Bonjour" in captured.out
    
    # Vérifie que les entrées utilisateur sont traitées correctement
    assert "Vous avez dit : test" in captured.out
    assert "Bien dit !" in captured.out  # Pour un palindrome comme "test"

    # Vérifie que le message de sortie est affiché
    assert "Au revoir" in captured.out


# --- COMMENT LANCER LES TESTS ---
# 1. Installe pytest si besoin : pip install pytest
# 2. Place ce fichier dans le même dossier que main.py
# 3. Ouvre un terminal dans ce dossier (Shift + clic droit > "Ouvrir une fenêtre de commande ici")
# 4. Lance la commande suivante :
#    pytest test_main.py
# 5. Lis le résultat dans le terminal : chaque test doit s'afficher comme "passed" s'il réussit.