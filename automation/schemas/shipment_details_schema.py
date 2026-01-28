# schemas/shipment_details_schema.py

shipment_details_schema = {
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