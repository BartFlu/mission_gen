from flask import Blueprint, session, render_template
from dacite import from_dict
from src.DataModel.tablemodel import TableData
from src.DataModel.mission_model import MissionData
from src.FlaskServer.db import get_db


html_output_component = Blueprint('html_output', __name__)


@html_output_component.route('/selectMission')
def select_mission():
    db = get_db()
    all_ids = db.mission_driver.read_all_mission_ids()
    sel_ids = extract_unique_ids(all_ids)
    if 'selected_mission' in session and 'selected_table' in session:
        mission = from_dict(data_class=MissionData, data=session['selected_mission'])
        source = mission.mission_id.split("-")[0]
        table = from_dict(data_class=TableData, data=session['selected_table'])
        return render_template("select_mission.html", sel_ids=sel_ids, mission=mission, source=source, table=table)
    # if only mission is stored in session only mission will be loaded
    elif 'selected_mission' in session:
        mission = from_dict(data_class=MissionData, data=session['selected_mission'])
        source = mission.mission_id.split("-")[0]
        return render_template("select_mission.html", sel_ids=sel_ids, mission=mission, source=source)
    return render_template("select_mission.html", sel_ids=sel_ids)


@html_output_component.route('/')
def home():

    db = get_db()
    all_ids = db.mission_driver.read_all_mission_ids()
    sel_ids = extract_unique_ids(all_ids)
    if 'mission' in session and 'random_table' in session:
        mission = from_dict(data_class=MissionData, data=session['mission'])
        source = mission.mission_id.split("-")[0]
        table = from_dict(data_class=TableData, data=session['random_table'])
        return render_template("mission_gen.html", sel_ids=sel_ids, mission=mission, source=source, table=table)
    elif 'mission' in session:
        mission = from_dict(data_class=MissionData, data=session['mission'])
        source = mission.mission_id.split("-")[0]
        return render_template("mission_gen.html", sel_ids=sel_ids, mission=mission, source=source)

    return render_template("mission_gen.html", sel_ids=sel_ids, mission=None, table=None)


def extract_unique_ids(all_ids):
    """
    IDs are part of mission details entry. Separated from the rest with an '-' sign. Thus split is made to slice them
    from the rest of the string. Set method is use to make sure all ids will be unique.
    :param all_ids: list of all the strings with mission details from the db
    :return: list of just the id part
    """
    sel_ids = set([x.split("-")[0] for x in all_ids])
    return sel_ids


