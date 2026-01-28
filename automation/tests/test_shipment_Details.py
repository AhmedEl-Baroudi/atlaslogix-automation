import pytest
from jsonschema import validate
from automation.schemas.shipment_details_schema import shipment_details_schema

@pytest.mark.shipment_details
def test_shipment_details_schema(api_client, shipment_id):
    """Validate shipment details response schema and business rules for a given shipment."""
    response = api_client.get_shipment(shipment_id)
    data = response.json()

    # Validate against schema
    validate(instance=data, schema=shipment_details_schema)

    # Assertions
    assert response.status_code == 200
    assert data["tenantId"] == "TENANT-01"
    assert data["shipmentId"] == shipment_id
    assert data["status"] in ["IN_TRANSIT", "AT_WAREHOUSE", "DELIVERED", "LOCKED"]
    assert data["compliance_status"] in ["APPROVED", "PENDING", "REJECTED"]
    assert data["approved_by"].startswith("user-")
    assert isinstance(data["approved_by"], str)
    assert isinstance(data["status"], str)
    assert isinstance(data["compliance_status"], str)