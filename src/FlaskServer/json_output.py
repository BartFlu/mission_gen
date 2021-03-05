from flask import Blueprint, session, request, redirect, url_for, jsonify
from random import choice
from src.FlaskServer.db import get_db
import json


json_output_component = Blueprint('json_output', __name__)


@json_output_component.route('/getSource')
def get_ids():

    """
    This method is use to generate up-to-date content for Source dropdown. For random and select.
    :return: json with all available mission sources.
    """

    db = get_db()
    all_ids = db.mission_driver.read_all_mission_ids()
    sources = set([x.split("-")[0] for x in all_ids])  # Extract the mission source from the ID
    data = {
        "source": list(sources),
    }
    return json.dumps(data)


@json_output_component.route('/getSession')
def get_session():
    print(session)

    return json.dumps(session)


@json_output_component.route('/getRandomScenario', methods=['GET'])
def get_random_scenario():

    """
        Purpose: Random mission choice.
        Request has to contain two keys: scale and group. Source can be empty - in that case method will choose mission
        from all sources.
        In case of request without any of the keys it return error.

        :return: json with mission parameters
    """
    scale = request.args.get("scale")

    if scale is None:
        return jsonify({"error": "Missing key: scale"})
    source = request.args.get("source")
    if source is None:
        return jsonify({"error": "Missing key: source"})
    db = get_db()

    if source:  # if group was chosen
        available_ids = db.mission_driver.read_selected_ids(group=source, scale=scale)

        if not available_ids:  # in case of non-existing scale for that source
            available_ids = db.mission_driver.read_all_scale_mission_ids(scale)  # search from all available sources

    else:  # if group was left as "all"
        available_ids = db.mission_driver.read_all_scale_mission_ids(scale)
        # search from all available sources

    mission_id = choice(available_ids)  # random choice from returned ids
    mission = db.mission_driver.read_mission_by_id(mission_id)  # return mission mathinng to the chosen id
    session['mission'] = mission  # choden mission is saved in session
    #  clears session table info if mission without it was chosen.
    if not mission.mission_id.startswith("GTpack") or not mission.mission_scale == "StrikeForce":
        session.pop('table', None)

    return mission.to_json()


@json_output_component.route('/getTerrainMap', methods=['GET'])
def get_terrain_map():

    """
    Purpose: Random choice of suitable terrain map.
    Request has to contain two keys: mission_id and type. Both are obligatory and cannot be empty
    :return: table info (img files names) as json
    """

    db = get_db()
    mission_id = request.args.get("mission_id")
    if mission_id is None:
        return jsonify({"error": "Missing key: mission_id"})
    table_type = request.args.get("type")
    if table_type is None:
        return jsonify({"error": "Missing key: table_type"})

    available_tables = db.terrain_driver.read_matching_terrain_ids(mission_id)
    if available_tables:
        table_id = choice(available_tables)
        table = db.terrain_driver.read_selected_terrain(table_id)
        if table_type == "random":
            session.pop('random_table', None)
            session['random_table'] = table
            print('saved in random_table')
        elif table_type == "select":
            session.pop('selected_table', None)
            session['selected_table'] = table
            print('saved in selected_table')
        return table.to_json()
    else:
        return jsonify({"error": "Not Found"})


@json_output_component.route('/getAvailableScenariosData')
def get_available_scenarios_data():

    """
    Purpose: Delivers data for selector dropdowns.
    :return: Whole db content as json like this
    {"Source": {"Scale": [{"mission_id": "GTpack-inc-crossfire", "name": "Crossfire"},
    """

    db = get_db()
    all_ids = db.mission_driver.read_all_mission_ids()
    sel_ids = set([x.split("-")[0] for x in all_ids])  # z mission_id wyciąga źródło misji (split), tworzy listę,
    db_content = {}
    for i in sel_ids:
        scales = db.mission_driver.read_matching_scales(i)
        db_content[i] = dict.fromkeys(scales, [])
        for scale in scales:
            missions_ids = db.mission_driver.read_selected_ids(i, scale)
            missions_names = db.mission_driver.read_selected_names(i, scale)
            table = []
            for mission_id, name in zip(missions_ids, missions_names):
                table.append({
                    "mission_id": mission_id,
                    "name": name
                })
            db_content[i][scale] = table
    return json.dumps(db_content)


@json_output_component.route('/getScenarioByID', methods=["GET"])
def get_scenario_by_id():
    """
        Purpose: Retrieve selected mission data. Requires key mission_id
        :return: mission data as json
    """
    db = get_db()
    mission_id = request.args.get("mission_id")
    mission = db.mission_driver.read_mission_by_id(mission_id)
    session.pop('selected_mission', None)
    session['selected_mission'] = mission
    if not mission.mission_id.startswith("GTpack") or not mission.mission_scale == "StrikeForce":
        print('tabled poped')
        session.pop('table_selector', None)
    return mission.to_json()
