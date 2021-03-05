from flask_login import UserMixin
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from bson import ObjectId
from typing import Optional
from wtforms import form, fields
from flask_admin.contrib.pymongo import ModelView
from flask_login import current_user


@dataclass_json
@dataclass
class User(UserMixin):
    _id: Optional[ObjectId] = None
    username: str = ''
    email: str = ''
    pass_hash: str = ''

    def get_id(self):
        try:
            return str(self.username)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')


class UserForm(form.Form):
    username = fields.StringField('Username')
    email = fields.StringField('Email')
    role = fields.StringField('Role')


class UserView(ModelView):
    column_list = ('username', 'email', 'role')
    form = UserForm

    def is_accessible(self):  # this method allows only logged in users access this admin view.
        return current_user.is_authenticated  # Can be changed to allow access with certain user role. Flask-security ad
