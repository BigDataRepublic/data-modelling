# Data Modelling

---


# Why?
- The design makes it easy to join data together
- Represent the data in a way tha t the stakeholders want

---

# Normalized (Inmon)
- Uses the normalized form for building entity structure, avoiding data redundancy as much as possible.
- Advantage of this top-down approach in database design is that it is robust to business changes and contains a dimensional perspective of data across data mart
- Querying becomes challenging as it includes numerous tables


---

# Star Schema (Kimball)

---


# Four-step dimensional design process
1. Select the business process
2. Declare the grain
3. Identify the dimensions
4. Identify the facts


---

# Dimension table structure
- Has a single primary key column
- Embedded as a foreign key in an associated fact table
- Usually flat, wide denormalized tables 
- Need a surrogate key, as dimension values can be updated. They can be simple integers


---

# Steps
1. Identify a fact
2. Determine dimensions (attributes and descriptions around a fact)
3. Create mart - which we want our end users to interact with more 

💡 The combination of a fact table with several dimension tables is called the start schema

---

# Facts
- Low granularity
- Keys
- Numeric Values

---

# Granularity
- Most important design step is declaring the fact able grain
- The business definition of what a single fact table record represents
- Build it on the lowest possible grain, meaning it cannot be divided any further
- Once the data is aggregated, you can not disaggregate it to a finer level
---

# Desiging the facts table
- You want many identifiers in your facts table, e.g. product_id, employee_id, customers etc.
- Allows you to join with dimension tables

---

# Determine the dimensions
- Will add context to a fact through attributes & descriptions
- Can be slowly changing, e.g. office location for an employee ❓ How do you handle that?
- Text based values or dates
- The primary key is embedded as a foreign key in any associated fact table
- Usually wide, flat denormalized tables with many low-cardinality text attributes 

---

# Conformed dimensions
- One dimension might be able to be joined with multiple facts table
- Guarantees that a single data item is used in a similar manner across all the facts
- Ensures that all departments work with the same data definitions
- Example: 'Customer ID' means the same thing across all the different datasets

--- 

# Surrogate key
- Unique records for records in a dimension table
- Data in dimension tables can change over time (slowy changing dimensions), surrogate keys provide a consistent and unchanging reference to each record

---

# Slowly changing dimensions

- How do you track changes in the dimension data stored in a data warehouse?
- There are different types of SCD's:
    - Type 1: Overwrite old data with new data
    - Type 2: keep historical data by adding new records with updated info
    - Type 3: Store the original and the current values in the same record

---

# Type 2

Example: An employee named John, with EmployeeID = 123, moves from 'Office A' to 'Office B'. Here's how you might implement this change with a SQL query:

First, update the current record for John to set its EndDate to the current date, indicating the end of this record's validity.

```sql
UPDATE Employee
SET EndDate = CURRENT_DATE
WHERE EmployeeID = 123 AND EndDate IS NULL;
```

Insert a new record with the updated info:

```sql
INSERT INTO Employee (EmployeeID, EmployeeName, OfficeLocation, StartDate, EndDate)
VALUES (123, 'John', 'Office B', CURRENT_DATE, NULL);
```

---

## How to join?

💡 On the Surrogate Key 😄

--- 

# Data Quality
- Test for uniqueness of the primary key and the surrogate key
- **Referential integrity**, make sure that all foreign keys in the fact table reference existing primary keys in the dimension tables
- Range or Domain Validity

---

# Bridge tables
- Allows you to handle many-to-many relationships
- E.g. products that fall in multiple categories


---

# Junk dimensions
- Used to handle and store miscellaneous data
- Common attributes are "IsPromotionalSale", "IsOnlinePurchase", or "HasWarranty"
- Do not want to place these in the facts table

# Create Marts
- Join facts & dims to create custom views/tables
- e.g. see total orders by product, customer etc.
- Used for reporting and analytics

---

# Benefits
- Common approach, well-documented & time-tested
- Capable of handling complex scenarios
- Provides clarity & stability to a data warehouse
- Fast to construct, no normalization required
- Easily to comprehened, simplifying querying and analysis

---

# Disadvantages
- Data isn't entirely integrated before reporting: no single source of truth

Not needed anymore for storage and computational reasons

---

# Data Vault Modelling

<img src="/Data_Vault_Example.png" alt="Extremely semplified example of Data Vault modelling"/>

