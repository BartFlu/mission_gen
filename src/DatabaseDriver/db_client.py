from pymongo import MongoClient
from abc import ABC, abstractmethod

from src.DatabaseDriver.mission_driver import MissionDataDriver
from src.DatabaseDriver.terrain_driver import TerrainDataDriver
from src.DatabaseDriver.user_driver import UsersDataDriver

from typing import Optional

import os


class MongoDatabaseDriverBase(ABC):

    def __init__(self, db="wh40k_mission_gen_db"):


        self.client: Optional[MongoClient] = None  # initialization of client variable -
        # to be replaced with pymongo MongoClient instance
        self.db = None
        self.mission_driver: Optional[MissionDataDriver] = None
        self.terrain_driver: Optional[TerrainDataDriver] = None
        self.user_driver: Optional[UsersDataDriver] = None

    def _connect_drivers(self):
        self.mission_driver = MissionDataDriver(self.db)
        self.terrain_driver = TerrainDataDriver(self.db)
        self.user_driver = UsersDataDriver(self.db)

    def get_mission_collection(self):
        return self.db[self.mission_driver.mission_col]

    @staticmethod
    @abstractmethod
    def _connect(conn_details):
        return None

    def client_close(self):
        self.client.close()


class MongoDatabaseDriverLocal(MongoDatabaseDriverBase):

    def __init__(self, db="wh40k-mission-gen-db", port=27017):
        super().__init__(db=db)

        self.client = self._connect(port)
        self.db = self.client[db]
        self._connect_drivers()

    @staticmethod
    def _connect(port: int = 27017):
        return MongoClient(host='localhost', port=port)


class MongoDatabaseDriverProduction(MongoDatabaseDriverBase):

    def __init__(self, db="wh40k-mission-gen", uri=None):

        super().__init__(db=db)
        self.client = self._connect(uri or os.environ["Mongo"])
        self.db = self.client[db]
        self._connect_drivers()

    @staticmethod
    def _connect(conn_str: str):
        return MongoClient(conn_str)


class MongoDatabaseDriverDevelop(MongoDatabaseDriverBase):

    def __init__(self, db="develop-mission-gen", uri=None):

        super().__init__(db=db)

        self.client = self._connect(uri or os.environ["Mongo"])
        self.db = self.client[db]
        self._connect_drivers()

    @staticmethod
    def _connect(conn_str: str):
        return MongoClient(conn_str)
