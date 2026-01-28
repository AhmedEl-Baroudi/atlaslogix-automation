import pytest
from jsonschema import validate
from automation.schemas.shipments_list_schema import shipment_schema

@pytest.mark.shipments
def test_shipments_schema(api_client):
    """Validate shipments list response schema and business rules for the tenant."""
    response = api_client.get_shipments()
    data = response.json()

    # Validate against schema
    validate(instance=data, schema=shipment_schema)

    # Assertions
    assert response.status_code == 200
    assert "count" in data and data["count"] >= 1
    assert "results" in data and isinstance(data["results"], list)

    for shipment in data["results"]:
        assert shipment["tenantId"] == "TENANT-01"
        assert shipment["shipmentId"].startswith("SHIP-")
        assert shipment["status"] in ["IN_TRANSIT", "AT_WAREHOUSE", "DELIVERED", "LOCKED"]
        assert shipment["compliance_status"] in ["APPROVED", "PENDING", "REJECTED"]
        assert isinstance(shipment["status"], str)
        assert isinstance(shipment["compliance_status"], str)