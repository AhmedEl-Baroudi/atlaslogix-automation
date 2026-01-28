import pytest
import requests
import logging

BASE_URL = "https://nexus-atlaslogix-assessment.vast-soft.com/api/v1"
EMAIL = "auditor@atlaslogix.test"
PASSWORD = "password"

# Configure logging once for the suite
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def login(self):
        return requests.post(f"{self.base_url}/auth/login", json={
            "email": EMAIL,
            "password": PASSWORD
        })

    def get_shipments(self):
        return requests.get(f"{self.base_url}/tenants/TENANT-01/shipments", headers=self.headers)

    def get_shipment(self, shipment_id: str):
        return requests.get(f"{self.base_url}/shipments/{shipment_id}", headers=self.headers)

    def approve_compliance(self, shipment_id: str):
        return requests.post(f"{self.base_url}/shipments/{shipment_id}/compliance/approve", headers=self.headers)

    def get_audit_logs(self, shipment_id: str):
        return requests.get(
            f"{self.base_url}/audit-logs?entity=shipment&entityId={shipment_id}",
            headers=self.headers
        )

@pytest.fixture(scope="session")
def token():
    """Login once per session and return bearer token."""
    resp = requests.post(f"{BASE_URL}/auth/login", json={
        "email": EMAIL,
        "password": PASSWORD
    })
    logger.info("Login response: %s", resp.text)
    assert resp.status_code == 200
    data = resp.json()
    return data["token"]


@pytest.fixture(scope="session")
def api_client(token):
    """Provide a reusable API client with authenticated headers."""
    return APIClient(BASE_URL, token)


@pytest.fixture(scope="session")
def shipment_id(api_client):
    """Fetch and return the first shipment ID."""
    resp = api_client.get_shipments()
    logger.info("Shipments response: %s", resp.text)
    assert resp.status_code == 200
    data = resp.json()
    assert "results" in data and len(data["results"]) > 0
    return data["results"][0]["shipmentId"]