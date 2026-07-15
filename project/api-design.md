# BiteTrack API Design

## Endpoint Specification

---

## Authentication

- `POST /auth/register` - Register a new user.
- `POST /auth/token` - Authenticate a user and issue access & refresh tokens.
- `POST /auth/refresh` - Rotate an access token using a refresh token.

---

## Users

- `GET /users/me` - Retrieve the authenticated user's profile.
- `PATCH /users/me` - Update the authenticated user's profile.
- `GET /users` - List users (Administrator only).
- `POST /users` - Create a new staff or administrator account (Administrator only).

---

## Customers

- `POST /customers` - Create customer.
- `GET /customers` - List customers.
- `GET /customers/{id}` - Retrieve customer information.
- `PATCH /customers/{id}` - Update customer information.
- `DELETE /customers/{id}` - Archive customer.
- `GET /customers/{id}/balance` - Retrieve current outstanding balance.

---

## Categories

- `POST /categories` - Create category.
- `GET /categories` - List categories.
- `GET /categories/{id}` - Retrieve category details.
- `PUT /categories/{id}` - Update category.
- `DELETE /categories/{id}` - Delete category.

---

## Products

- `POST /products` - Create product.
- `GET /products` - List products.
- `GET /products/{id}` - Retrieve product details.
- `PUT /products/{id}` - Update product.
- `DELETE /products/{id}` - Delete product.

---

## Sales

- `POST /sales` - Register a sale and update inventory.
- `GET /sales` - List sales.
- `GET /sales/{id}` - Retrieve sale details.
- `POST /sales/{id}/payments` - Register a payment for an existing sale.
- `GET /sales/{id}/payments` - List payments associated with a sale.

---

## Inventory

- `POST /inventory/losses` - Register inventory loss.
- `GET /inventory/losses` - List inventory losses.

---

## Reports

- `GET /reports/sales`
- `GET /reports/customer-balances`
- `GET /reports/inventory`
- `GET /reports/product-performance`
- `GET /reports/waste`