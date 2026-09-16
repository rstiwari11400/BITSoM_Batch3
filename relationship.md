# Relational Schema & Table Relationships

This document outlines the structure and relationships of the retail dataset.

## ER Diagram

```mermaid
erDiagram
    STORES ||--o{ TRANSACTIONS : "generates"
    STORES ||--o{ STORE_PROMOTIONS : "has"
    PROMOTIONS ||--o{ STORE_PROMOTIONS : "deployed_at"
    PROMOTIONS ||--o{ TRANSACTIONS : "applied_to"
    CALENDAR ||--o{ TRANSACTIONS : "happens_on"

    STORES {
        string store_id PK
        string city
        string state
        string location_type
        string store_format
        int store_size_sqft
        date launch_date
        int competition_density
        int avg_monthly_footfall
        string zone
    }

    PROMOTIONS {
        string promo_id PK
        string promo_type
        string promo_description
        string target_category
        boolean is_national_promo
    }

    STORE_PROMOTIONS {
        string store_id FK
        string promo_id FK
        date start_date "Store Specific Start"
        date end_date "Store Specific End"
    }

    TRANSACTIONS {
        string transaction_id PK
        string store_id FK
        string promo_id FK
        string customer_id
        datetime transaction_date
        float gross_bill_value
        float net_bill_value
        int total_items
        float promo_discount_amount
        string payment_mode
        string category_mix
    }

    CALENDAR {
        date date PK
        boolean is_weekend
        boolean is_festive_period
        string festival_name
        int month
        int year
    }
```

## Table Relationships

1.  **STORES ↔ TRANSACTIONS** (One-to-Many)
    *   A single store generates many transactions.
    *   `TRANSACTIONS.store_id` references `STORES.store_id`.

2.  **PROMOTIONS ↔ TRANSACTIONS** (One-to-Many)
    *   A single promotion can be applied to many transactions.
    *   `TRANSACTIONS.promo_id` references `PROMOTIONS.promo_id`.
    *   *Note*: Not all transactions have a promotion (`promo_id` can be NULL).

3.  **STORES ↔ STORE_PROMOTIONS** (One-to-Many)
    *   A store can have multiple active promotions over time.
    *   `STORE_PROMOTIONS.store_id` references `STORES.store_id`.

4.  **PROMOTIONS ↔ STORE_PROMOTIONS** (One-to-Many)
    *   A specific promotion type (e.g., "Diwali Sale") is deployed across multiple stores.
    *   `STORE_PROMOTIONS.promo_id` references `PROMOTIONS.promo_id`.

5.  **CALENDAR ↔ TRANSACTIONS** (One-to-Many)
    *   Each transaction occurs on a specific date found in the calendar.
    *   `TRANSACTIONS.transaction_date` aligns with `CALENDAR.date`.

## Key Constraints
*   **Promo Validity**: A transaction with `promo_id = X` at `store_id = Y` on `date = D` is only valid if there exists a record in `STORE_PROMOTIONS` where:
    *   `store_id = Y`
    *   `promo_id = X`
    *   `start_date <= D <= end_date`
