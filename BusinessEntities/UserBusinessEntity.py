class UserBusinessEntity:
    def __init__(self,
user_name, password, email_id, user_creation_date, user_status, role, user_id=None):

        self.user_id =user_id
        self.user_name = user_name
        self.password = password
        self.email_id = email_id
        self.user_creation_date = user_creation_date
        self.user_status = user_status
        self.role = role

