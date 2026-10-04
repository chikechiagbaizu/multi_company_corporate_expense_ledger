# Project 5: Multi-Company Corporate Expense Ledger

An enterprise-oriented financial module providing multi-company data isolation, controlled access, and cross-company reporting utilities.

---

## Business Case and Problem Statement

Organizations managing multiple corporate entities often face compliance risks, data leakage, and administrative errors caused by misallocated expenses or unauthorized cross-company document access.

This module addresses these challenges through a security-focused architecture.

Internally, it implements strict data isolation, allowing users to view and interact only with records belonging to their permitted companies while providing authorized managers with controlled cross-company aggregation and reporting capabilities.

---

## Technical Implementations

* **Two-Tier System Security Architecture:** Configured model-level access matrices via security tables to govern role permissions, working alongside automated record rules to dynamically restrict records based on the user's permitted companies.

* **Optimized Database Aggregations:** Utilized Odoo's native grouping and aggregation mechanisms to efficiently calculate expense totals across larger datasets without unnecessary Python-level iteration.

* **Multi-Company Context Switching:** Developed cross-company reporting utilities that leverage Odoo environment context and company switching mechanisms to execute queries within the appropriate company scope while maintaining environment consistency.

* **Relational Interface Boundaries:** Implemented dynamic user interface attributes to govern conditional visibility and field accessibility, including restricting record modifications once an expense transitions out of its draft lifecycle.

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

* **`__init__.py`**: Core initializer used to expose the backend application packages.

* **`models/corporate_expense.py`**: Core transactional expense model containing business logic, database state management, and lifecycle transition actions.

* **`security/ir.model.access.csv`**: Model-level access control list assigning baseline create, read, write, and delete permissions to security groups.

* **`security/corporate_expense_record_rule.xml`**: Record rules restricting expense visibility and access according to the user's permitted companies.

* **`security/corporate_expense_groups.xml`**: Defines the System Admin and Standard Users security groups.

* **`views/view_corporate_expense_form.xml` & `views/view_corporate_expense_list.xml`**: Presentation configurations defining form layouts, list columns, window actions, and menu navigation.

---

## Deployment and Installation Checklist

1. Copy the module directory to the server's designated custom addons directory.

2. Ensure the module manifest lists the required core dependencies, including `base` and `account`, in the dependency array.

3. Update the Odoo Apps list through the application interface to register the new module.

4. Install the **Corporate Expense Ledger** module.
