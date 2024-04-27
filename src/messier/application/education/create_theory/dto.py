from dataclasses import dataclass


@dataclass
class CreateTheoryDTO:
    educational_material_id: int
    title: str
    description: str
