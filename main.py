# QApplication est le gestionnaire d'app et QWidget est une base vide de widget GUI
# Les modules principaux pour Qt sont QtWidgets, QtGui et QtCore.

from PyQt5.QtWidgets import QApplication
import sys
from views.home import HomeWindow
from controllers.controller import LoginController

if __name__ == "__main__":
    # creation d'une instance de l'app
    app = QApplication(sys.argv)
    # Chargement des models
    model = ()
    # Chargement du controller
    controller = LoginController()
    # Chargement de la premiere vue de l'app
    view = HomeWindow(LoginController)
    # affichage de la vue par defaut de notre app car cela est masqué par defaut
    view.show()
    sys.exit(app.exec())
