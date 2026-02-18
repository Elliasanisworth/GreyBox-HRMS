from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BedObservation(BaseModel):
    resourceType: str = "Observation"
    id: str 
    status: str = "final"
    code: dict = {"text": "Bed Occupancy Status"}
    effectiveDateTime: str = datetime.utcnow().isoformat()
    valueString: str  # "Occupied" or "Available"
    
    # Modern Pydantic V2 Config
    model_config = {
        "json_schema_extra": {
            "example": {
                "resourceType": "Observation",
                "id": "BED-42",
                "status": "final",
                "valueString": "Occupied"
            }
        }
    }