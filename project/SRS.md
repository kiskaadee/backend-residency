# BiteTrack v2 — Software Requirements Specification (SRS)

Version: 0.1 (Draft)

---

# 1. Purpose

BiteTrack is an operational management system designed for small food businesses producing and selling perishable products.

The system centralizes inventory management, customer management, sales, payment tracking, inventory loss registration, and operational reporting into a unified workflow.

Its objective is to reduce operational overhead while preserving historical business information that supports better production and inventory decisions.

---

# 2. Scope

The system shall provide functionality for:

- User authentication
- User authorization
- Customer management
- Product catalog management
- Category management
- Inventory management
- Sales registration
- Payment tracking
- Inventory loss registration
- Business reporting

The current version does not attempt to replace accounting or ERP software.

---

# 3. Stakeholders

- Business Owner
- Administrator
- Staff Member

Future versions may include customer-facing functionality.

---

# 4. Business Problem

Small food businesses frequently rely on multiple spreadsheets to independently manage:

- Customers
- Inventory
- Sales
- Outstanding payments
- Inventory waste
- Business reports

This fragmentation makes it difficult to answer questions such as:

- Which customers still owe money?
- Which products generate the most waste?
- How much inventory expires every week?
- Which products are most profitable?
- How much inventory should be produced tomorrow?

BiteTrack consolidates these operational workflows into a single system.

---

# 5. Functional Requirements

## 5.1 Identity & Access

FR-001  
The system shall allow administrators to register users.

FR-002  
The system shall authenticate registered users.

FR-003  
The system shall enforce role-based authorization.

FR-004  
The system shall allow administrators to activate or deactivate user accounts.

---

## 5.2 Customer Management

FR-010  
The system shall maintain a customer directory.

FR-011  
A customer record shall contain:

- Full name
- Phone number
- Optional email address

FR-012  
The system shall associate sales with customers.

FR-013  
The system shall determine each customer's outstanding balance from recorded sales and payments.

---

## 5.3 Product Management

FR-020  
The system shall manage product categories.

FR-021  
The system shall create, update and archive products.

FR-022  
Products shall define a default shelf life.

---

## 5.4 Inventory

FR-030  
The system shall maintain current inventory levels.

FR-031  
The system shall automatically decrease inventory when sales are recorded.

FR-032  
The system shall allow manual registration of inventory losses.

FR-033  
Inventory losses shall record a reason.

Examples include:

- Expired
- Damaged
- Quality issue
- Manual adjustment

---

## 5.5 Sales

FR-040  
The system shall register product sales.

FR-041  
A sale shall contain one or more sale items.

FR-042  
The system shall calculate sale totals automatically.

FR-043  
The system shall associate every sale with the staff member who created it.

---

## 5.6 Payments

FR-050  
The system shall record payments associated with a sale.

FR-051  
A sale may receive multiple payments.

FR-052  
The system shall calculate outstanding balances from recorded payments.

---

## 5.7 Reporting

FR-060  
Display current inventory.

FR-061  
Display inventory loss history.

FR-062  
Display customer balances.

FR-063  
Display sales history.

FR-064  
Display product performance.

FR-065  
Provide historical operational reports.

---

# 6. Non-functional Requirements

## Performance

The system shall provide responsive interaction during normal business operations.

## Security

Passwords shall be stored using an adaptive cryptographic password hashing algorithm.

The system shall authenticate users before granting access to protected resources.

Role-based authorization shall restrict access to administrative functionality.

## Reliability

Operational data shall remain persistent and recoverable after unexpected failures.

## Maintainability

The software architecture shall support incremental feature additions with minimal impact on existing functionality.

---

# 7. Constraints

- Backend-first development.
- Single business deployment.
- Lightweight deployment on commodity hardware.
- Designed primarily for small food businesses.

---

# 8. Assumptions

- One deployment corresponds to one business.
- Inventory quantities are entered manually.
- Products belong to one category.
- Staff members authenticate before using the system.

---

# 9. Out of Scope

The current version does not include:

- Accounting
- Supplier management
- Payment gateway integration
- Online ordering
- Multi-tenant deployments

---

# 10. Planned Future Features

- Bootstrap initialization using a one-time deployment key.
- QR-based administrator recovery.
- Automatic inventory expiration.
- Production recommendations based on historical sales and inventory losses.