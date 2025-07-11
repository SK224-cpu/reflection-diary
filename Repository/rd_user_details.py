import BusinessEntities.UserBusinessEntity as User

class UserDetails:
    def __init__(self, conn):
        self.conn = conn

    def create_user(self, u:User):
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO rd_user_details (
            user_name,password, email_id, user_creation_date, user_status, role, user_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning user_id""",
                        (u.user_name,u.password, u.email_id, u.user_creation_date, u.user_status, u.role, u.user_id))

            new_user = cur.fetchone()[0]
        self.conn.commit()
        return new_user

    def update_user(self, u:User, user_id):
        with self.conn.cursor() as cur:
            cur.execute("""Update user_details set user_name=%,password=%, email_id=%, user_creation_date=%, 
            user_status=%, role=% where user_id = %s """, (u.user_name,u.password, u.email_id, u.user_creation_date, u.user_status, u.role))
        self.conn.commit()