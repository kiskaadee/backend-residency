# Database Design

## Planned Domain Model

```mermaid
erDiagram

USER {
    uuid id PK
    string email UK
    string password_hash
    string role
    boolean is_active
    datetime created_at
}

CUSTOMER {
    uuid id PK
    string name
    string phone
    string email
    datetime created_at
}

CATEGORY {
    uuid id PK
    string name
    string description
}

PRODUCT {
    uuid id PK
    string name
    string sku UK
    string description
    decimal unit_price
    int stock_level
    int shelf_life_days
}

SALE {
    uuid id PK
    uuid customer_id FK
    uuid created_by FK
    decimal total_amount
    datetime created_at
}

SALE_ITEM {
    uuid id PK
    uuid sale_id FK
    uuid product_id FK
    int quantity
    decimal unit_price
}

PAYMENT {
    uuid id PK
    uuid sale_id FK
    decimal amount
    string payment_method
    datetime paid_at
}

INVENTORY_LOSS {
    uuid id PK
    uuid product_id FK
    int quantity
    string reason
    datetime created_at
}

CATEGORY ||--o{ PRODUCT : contains

CUSTOMER ||--o{ SALE : places

USER ||--o{ SALE : records

SALE ||--|{ SALE_ITEM : contains

SALE ||--o{ PAYMENT : receives

PRODUCT ||--o{ SALE_ITEM : sold_as

PRODUCT ||--o{ INVENTORY_LOSS : discarded
```

## Notes

- Outstanding customer balances are **derived** from sales and payments rather than stored directly.
- A sale may receive multiple payments.
- Product stock is maintained as a `stock_level` field during the initial project milestones.
- Inventory losses represent products removed from inventory without completing a sale.
- Payment status is derived (calculated field) from recorded payments rather than stored explicitly.