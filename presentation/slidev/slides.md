---
fonts:
  sans: Quicksand
  weights: '300,400,500,600,700'
  provider: none

class: bg-red
---

<h1 style="color: white; margin-top: -80px; margin-left: -18px; font-weight:600">Data Modelling Techniques</h1>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Transactional vs Analytical Data Modelling</h1>

<div class="grid-container">
 <div>
  <p style="color: #00b9ad">
   • Designed primarily for daily operations and transactions in businesses like sales, inventory management, and customer service.
   <br><br>
   • Highly normalized with many tables to reduce data redundancy and improve data integrity.
   <br><br>
   • Optimized for fast data insertion, update, and retrieval operations to support real-time transaction processing.
   <br><br>
   • E.G. Order processing systems, inventory management systems, and customer relationship management (CRM) systems.
  </p>
 </div>
 <div>
  <p style="color: #00b9ad">
   • Designed for analysis and decision-making, often used in data warehousing and business intelligence applications.
   <br><br>
   • Uses denormalized schemas like star schema or snowflake schema, allowing for complex queries and aggregations.
   <br><br>
   • Optimized for complex queries, large-scale data aggregation, and analytical processing.
   <br><br>
   • E.G. Data warehouses, online analytical processing (OLAP) systems, and big data analytics platforms.
  </p>
 </div>
</div>

---

# What is analytical data modeling?
- Create a structured and organized representation of **data elements** and their **relationships** within a system
- Serves as a **blueprint**  for how data is collected, stored, managed, used within databases
- Aims to support the organization objectives in both operational and analytical environments

---

Example: Imagine a table that records sales for products in various branches of a store 🏪:

| BranchID | BranchLocation | ProductID | ProductName | ProductPrice |
|----------|----------------|-----------|-------------|--------------|
| 1        | New York       | 101       | Apple       | $1           |
| 1        | New York       | 102       | Banana      | $0.5         |
| 2        | Los Angeles    | 101       | Apple       | $1           |
| 2        | Los Angeles    | 103       | Cherry      | $2           |

---

Example: Imagine a table that records sales for products in various branches of a store 🏪:

| BranchID | BranchLocation | ProductID | ProductName | ProductPrice |
|----------|----------------|-----------|-------------|--------------|
| 1        | New York       | 101       | Apple       | $1           |
| 1        | New York       | 102       | Banana      | $0.5         |
| 2        | Los Angeles    | 101       | Apple       | $1           |
| 2        | Los Angeles    | 103       | Cherry      | $2           |

In the table above ☝️
- BranchID and ProductID together can be considered as the composite primary key.
- BranchLocation is dependent on BranchID.
- ProductName and ProductPrice are dependent on ProductID.

---

# 🤔 How could we model this to make the structures more clear?

---

# 🤔 How could we model this to make the structures more clear?

We can **normalize** the tables ➡️ divide into smaller, less redundant tables


| BranchID | BranchLocation |
|----------|----------------|
| 1        | New York       |
| 2        | Los Angeles    |

---

| ProductID | ProductName | ProductPrice |
|-----------|-------------|--------------|
| 101       | Apple       | $1           |
| 102       | Banana      | $0.5         |
| 103       | Cherry      | $2           |

---

| BranchID | ProductID |
|----------|-----------|
| 1        | 101       |
| 1        | 102       |
| 2        | 101       |
| 2        | 103       |

---

# Why do we model data?

### 1️⃣ Clarity and understanding:
- Normalization simplifies the database structure. 
- It becomes easier to understand the relationships between different data entities.

---

# Why do we model data?

### 2️⃣ Data Quality and Consistency:
- Branch details are stored only once in the branch table, which reduces the risk of inconsistent data (e.g., having different spellings for the same branch location in multiple records).
- Product details are similarly centralized, ensuring that any updates to a product's price or name need only be made in one place, thereby maintaining consistency across all entries that reference the product.

---

# Why do we model data?

### 3️⃣ Efficient Data Management:
- Queries related to specific entities (like all products sold at a branch or all branches selling a particular product) become faster and less complex because the data is segmented and indexed more effectively.
- Operations like updates, inserts, and deletions are more efficient because they are localized to specific, smaller tables rather than a large, monolithic table.

---

# Why do we model data?

### 4️⃣ Facilitates Data Integration:
- Integrating data from different sources (like merging another set of branch and product data from a different system) becomes easier because the structure dictates where and how new data fits into the existing schema.
- It supports the use of standard interfaces for database interactions, which is crucial when combining data from disparate systems or preparing for enterprise-level data analysis

---

# Why do we model data?

### 5️⃣ Facilitates Data Integration:
- As the organization grows (e.g., opening new branches or expanding product lines), the database can accommodate new data without significant restructuring.
- Adjustments to the database (like adding new attributes to entities) can be managed with minimal disruption to the existing database operations.

---

# 💡 Let's introduce a few more concepts
- Data Warehouse
- Data Mart
- Data Lake

---

# Data Warehouse
- A centralized repository to support business intelligence (BI) activities
- Stores current and historical data from various sources
- Optimized for query and analysis

---

<img src="/data-warehousing.png" alt="Data Warehousing graph"/>

---

# In practice
Put another SQL database on top of your production DB (which are the data sources)

E.g. a Bigquery database on top of Postgres

---

# 🎯 Goals?
- **Consolidation**: Brings data from diverse sources into one unified view.
- **Reporting & Analysis**: Supports complex queries and reporting.
- **Historical Insight**: Maintains historical data for trend analysis.
- **Data Integrity**: Ensures consistent, clean, and reliable data.

---

# 🔑 Key features
- **Subject-Oriented**: Organized around subjects like sales, products, or customers.
- **Integrated**: Data is consistent across all subjects.
- **Time-Variant**: Historical data is kept for analysis over time.
- **Non-Volatile**: Once data is in the warehouse, it doesn't change.

---

# What is a data mart?
- A subset of the data warehouse
- Normally related to a specific team in the business (for example marketing)
- Only provides the data related to this business unit

---

# Why do we break down the warehouse like this?
- **Performance**: Faster query performance due to reduced data volume.
- **Agility**: Quicker to build and modify.
- **User-Friendly**: Tailored to specific business unit needs, making it more intuitive.

---

# What problems do you think arise with data marts?
- Data consistency: Ensuring data in the data mart is consistent with other marts and the main warehouse.
- Maintenance: Keeping the data mart updated as business needs evolve.
- Integration: If starting with independent data marts, integrating them can be challenging.

---

# Okay but how do we actually go about building our warehouse and marts?
--> data modelling

---

# But before that...

Step by step:
- Requirements analysis: what do the stakeholders want to derive from the data? Can be very laborious if the comapny is large
- Understand your sources: find all of the companies data. Work out what is useful and what is not
- Data Modelling: decide how you are going to model the data

---

# Inmon approach
Bill Inmon is the father of data warehousing

---

# How?
- Normalized to the third normal form (3NF), which is the type of normalization that we saw in our first example
- Create the data warehouse
- Then build the marts ➡️ this is a top down approach

---

<img src="/top_vs_bottom_wh.png" alt="Data Warehousing graph"/>

---

# Normalized (Inmon)
- Uses the normalized form for building entity structure, **avoiding data redundancy** as much as possible.
- Single source of truth for the entire organization
- Advantage of this top-down approach in database design is that it is **robust to business changes** and contains a dimensional perspective of data across data mart
- Requires a more substantial upfront investment in planning and resources
- **Querying becomes challenging** as it includes numerous tables

---

# Star Schema (Kimball)

---

# Four-step dimensional design process
1. Select the business process
2. Declare the grain
3. Identify the dimensions
4. Identify the facts

---


# Steps
1. Identify a fact
2. Determine dimensions (attributes and descriptions around a fact)
3. Create mart - which we want our end users to interact with more 

💡 The combination of a fact table with several dimension tables is called the start schema

---

# Facts


| Date       | CampaignName | Impressions | Clicks | Conversions | Spend |
|------------|--------------|-------------|--------|-------------|-------|
| 2023-09-10 | Summer Sale  | 10,000      | 1,000  | 100         | $500  |
| 2023-09-11 | Fall Launch  | 15,000      | 1,500  | 150         | $750  |

<br>

- Low granularity
- Contains identifiers that allow you to join with dimension tables
- Numeric Values

---

# Granularity
- Most important design step is declaring the fact able grain
- The business definition of what a single fact table record represents
- Build it on the **lowest possible grain**, meaning it cannot be divided any further
- Once the data is aggregated, you can not disaggregate it to a finer level

---

# Dimension table structure

| CampaignName | StartDate  | EndDate    | TargetAudience | Channel  |
|--------------|------------|------------|----------------|----------|
| Summer Sale  | 2023-09-01 | 2023-09-30 | Ages 18-25     | Facebook |
| Fall Launch  | 2023-09-10 | 2023-10-10 | Ages 25-35     | Email    |

<br>

- Will add context to a fact through attributes & descriptions
- Can be slowly changing, e.g. office location for an employee ❓ How do you handle that?
- Has a single primary key column
- Embedded as a foreign key in an associated fact table
- Usually flat, wide denormalized tables 
- Need a surrogate key, as dimension values can be updated. They can be simple integers

---

In this simplified model:

- The Campaign Performance table provides metrics on how each campaign performed on a given date.
- The Campaign Details table provides additional context about each campaign, such as its duration, target audience, and channel.

This model allows marketing teams to quickly see how each campaign is performing and understand the context behind each campaign.

# ❓ What are the benefits?

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

# Data Quality
- Test for uniqueness of the primary key and the surrogate key
- **Referential integrity**, make sure that all foreign keys in the fact table reference existing primary keys in the dimension tables
- Range or Domain Validity

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

---

# Data Vault Modeling
Invented by Dan Linstedt (1990s) / Inspired by complex networks found in Nature

### Networks Topology:
- <span style="color:red">_**hubs**_</span> (such as persons or other objects) &#8594; Business Keys
- <span style="color:green">_**links**_</span> between those objects &#8594; Business Processes / Relationships between business keys
- <span style="color:yellow">_**information**_</span> that describes the context of the objects &#8594 Attributes of a business key or relationship


---

# Data Vault Modeling

Simple example

<img src="/Data_Vault_Example.png" alt="Extremely semplified example of Data Vault modelling"/>

