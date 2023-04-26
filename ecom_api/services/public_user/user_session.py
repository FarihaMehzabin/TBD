import uuid, traceback
from ecom_api.services.hashing import Hashing
from ecom_api.models.data_table_models.public_user.create_user_session_result import CreateUserSessionResultDataModel
from ecom_api.models.data_table_models.public_user.check_user_session_result import CheckUserSessionResultDataModel
from ecom_api.db.user_session_db import UserSessionDB

class UserSessionService:
    def __init__(self):
        self.hash = Hashing()
        self.user_session_db = UserSessionDB()

    def create_session(self, user_id):
        guid_id = str(uuid.uuid4())
        hashed_guid = self.hash.hash_guid(guid_id)

        if self.user_session_db.create_session(hashed_guid, user_id):
            response = CreateUserSessionResultDataModel(hashed_guid)
            return response
        else:
            return False

    def check_session_user(self, guid):
        data = self.user_session_db.get_session_by_guid(guid)

        if data:
            user_id = data[1]

            user_data = self.user_session_db.get_user_by_id(user_id)
            if user_data:
                response = CheckUserSessionResultDataModel(True, user_data[0] + user_data[1], user_id)
                return response

        return CheckUserSessionResultDataModel(False, 'No user found')