# schemas/audit_schema.py

audit_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "entity": {"type": "string"},
                    "entity_id": {"type": "string"},
                    "field": {"type": "string"},
                    "before": {"type": "string"},
                    "after": {"type": "string"},
                    "changed_by": {"type": "string"},
                    "timestamp": {"type": "string", "format": "date-time"}
                },
                "required": [
                    "entity",
                    "entity_id",
                    "field",
                    "before",
                    "after",
                    "changed_by",
                    "timestamp"
                ]
            }
        }
    },
    "required": ["data"]
}