import pytest
from jsonschema import validate
from automation.schemas.audit_schema import audit_schema

@pytest.mark.audit
def test_audit_schema(api_client, shipment_id):
    """Validate audit log schema and business rules for a given shipment."""
    response = api_client.get_audit_logs(shipment_id)
    data = response.json()

    # Validate against schema
    validate(instance=data, schema=audit_schema)

    # Assertions
    assert response.status_code == 200
    assert "data" in data and len(data["data"]) >= 1

    for log in data["data"]:
        assert log["entity"] == "shipment"
        assert log["entity_id"] == shipment_id
        assert log["field"] == "compliance_status"
        assert log["before"] in ["PENDING", "APPROVED", "REJECTED"]
        assert log["after"] in ["PENDING", "APPROVED", "REJECTED"]
        assert log["changed_by"].startswith("user-")
        assert isinstance(log["timestamp"], str) and "T" in log["timestamp"]  # basic ISO check