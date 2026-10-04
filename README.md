# Project 5: Multi-Company Corporate Expense Ledger and API Integration Engine

An enterprise-grade financial module providing row-level data isolation, multi-subsidiary auditing utilities, and secure external REST API data synchronization for high-volume corporate expense tracking.

---

## Business Case and Problem Statement

Conglomerates managing multiple corporate entities often face compliance risks, data leakage, and administrative errors due to misallocated expenses or unauthorized cross-subsidiary document access. Furthermore, manual entry of expenses from external applications or third-party scanning tools introduces data latency and increased operating costs.

This module resolves these vulnerabilities through a two-tier framework.

Internally, it implements strict data isolation, allowing users to view and interact only with records belonging to their active business tenants while providing global managers with secure cross-company aggregation tools.

Externally, it deploys a headless API endpoint that permits authenticated third-party applications to inject expense records directly into the system safely.

---

## Technical Implementations

* **Two-Tier System Security Architecture:** Configured model-level access matrices via security tables to govern role permissions, working alongside automated row-level global record rules to dynamically append company context filters to all active database queries.

* **Optimized Database Aggregations:** Utilized native database group processing methods to execute high-speed native SQL aggregation routines directly in PostgreSQL, avoiding the performance degradation associated with standard memory loop evaluations over heavy datasets.

* **Multi-Tenant Context Switching:** Developed cross-subsidiary reporting utilities that leverage database environment modifiers to transition background query scopes across individual business entities without causing cache validation exceptions.

* **Unauthenticated Web Controllers:** Designed an external network controller inheriting from the base routing class that bypasses Cross-Site Request Forgery (CSRF) restrictions to accept secure, real-time incoming communication payloads from external third-party webhooks.

* **Relational Interface Boundaries:** Implemented dynamic user interface attributes to govern conditional visibility and field accessibility, locking record linkages once an expense transitions out of its draft lifecycle.

---

## Module Directory Structure

```text
__manifest__.py
__init__.py
controllers/main.py
models/corporate_expense.py
security/ir.model.access.csv
security/corporate_expense_security.xml
views/corporate_expense_views.xml
```

* **`__manifest__.py`**: Module descriptor declaring system dependencies and loading sequence.

* **`__init__.py`**: Core initializers to expose the backend application packages.

* **`controllers/main.py`**: REST API endpoint implementation managing internet URL paths and security headers.

* **`models/corporate_expense.py`**: Core transactional tracking schema, database state overrides, and loop-safe transition actions.

* **`security/ir.model.access.csv`**: Table-level access control list assigning baseline execution rights to security groups.

* **`security/corporate_expense_security.xml`**: Global structural record rules filtering visibility parameters based on multi-subsidiary company choice arrays.

* **`views/corporate_expense_views.xml`**: Structural presentation configurations defining the visual layout of form components, list columns, window actions, and dashboard navigation menus.

---

## Deployment and Installation Checklist

1. Export the module directory directly to your server's designated custom addons directory path.

2. Ensure the module manifest explicitly lists base core modules within its dependency array to permit correct framework loading order.

3. Update your server application list via the application interface to register the new code repository.

4. Install the corporate expense ledger package. Use an external API test harness to transmit sample JSON network payloads to the synchronized path, verifying that custom security authorization headers are evaluated properly by the engine.
