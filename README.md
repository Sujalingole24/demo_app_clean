# demo_app

A custom Frappe app to manage serial number generation with full support for Auto Generate, Use Existing, and Based on Raw Material modes.

---

## Features

- Generate serial numbers intelligently through the `Serial Voucher` Doctype
- 3 generation types:
  - Auto Generate
  - Use Existing
  - Based on Raw Material (linked with Work Order)
- Integrated child table: `Serial Voucher Detail`
- Naming Series applied (`SV-YYYY-#####`)
- Clean backend logic using `before_save` hook
- Fully exportable via fixtures

---

## Doctypes

### Serial Voucher (Parent)
- `item` (Link: Item)
- `quantity` (Int)
- `generate_type` (Select: Auto Generate / Use Existing / Based on Raw Material)
- `work_order` (Link: Work Order)
- `serial_numbers` (Child Table: Serial Voucher Detail)

### Serial Voucher Detail (Child)
- `serial_number` (Data)
- `item` (Link: Item)
- `existing_serial` (Link: Serial No)

---

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
# Go to your bench directory
cd frappe-bench

# Clone the app
git clone https://github.com/<your-username>/demo_app.git apps/demo_app

# Install the app
bench --site your-site-name install-app demo_app

# Migrate to apply changes
bench --site your-site-name migrate

