# Postman Run Guide — AtlasLogix Assessment API

## Overview
This guide explains how to run the AtlasLogix Postman collection for smoke testing and compliance validation.

---

## Collection Variables
Define these variables at the **collection level**:

- **`baseUrl`** → `https://nexus-atlaslogix-assessment.vast-soft.com/api`
- **`token`** → Bearer token obtained from `/api/v1/auth/login`
- **`tenantId`** → e.g., `TENANT-01`
- **`shipmentId`** → dynamically set from `/api/v1/tenants/{{tenantId}}/shipments`

---

## Refreshing Token
1. Run **Auth → POST /api/v1/auth/login** with credentials:
   - Email: `auditor@atlaslogix.test`
   - Password: `password`
2. Copy the `access_token` from the response.
3. Save it into the **collection variable `token`**, or automate with:
   ```javascript
   let jsonData = pm.response.json();
   pm.collectionVariables.set("token", jsonData.access_token);

    Smoke Test Sequence
Run the following requests in order:
- Auth → /api/v1/auth/login
- Shipments List → /api/v1/tenants/{{tenantId}}/shipments
- Shipment Details → /api/v1/shipments/{{shipmentId}}
- Sensor Data → /api/v1/shipments/{{shipmentId}}/sensor-data
- Compliance Approve → /api/v1/shipments/{{shipmentId}}/compliance/approve
- Compliance Report → /api/v1/shipments/{{shipmentId}}/compliance/report
- Audit Logs → /api/v1/audit-logs?entity=shipment&entityId={{shipmentId}}
- Stream Sensor Data (Bonus) → /api/v1/stream/sensor-data


