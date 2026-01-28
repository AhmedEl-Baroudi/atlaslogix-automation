import pytest
from jsonschema import validate
from automation.schemas.login_schema import login_schema

@pytest.mark.login
def test_login_schema(api_client):
    """Validate login response schema and business rules for the compliance auditor user."""
    response = api_client.login()
    data = response.json()

    # Validate against schema
    validate(instance=data, schema=login_schema)

    # Assertions
    assert response.status_code == 200
    assert data["role"] == "COMPLIANCE_AUDITOR"
    assert data["tenantId"] == "TENANT-01"
    assert data["userId"].startswith("user-")
    assert isinstance(data["userId"], str)
    assert isinstance(data["tenantId"], str)
    assert isinstance(data["role"], str)