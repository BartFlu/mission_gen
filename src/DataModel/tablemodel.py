from bson import ObjectId
from typing import Optional, List

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TableData:
    """
        This dataclass should be used to represent table data
        The class is loaded from/feeded to the mongo database driver
    """
    _id: Optional[ObjectId] = None  # db specific
    table_id: str = ""
    relevant_mission_id: List[str] = field(default_factory=list)
    table_img: str = ""     # name of a static file with this table image
