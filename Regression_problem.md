# Retail Sales Forecasting: Problem Statement

## 1. Business Context
In retail, accurate store-level sales forecasting is critical for inventory planning, logistics, staffing, and promotional marketing. Retail leadership wants to understand **what factors drive store revenue** and needs a machine learning model to **forecast total monthly sales** for any store before the month begins.

---

## 2. Machine Learning Formulation
* **Unit of Analysis**: Store-Month (one observation per store per year-month).
* **Target Variable ($y$)**: `total_sales` (Total monthly net sales in INR).
* **Predictor Features ($X$)**: 
  * Store attributes (size in sqft, format, location type, competition, footfall).
  * Calendar & Seasonality (month, festive days, weekend days, days in month).
  * Promotional campaigns (active days of BOGO, Festive Bonanza, Clearance, etc.).
* **Forbidden Features (Data Leakage)**: `total_transactions`, `total_items`, and `total_discount` cannot be used as features because they are outcomes that are only known after the month has concluded.

---

## 3. Data Sources
The dataset covers 50 stores over a 5-year timeline (2021–2025) across 5 core tables:
1. **`TRANSACTIONS.csv`**: Over 6 million raw point-of-sale transactions.
2. **`STORES.csv`**: Store characteristics, locations, competition, and footfall (includes missing values).
3. **`CALENDAR.csv`**: Dates with weekend flags and festive period indicators.
4. **`PROMOTIONS.csv`**: Master list of discount schemes and promo categories.
5. **`STORE_PROMOTIONS.csv`**: Active campaign schedules per store.

*(Data can be loaded locally from `raw_data/` or downloaded via Google Drive in Google Colab).*
