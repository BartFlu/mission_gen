from bson import ObjectId
from typing import Optional

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from wtforms import form, fields
from flask_admin.contrib.pymongo import ModelView
from flask_login import current_user


@dataclass_json
@dataclass
class MissionData:
    """
        This dataclass should be used to represent mission data
        The class is loaded from/feeded to the mongo database driver
    """
    _id: Optional[ObjectId] = None  # db specific
    mission_id: str = ""  # string type id specyfing set and mission name separeted with '-'
    mission_name: str = ""
    mission_scale: str = ""  # description of the size of the mission
    deployment_img: str = ""  # location of the img file in the static folder
    mission_desc: str = ""  # mission description in html


class MissionForm(form.Form):
    _id = fields.StringField('_id')
    mission_id = fields.StringField('Mission id')
    mission_name = fields.StringField('Mission Name')
    mission_scale = fields.StringField('Mission Scale')
    deployment_img_name = fields.StringField("Deployment img file name")
    mission_desc = fields.StringField('Mission description')


class MissionView(ModelView):
    column_list = ('_id', "mission_id", 'mission_name', 'mission_scale', 'deployment_img_name', 'mission_desc')
    form = MissionForm

    def is_accessible(self):  # this method allows only logged in users acces this admin view.
        return current_user.is_authenticated  # Can be changed to allow acces with certain user role. Flask-security ad



if __name__ == "__main__":

    md = MissionData(
        mission_id="core-test_id",
        mission_name="",
        mission_scale="incursion",
        deployment_img="dssd2A1",
        mission_desc="<p> mission desc </p>"
    )

    print(type(md))

    print("\n Base dataclass \n")
    print(md)

    print("\n Json format \n")
    print(md.to_json())

    print("\n Dict format \n")
    print(md.to_dict())
