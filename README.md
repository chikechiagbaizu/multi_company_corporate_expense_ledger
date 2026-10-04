# Project 5: Multi-Company Corporate Expense Ledger and API Integration Engine

An enterprise-grade financial module providing row-level data isolation and multi-subsidiary auditing utilities.

---

## Business Case and Problem Statement

Conglomerates managing multiple corporate entities often face compliance risks, data leakage, and administrative errors due to misallocated expenses or unauthorized cross-subsidiary document access. Furthermore, manual entry of expenses from external applications or third-party scanning tools introduces data latency and increased operating costs.

This module resolves these vulnerabilities through a two-tier framework.

Internally, it implements strict data isolation, allowing users to view and interact only with records belonging to their active business tenants while providing global managers with secure cross-company aggregation tools.

---

## Technical Implementations

* **Two-Tier System Security Architecture:** Configured model-level access matrices via security tables to govern role permissions, working alongside automated row-level global record rules to dynamically append company context filters to all active database queries.

* **Optimized Database Aggregations:** Utilized native database group processing methods to execute high-speed native SQL aggregation routines directly in PostgreSQL, avoiding the performance degradation associated with standard memory loop evaluations over heavy datasets.

* **Multi-Tenant Context Switching:** Developed cross-subsidiary reporting utilities that leverage database environment modifiers to transition background query scopes across individual business entities without causing cache validation exceptions.

* **Relational Interface Boundaries:** Implemented dynamic user interface attributes to govern conditional visibility and field accessibility, locking record linkages once an expense transitions out of its draft lifecycle.

---

## Module Directory Structure

```text
__manifest__.py
__init__.py
models/corporate_expense.py
security/ir.model.access.csv
security/corporate_expense_record_rule.xml
security/corporate_expense_groups.xml
views/view_corporate_expense_form.xml
views/view_corporate_expense_list.xml
```

* **`__manifest__.py`**: Module descriptor declaring system dependencies and loading sequence.

* **`__init__.py`**: Core initializers to expose the backend application packages.

* **`models/corporate_expense.py`**: Core transactional tracking schema, database state overrides, and loop-safe transition actions.

* **`security/ir.model.access.csv`**: Table-level access control list assigning baseline execution rights to security groups.

* **`security/corporate_expense_record_rule.xml`**: Global structural record rules filtering visibility parameters based on multi-subsidiary company choice arrays.

* **`security/corporate_expense_groups.xml`**: Created System Admin and Standard Users groups.

* **`views/view_corporate_expense_form.xml & views/view_corporate_expense_list.xml`**: Structural presentation configurations defining the visual layout of form components, list columns, window actions, and dashboard navigation menus.

---

## Deployment and Installation Checklist

1. Export the module directory directly to your server's designated custom addons directory path.

2. Ensure the module manifest explicitly lists base core and account core modules within its dependency array to permit correct framework loading order.

3. Update your server application list via the application interface to register the new code repository.

4. Install the corporate expense ledger package. 
