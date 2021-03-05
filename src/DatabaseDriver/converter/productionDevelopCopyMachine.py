from DatabaseDriver.db_client import MongoDatabaseDriverProduction, MongoDatabaseDriverDevelop
from dacite import from_dict
from DataModel.mission_model import MissionData


class ProductionDevelopCopy:
    """
    This class take care of making the transition of data between production and develop db's
    """

    def __init__(self):
        self.production = MongoDatabaseDriverProduction()
        self.develop = MongoDatabaseDriverDevelop()

    def copy_to_develop(self):
        self._transfer_mission_collection_to_develop()
        self._transfer_tables_collection_to_develop()

    def _transfer_mission_collection_to_develop(self):
        production_id_list = self.production.mission_driver.read_all_mission_ids()
        for id in production_id_list:
            mission = self.production.mission_driver.read_mission_by_id(id)
            self.develop.mission_driver.create_mission(mission)
            return True

    def _transfer_tables_collection_to_develop(self):
        production_id_list = self.production.terrain_driver.read_all_terrain_ids()
        for id in production_id_list:
            terrain = self.production.terrain_driver.read_selected_terrain(id)
            self.develop.terrain_driver.create_terrain_map(terrain)

    def copy_to_production(self):
        if self._security_check():
            self._transfer_mission_collection_to_production()
            self._transfer_table_collection_to_production()
        else:
            print('Aborted.')

    @staticmethod
    def _security_check():
        sec = input('Type "I\'am coping data into the production database" to proceed: ')
        if sec == 'I\'am coping data into the production database':
            return True

    def _transfer_mission_collection_to_production(self):
        develop_id_list = self.develop.mission_driver.read_all_mission_ids()
        for id in develop_id_list:
            mission = self.develop.mission_driver.read_mission_by_id(id)
            self.production.mission_driver.create_mission(mission)

    def _transfer_table_collection_to_production(self):
        develop_id_list = self.develop.terrain_driver.read_all_terrain_ids()
        for id in develop_id_list:
            terrain = self.develop.terrain_driver.read_selected_terrain(id)
            self.production.terrain_driver.create_terrain_map(terrain)


if __name__ == "__main__":
    copy = ProductionDevelopCopy()


