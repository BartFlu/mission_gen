from pymongo import database
from dacite import from_dict
from src.DataModel.mission_model import MissionData


class MissionDataDriver:
    def __init__(self, db_link: database.Database):
        self.db = db_link
        self.mission_col = "missions"

    def create_mission(self, mission: MissionData):
        exists = self.db[self.mission_col].find_one({"mission_id": mission.mission_id})
        if exists:
            print("Mission already exists")
            return None
        else:
            temp_dict = mission.to_dict()
            temp_dict.pop("_id")
            res = self.db[self.mission_col].insert_one(temp_dict)
            return res.inserted_id

    def read_all_mission_ids(self):
        """
        :return: Returns a list with all mission_id from the collection
        """
        temp_missions = self.db[self.mission_col].find({}, {"_id": 0, "mission_id": 1})
        return [mission["mission_id"] for mission in temp_missions]

    def read_all_scale_mission_ids(self, scale: str):
        """

        :param scale: Mission scale as string
        :return: A list with all mission of desired scale from the collection
        """
        temp_missions = self.db[self.mission_col].find({"mission_scale": scale}, {"_id": 0, "mission_id": 1})
        return [mission["mission_id"] for mission in temp_missions]

    def read_matching_scales(self, source: str):
        """

        :param source: Source of mission as a string
        :return: a set of all the mission sources in the collection
        """
        temp_mission = self.db[self.mission_col].find(
            {"mission_id": {"$regex": f'{source}-'}}, {"_id": 0, "mission_scale": 1})

        return set([mission["mission_scale"] for mission in temp_mission])

    def read_mission_by_id(self, mission_id: str):
        """

        :param mission_id:
        :return: an instance of MissionData class filled with parameters of the mission with corresponding mission_id
        """
        mission = self.db[self.mission_col].find_one({"mission_id": mission_id}, {"_id": 0})

        if mission:
            return from_dict(data_class=MissionData, data=mission)
        return None

    def update_mission_by_id(self, mission_id: str, field: str, value: str):
        """

        :param mission_id: mission_if of the chosen mission
        :param field: name of the field we wish to change
        :param value: new value for the field
        :return: Mongo response
        """
        res = self.db[self.mission_col].update_one({"mission_id": mission_id}, {"$set": {field: value}})
        return res

    def delete_mission_by_id(self, mission_id: str):
        """

        :param mission_id: mission_of of the mission we wish to delete
        :return: Boolean True if the mission was deleted, else False
        """
        res = self.db[self.mission_col].delete_one({"mission_id": mission_id})
        return res.deleted_count > 0

    def read_selected_ids(self, group: str, scale: str):
        """
        Read mission by the part of mission_id(group)
        :param group:
        :param scale:
        :return: a list of selected missions
        """
        temp_missions = self.db[self.mission_col].find(
            {"mission_id": {"$regex": f'{group}-'}, "mission_scale": scale}, {"_id": 0, "mission_id": 1})

        return [mission["mission_id"] for mission in temp_missions]

    def read_selected_names(self, group: str, scale: str):
        """

        :param group:
        :param scale:
        :return:
        """
        temp_mission = self.db[self.mission_col].find(
            {"mission_id": {"$regex": f'{group}-'}, "mission_scale": scale}, {"_id": 0, "mission_name": 1})

        return [mission["mission_name"] for mission in temp_mission]


if __name__ == "__main__":
    pass
