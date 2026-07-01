# BiteTrack API Design

## Endpoints Specification

### Authentication
- `POST /auth/register` - Create user.
- `POST /auth/token` - Authenticate user & issue JWT Access & Refresh Tokens.
- `POST /auth/refresh` - Rotate access tokens using HttpOnly Refresh Cookie.

### Users & Profiles
- `GET /users/me` - Fetch own profile.
- `PATCH /users/me` - Update own profile.
- `GET /users` - List all users (Admin only).

### Categories
- `POST /categories` - Create category.
- `GET /categories` - List categories (with pagination).
- `GET /categories/{id}` - Retrieve category detail.
- `PUT /categories/{id}` - Update category.
- `DELETE /categories/{id}` - Delete category.

### Products
- `POST /products` - Create product.
- `GET /products` - List products (with text search, category filters, and pagination).
- `GET /products/{id}` - Retrieve product details.
- `PUT /products/{id}` - Update product attributes.
- `DELETE /products/{id}` - Delete product.

### Orders
- `POST /orders` - Place order (adjusts stock level inside database transaction).
- `GET /orders` - List orders.
- `GET /orders/{id}` - Retrieve order details.
- `PATCH /orders/{id}/status` - Cancel or process order (Admin/Worker only).
