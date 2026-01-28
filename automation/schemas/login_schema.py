# schemas/login_schema.py

login_schema = {
    "type": "object",
    "properties": {
        "token": {"type": "string"},
        "role": {"type": "string"},
        "tenantId": {"type": "string"},
        "userId": {"type": "string"}
    },
    "required": ["token", "role", "tenantId", "userId"]
}