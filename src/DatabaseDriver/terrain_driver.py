from pymongo import database
from dacite import from_dict
from src.DataModel.tablemodel import TableData


class TerrainDataDriver:
    def __init__(self, db_link: database.Database):
        self.db = db_link
        self.mission_col = "terrain_maps"

    def create_terrain_map(self, table: TableData):
        exists = self.db[self.mission_col].find_one({"table_id": table.table_id})
        if exists:
            print("Table already exists")
            return None
        else:
            temp_dict = table.to_dict()
            temp_dict.pop("_id")
            res = self.db[self.mission_col].insert_one(temp_dict)
            return res.inserted_id
        pass

    def read_all_terrain_ids(self):
        """

        :return: a list of all available tables
        """
        temp_list = self.db[self.mission_col].find({}, {"_id": 0, "table_id": 1})
        return [table['table_id'] for table in temp_list]

    def read_matching_terrain_ids(self, sel_id):
        """

        :param sel_id: id of a chosen mission
        :return: a list of ids of all matching tables
        """
        temp_list = self.db[self.mission_col].find({"relevant_mission_id": sel_id},
                                                                              {"_id": 0, "table_id": 1})
        return [table['table_id'] for table in temp_list]

    def read_selected_terrain(self, table_id):
        """

        :param table_id: selected table id
        :return: an instance of TableData class filled with selected table data
        """
        mission = self.db[self.mission_col].find_one({"table_id": table_id}, {"_id": 0})
        if mission:
            return from_dict(data_class=TableData, data=mission)

    def update_terrain_map(self):
        # TODO implementation
        pass

    def delete_mission_by_id(self, mission_id: str):
        # TODO implementation
        pass


if __name__ == "__main__":
    pass