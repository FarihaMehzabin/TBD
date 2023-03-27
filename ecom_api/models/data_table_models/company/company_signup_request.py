

class CompanySignupRequestDataModel:
    def __init__(self, user):
        self.company = user["company_name"]
        self.username = user["username"]
        self.password = user["password"]
        self.error_message = None
        self.status_code = 200
        self.validate()

    def validate(self):
        try:
            if not self.username or not isinstance(self.username, str) or len(self.username) < 3:
                raise ValueError("Invalid username.")

            if not self.password or not isinstance(self.password, str) or len(self.password) < 8:
                raise ValueError("Invalid password. Password must be at least 8 characters.")
            
            if not self.first_name or not isinstance(self.company, str) or len(self.company) < 1:
                raise ValueError("Invalid company name.")
            
            
        except ValueError as e:
            self.error_message = str(e)
            self.status_code = 400
        
    
    