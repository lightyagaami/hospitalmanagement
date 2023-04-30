from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer


from controllers.database.db_controller import db
from views.appointmentWindow import AppointmentWindow


class User:
    def insertData(self):
        try:
            print("dans le insert data")
            conn = db.createConnection(self)
            cursor = conn.cursor()
            sql = "INSERT INTO hospita_system.users (username,password,email,contact,address) VALUES (%s, %s, %s, %s, %s)"
            values = (self.username_edit.text(), self.password_edit.text(),
                      self.email_edit.text(), self.phone_edit.text(), self.address_edit.text())
            cursor.execute(sql, values)
            conn.commit()
            self.close()
        except (Exception) as e:
            print(e)
            conn.rollback()

    def loginUser(self):
        conn = db.createConnection(self)
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM hospita_system.users WHERE username=%s AND password=%s"
            values = (self.input1.text(), self.input2.text())
            cursor.execute(sql, values)
            result = cursor.fetchone()
            if result:
                print("User logged successfully !")
                # recuperer l'ID de l'utilisateur connecté
            #  id_user = result[0]

                # clean les zones de saisies
                self.input1.clear()
                self.input2.clear()

                # masquer la fenetre actuelle
                self.close()

                # aller au dashboard
                self.doctor_page = AppointmentWindow()
                self.doctor_page.show()
            else:
                print("Invalid email or password")
                self.error_lbl.setText("Email ou mot de passe incorrect")
                font = QFont('Arial', 12)
                self.error_lbl.setFont(font)
                self.error_lbl.setStyleSheet("color: red;")
                self.error_lbl.setAlignement(Qt.AlignmentFlag.AlignCenter)

                # clean les zones de saisies
                self.login_input.clear()
                self.password_inpu.clear()

                # retirer les erreurs text apres 10s
                timer = QTimer(self)
                timer.setSingleShot(True)
                timer.timeout.connect(lambda: self.error_lbl.setText(""))
                timer.start(10000)
        except (Exception) as e:
            print("error: " + str(e))
