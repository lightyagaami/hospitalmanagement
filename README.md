

Application de gestion et management d'hopital





### Fonctionnalités
1. Les utilisateurs peuvent créer leur compte utilisateur.
2. Les utilisateurs peuvent se connecter
3. Les utilisateurs peuvent prendre rendez-vous.
4. Les utilisateurs peuvent voir leurs rendez-vous dans la file d'attente.
5. Les docteurs peuvent se connecter si ils ont été ajouté par l'administrateur.


### Fichiers et répertoires
   - `controllers` - répertoire du projet.
     - `controller.py` - contient les contrôleurs qui sont chargés de la logique métier de  l'application. Dans ce cas, il s'agit du contrôleur de connexion qui vérifie les informations d'identification entrées par l'utilisateur.
     - `database` - ce fichier contient la connexion à la base de données MySQL et les fonctions d'insertion et de sélection de données pour la table "users".
   - `models` - répertoire du projet contenant quelques modèle.
     - `models.py` - ce fichier contient les classes pour les modèles de données de l'application, notamment la classe Users, la classe Doctor et la classe Appointment.
         
   - `views` - répertoire du projet contenant mes vues
     - `appointmentView.py` - affichage de la liste des rendez-vous pour un médecin, avec une interface graphique PyQt5.
     - `appointmentWindow.py` - c'est la fenêtre de prise de rendez-vous
     - `doctorLogin.py` - c'est la page de connexion pour les docteurs.
     - `popupInscription.py` - c'est une fenêtre de dialogue qui permet à un utilisateur de créer un compte en entrant ses informations personnelles
     - `home.py` -  c'est le fichier contenant la classe HomeWindow, qui est la fenêtre d'accueil de l'application. Elle permet de sélectionner si l'utilisateur est un utilisateur normal, une caissière, un docteur ou un administrateur et d'ouvrir les pages correspondantes en fonction du choix de l'utilisateur.
     - `view.py` - c'est le module contenant la définition de la classe MainWindow, qui est une sous-classe de QMainWindow. Cette classe définit l'interface utilisateur graphique (GUI) de l'application.
   - `main.py` -  C'est le point d'entrée du programme. Il importe les modules nécessaires et définit la fonction principale qui crée une instance de QApplication et initialise les différents composants de l'application tels que les modèles, les contrôleurs et les vues. Enfin, il affiche la vue par défaut de l'application et démarre la boucle principale de l'application en appelant la méthode exec() de l'instance de QApplication.


### Installation

- Vérifiez que vous avez Python 3.x installé sur votre ordinateur. Vous pouvez le vérifier en ouvrant une invite de commande `python --version`
- Vous devez installé PyQt5 sur votre ordinateur `pip install pyqt5`
- Aller dans le dossier du projet : `cd '.\HOSPITAL MANAGMENT SYSTEM\'`
- Installez les dépendances du projet en exécutant `py -m pip install -r requirements.txt`.
- Telecharger WampServer
- Importer la base de donnée "hospita_system.sql" dans phpmyadmin
- Lancer l'application avec la commande suivante : `python main.py`
