import pytest
from jsonschema import validate
from automation.schemas.compliance_schema import compliance_schema

@pytest.mark.compliance
def test_compliance_schema(api_client, shipment_id):
    """Validate compliance approval response schema and business rules for a given shipment."""
    response = api_client.approve_compliance(shipment_id)
    data = response.json()

    if response.status_code == 200:
        # Validate against schema
        validate(instance=data, schema=compliance_schema)

        # Assertions for success
        assert data["tenantId"] == "TENANT-01"
        assert data["shipmentId"] == shipment_id
        assert data["compliance_status"] in ["APPROVED", "PENDING", "REJECTED"]
        assert data["status"] in ["IN_TRANSIT", "AT_WAREHOUSE", "DELIVERED", "LOCKED"]
        assert data["approved_by"].startswith("user-")

    else:
        # Assertions for error response
        assert response.status_code in [403, 409]
        assert "error" in data
        assert data["error"] == "RECORD_LOCKED"
        assert "message" in data
        assert "locked" in data["message"].lower()