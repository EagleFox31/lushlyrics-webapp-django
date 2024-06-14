from django.core.mail.backends.smtp import EmailBackend
from smtplib import SMTP

class CustomEmailBackend(EmailBackend):

    def open(self):
        if self.connection:
            return False

        # Préparation des paramètres de connexion
        connection_params = {
            'host': self.host,
            'port': self.port,
        }

        try:
            # Création de la connexion SMTP avec les paramètres spécifiés
            self.connection = SMTP(**connection_params)

            # Activation de TLS si spécifié dans les paramètres
            if self.use_tls:
                self.connection.ehlo()
                self.connection.starttls()
                self.connection.ehlo()

            # Authentification avec nom d'utilisateur et mot de passe si spécifié
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            
            return True
        except:
            if self.fail_silently:
                return False
            raise
