

class LoginController:
    def __init__(self):
        # initialiser les données d'utilisateurs
        self.users = {
            'user': 'user',
            'user2': 'password2',
            'user3': 'password3'
        }

    def login(username, password):
        # vérifier si le nom d'utilisateur et le mot de passe sont valides
        if username == 'user' and password == 'user':
            # Connexion réussie, retourner True
            return True
        else:
            # Connexion échouée, retourner False
            return False
