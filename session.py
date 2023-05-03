import main
import connections

class sessionAuth:

    def checkAuthentication(self):
        username = self.loginUsername.text().lower()
        password = self.loginPassword.text().lower()
        conn = connections.conndb()
        strsql = f"SELECT * FROM adminusers WHERE adminUsername = '{username}' and adminPassword='{password}'"
        result = conn.queryResult(strsql)

        if result:
            return "Approved"
        else:
            self.txtLoginError.show()
            self.txtLoginError.setText(" Wrong Username/Password ")
            self.txtPasswordError.show()
            self.txtUserError.show()

    def sessionUser(self):
        username = self.loginUsername.text()
        password = self.loginPassword.text()
        if username == "user" and password == "password":
            username = str(self.loginUsername.text())
            return ("Something")
        

       



