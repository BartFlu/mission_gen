from DatabaseDriver.db_client import MongoDatabaseDriverProduction, MongoDatabaseDriverDevelop
from DataModel.usermodel import User

if __name__ == "__main__":
    mddl = MongoDatabaseDriverProduction()
    dev = MongoDatabaseDriverDevelop()

    source = {
"tables":
     [
         {
             "table_id": "1a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "1a"
         },
         {
             "table_id": "1b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "1b"
         },
         {
             "table_id": "1c-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "1c"
         },
         {
             "table_id": "2a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "2a"
         },
         {
             "table_id": "3a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "3a"
         },
         {
             "table_id": "4a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "4a"
         },
         {
             "table_id": "5a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "5a"
         },
         {
             "table_id": "6a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "6a"
         },
         {
             "table_id": "7a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "7a"
         },
         {
             "table_id": "8a-wtc",
             "relevant_mission_id": ["GTpack-sf-retrieval", "GTpack-sf-surround_and_destroy", "GTpack-sf-overrun"],
             "table_img": "8a"
         },
         {
             "table_id": "2b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "2b"
         },
         {
             "table_id": "3b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "3b"
         },
         {
             "table_id": "4b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "4b"
         },
         {
             "table_id": "5b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "5b"
         },
         {
             "table_id": "6b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "6b"
         },
         {
             "table_id": "7b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "7b"
         },
         {
             "table_id": "8b-wtc",
             "relevant_mission_id": ["GTpack-sf-scorched_earth", "GTpack-sf-battle_lines", "GTpack-sf-sweep_and_clear"],
             "table_img": "8b"
         },
         {
             "table_id": "2c-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "2c"
         },
         {
             "table_id": "3c-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "3c"
         },
         {
             "table_id": "4c-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "4c"
         },
         {
             "table_id": "5c-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "5c"
         },
         {
             "table_id": "6c-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "6c"
         },
         {
             "table_id": "7c-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "7c"
         },
         {
             "table_id": "8-wtc",
             "relevant_mission_id": ["GTpack-sf-the_vital_intelligence", "GTpack-sf-priority_target"],
             "table_img": "8c"
         }
     ]
}
    user = dev.mission_driver