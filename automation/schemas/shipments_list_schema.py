# schemas/shipment_schema.py

shipment_schema = {
    "type": "object",
    "properties": {
        "count": {"type": "integer"},
        "next": {"type": ["string", "null"]},
        "previous": {"type": ["string", "null"]},
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "shipmentId": {"type": "string"},
                    "tenantId": {"type": "string"},
                    "status": {"type": "string"},
                    "warehouse": {"type": "string"},
                    "compliance_status": {"type": "string"},
                    "last_updated": {"type": "string", "format": "date-time"},
                    "locked_at": {"type": "string", "format": "date-time"},
                    "approved_by": {"type": "string"}
                },
                "required": [
                    "shipmentId",
                    "tenantId",
                    "status",
                    "warehouse",
                    "compliance_status",
                    "last_updated",
                    "locked_at",
                    "approved_by"
                ]
            }
        }
    },
    "required": ["count", "next", "previous", "results"]
}