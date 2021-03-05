from pymongo import database
from bson import ObjectId


class UsersDataDriver:
    def __init__(self, db_link: database.Database):
        self.db = db_link
        self.mission_col = "users"
        self.name = 'users'

    def is_username_free(self, username):
        if self.db[self.mission_col].find_one({"username": username}):
            return False  # if username in use
        return True  # if username is free to use

    def does_email_exists(self, email):
        if self.db[self.mission_col].find_one({"email": email}):
            return 'There already is an account with that email'
        return True

    def insert_user(self, user_data):
        return self.db[self.mission_col].insert_one(user_data).inserted_id

    def get_user_by_username(self, username):
        return self.db[self.mission_col].find_one({'username': username})

    def get_user(self, user_id):
        return self.db[self.mission_col].find_one({"_id": ObjectId(user_id)})

    def get_pass_hash(self, user):
        return self.db[self.mission_col].find_one({'username': user}, {"_id": 0, "pass_hash": 1})['pass_hash']

