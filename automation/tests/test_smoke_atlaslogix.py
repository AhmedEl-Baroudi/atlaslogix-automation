import pytest
from jsonschema import validate

from automation.schemas.shipments_list_schema import shipment_schema
from automation.schemas.shipment_details_schema import shipment_details_schema
from automation.schemas.compliance_schema import compliance_schema
from automation.schemas.audit_schema import audit_schema


@pytest.mark.shipments
def test_shipments_list(api_client):
    """Verify shipments list returns at least one shipment and matches schema."""
    response = api_client.get_shipments()
    data = response.json()

    validate(instance=data, schema=shipment_schema)

    assert response.status_code == 200
    assert "count" in data and data["count"] >= 1
    assert "results" in data and isinstance(data["results"], list)


@pytest.mark.shipment_details
def test_shipment_details(api_client, shipment_id):
    """Fetch one shipment details and validate schema."""
    response = api_client.get_shipment(shipment_id)
    data = response.json()

    validate(instance=data, schema=shipment_details_schema)

    assert response.status_code == 200
    assert data["shipmentId"] == shipment_id
    assert data["tenantId"] == "TENANT-01"
    assert data["status"] in ["IN_TRANSIT", "AT_WAREHOUSE", "DELIVERED", "LOCKED"]
    assert data["compliance_status"] in ["APPROVED", "PENDING", "REJECTED"]


import pytest
from jsonschema import validate
from automation.schemas.compliance_schema import compliance_schema

@pytest.mark.compliance
def test_compliance_approve(api_client, shipment_id):
    """Attempt compliance approve and validate schema or error response."""
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


@pytest.mark.audit
def test_audit_logs(api_client, shipment_id):
    """Check audit logs after compliance attempt and validate schema."""
    response = api_client.get_audit_logs(shipment_id)
    data = response.json()

    validate(instance=data, schema=audit_schema)

    assert response.status_code == 200
    assert "data" in data and isinstance(data["data"], list)

    if data["data"]:
        entry = data["data"][0]
        assert entry["entity"] == "shipment"
        assert entry["entity_id"] == shipment_id
        assert entry["field"] == "compliance_status"
        assert entry["before"] in ["PENDING", "APPROVED", "REJECTED"]
        assert entry["after"] in ["PENDING", "APPROVED", "REJECTED"]
        assert entry["changed_by"].startswith("user-")