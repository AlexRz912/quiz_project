from user import User

u = User("royal_blood", 80)
u.users_data = u.json_load_user_if_exists()
u.json_save_user()
