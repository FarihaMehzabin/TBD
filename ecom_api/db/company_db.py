from services.db_functions import DbFunctions 
from services.hashing import Hashing
import traceback

class CompanyDB:
    def __init__(self):
        self.db = DbFunctions()
        self.hash = Hashing()

    def get_company_by_username(self, username):
        res = self.db.fetch(f"SELECT * FROM company WHERE username = '{username}'")
        return res[0] if res else None
    
    def create_company_user(self, company):
        try:
            hashed_pass = self.hash.hash_pass(company.password)

            rowcount, id = self.db.insert(
                f"INSERT INTO company (name, username, password) VALUES (%s, %s, %s)",
                (company.company, company.username, hashed_pass),
            )
            return rowcount, id
        
        except Exception as err:
            print(traceback.format_exc())
            print(f"{err}")
            return None, None
    