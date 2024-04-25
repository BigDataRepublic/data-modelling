---
fonts:
  sans: Quicksand
  weights: '300,400,500,600,700'
  provider: none

class: bg-red
---

<h1 style="color: white; margin-top: -80px; margin-left: -18px; font-weight:600">Data Modeling Techniques</h1>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Transactional vs Analytical Data Modeling</h1>

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
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">What Is Analytical Data Modeling</h1>

 <div>
  <p style="color: #00b9ad">
    <br><br>
   <h3>• Create a structured and organized representation of <b>data elements</b> and their <b>relationships</b> within a system</h3>
   <br><br>
   <h3>• Aims to support the organization objectives in analytical environments</h3>
  </p>
 </div>

---
class: bg-white

---
<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">What Is Analytical Data Modeling</h1>
<div>
  <h4 style="color: #0c2749; font-weight:400">Example: Imagine a table that records sales for products in various branches of a store 🏪</h4>
  <div>
    <br>
    <table border="1" style="color: #0c2749; font-weight:300">
    <thead>
      <tr>
        <th>BranchID</th>
        <th>BranchLocation</th>
        <th>ProductID</th>
        <th>ProductName</th>
        <th>ProductPrice</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>New York</td>
        <td>101</td>
        <td>Apple</td>
        <td>$1</td>
      </tr>
      <tr>
        <td>1</td>
        <td>New York</td>
        <td>102</td>
        <td>Banana</td>
        <td>$0.5</td>
      </tr>
      <tr>
        <td>2</td>
        <td>Los Angeles</td>
        <td>101</td>
        <td>Apple</td>
        <td>$1</td>
      </tr>
      <tr>
        <td>2</td>
        <td>Los Angeles</td>
        <td>103</td>
        <td>Cherry</td>
        <td>$2</td>
      </tr>
    </tbody>
    </table>
  </div>
</div>

---
class: bg-white

---
<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">What Is Analytical Data Modeling</h1>
<div>
  <h4 style="color: #0c2749; font-weight:400">Example: Imagine a table that records sales for products in various branches of a store 🏪</h4>
  <div>
    <br>
    <table border="1" style="color: #0c2749; font-weight:300">
    <thead>
      <tr>
        <th>BranchID</th>
        <th>BranchLocation</th>
        <th>ProductID</th>
        <th>ProductName</th>
        <th>ProductPrice</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>New York</td>
        <td>101</td>
        <td>Apple</td>
        <td>$1</td>
      </tr>
      <tr>
        <td>1</td>
        <td>New York</td>
        <td>102</td>
        <td>Banana</td>
        <td>$0.5</td>
      </tr>
      <tr>
        <td>2</td>
        <td>Los Angeles</td>
        <td>101</td>
        <td>Apple</td>
        <td>$1</td>
      </tr>
      <tr>
        <td>2</td>
        <td>Los Angeles</td>
        <td>103</td>
        <td>Cherry</td>
        <td>$2</td>
      </tr>
    </tbody>
    </table>
  </div>
  <p style="color: #00b9ad; margin-top: 4px;">
   <h4>In the table above ☝️</h4>
   <br>
   <h5 style="margin-top: -15px;">&nbsp;&nbsp;- <i>BranchLocation</i> is dependent on <i>BranchID</i>.</h5>
   <br>
   <h5 style="margin-top: -20px;">&nbsp;&nbsp;- <i>ProductName</i> and <i>ProductPrice</i> are dependent on <i>ProductID</i>.</h5>
  </p>
</div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Can We Make The Structure More Clear? 🤔</h1>

 <div>
  <br>
  <h4 style="color: #0c2749; font-weight:400">We can <b>normalize</b> the tables ➡️ divide into smaller, less redundant tables
</h4>
  <br>
  <table border="1" style="color: #0c2749; font-weight: 300;">
  <thead>
    <tr>
      <th>BranchID</th>
      <th>BranchLocation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>New York</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Los Angeles</td>
    </tr>
  </tbody>
  </table>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Can We Make The Structure More Clear? 🤔</h1>

 <div>
  <br>
  <h4 style="color: #0c2749; font-weight:400">We can <b>normalize</b> the tables ➡️ divide into smaller, less redundant tables
</h4>
  <br>
  <table border="1" style="color: #0c2749; font-weight: 300;">
  <thead>
    <tr>
      <th>ProductID</th>
      <th>ProductName</th>
      <th>ProductPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>101</td>
      <td>Apple</td>
      <td>$1</td>
    </tr>
    <tr>
      <td>102</td>
      <td>Banana</td>
      <td>$0.5</td>
    </tr>
    <tr>
      <td>103</td>
      <td>Cherry</td>
      <td>$2</td>
    </tr>
  </tbody>
</table>

 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Can We Make The Structure More Clear? 🤔</h1>

 <div>
  <br>
  <h4 style="color: #0c2749; font-weight:400">We can <b>normalize</b> the tables ➡️ divide into smaller, less redundant tables
</h4>
  <br>
  <table border="1" style="color: #0c2749; font-weight: 300; border-collapse: collapse;">
  <thead>
    <tr>
      <th>BranchID</th>
      <th>ProductID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>101</td>
    </tr>
    <tr>
      <td>1</td>
      <td>102</td>
    </tr>
    <tr>
      <td>2</td>
      <td>101</td>
    </tr>
    <tr>
      <td>2</td>
      <td>103</td>
    </tr>
  </tbody>
  </table>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Why Do We Model Data?</h1>

 <div>
  <br>
  <h3 style="color: #0c2749; font-weight:400">1️⃣ Clarity and understanding</h3>
  <p style="color: #00b9ad">
   • Normalization simplifies the database structure.
   <br><br>
   • It becomes easier to understand the relationships between different data entities.
  </p>
 </div>
 <div>
  <br>
  <h3 style="color: #0c2749; font-weight:400">2️⃣ Data Quality and Consistency</h3>
  <p style="color: #00b9ad">
   • Branch details are stored only once in the branch table, which reduces the risk of inconsistent data.
   <br><br>
   • Product details are similarly centralized, ensuring that any updates to a product's price or name need only be made in one place, thereby maintaining consistency
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Why Do We Model Data?</h1>

 <div>
  <br>
  <h3 style="color: #0c2749; font-weight:400">3️⃣ Efficient Data Management</h3>
  <p style="color: #00b9ad">
   • Queries related to specific entities become faster and less complex.
   <br><br>
   • Operations like updates, inserts, and deletions are more efficient.
  </p>
 </div>
 <div>
  <br>
  <h3 style="color: #0c2749; font-weight:400">4️⃣ Facilitates Data Integration</h3>
  <p style="color: #00b9ad">
   • As the organization grows (e.g., opening new branches or expanding product lines), the database can easiliy accommodate new data.
   <br><br>
   • Adjustments to the database (like adding new attributes to entities) can be managed with minimal disruption.
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Let's introduce a few more concepts 💡 </h1>

 <div>
  <p style="color: #00b9ad">
  <br><br>
  <h2>• Data Warehouse</h2>
  <br><br>
  <h2>• Data Mart</h2>
  <br><br>
  <h2>• Data Lake</h2>
  </p>
 </div>
 
---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Data Warehouse</h1>

 <div>
  <p style="color: #00b9ad">
    <br><br>
   <h2>• A centralized storage to support all business intelligence (BI) activities</h2>
   <br><br>
   <h2>• Stores current and historical data from various sources</h2>
    <br><br>
   <h2>• Optimized for query and analysis</h2>
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Data Warehouse</h1>
<br>
<img src="/data-warehousing.png" alt="Data Warehousing graph" width="85%" style="display: block; margin: auto;">

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">In Practice...</h1>
<br>
<h2 style="color: #0c2749; margin-left: -15px; font-weight:600">Put another SQL database "on top" of your production DB's (which are the data sources)</h2>
<br>
<h3 style="color: #00b9ad; margin-left: -15px; font-weight:600">E.g. a Bigquery database on top of Postgres</h3>
<br>
<h2 style="color: #0c2749; margin-left: -15px; font-weight:600">🎯 Goals?</h2>
 <div>
  <p style="color: #00b9ad">
   <h4 style="margin-top: 15px;">• <b>Consolidation</b>: Brings data from diverse sources into one unified view.</h4>
   <h4 style="margin-top: 5px;">• <b>Reporting & Analysis</b>: Supports complex queries and reporting.</h4>
   <h4 style="margin-top: 5px;">• <b>Historical Insight</b>: Maintains historical data for trend analysis.</h4>
   <h4 style="margin-top: 5px;">• <b>Data Integrity</b>: Ensures consistent, clean, and reliable data.</h4>
  </p>
 </div>

---

# 🔑 Key features
- **Subject-Oriented**: Organized around subjects like sales, products, or customers.
- **Integrated**: Data is consistent across all subjects.
- **Time-Variant**: Historical data is kept for analysis over time.
- **Non-Volatile**: Once data is in the warehouse, it doesn't change. (just keep appending)

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

# Okay but how do we actually go about building our warehouse and marts?

- **Requirements analysis:** what do the stakeholders want to derive from the data? 
- **Understand your sources**: find all of the companies data. Work out what is useful and what is not
- **Data Modeling**: decide how you are going to model the data

---

# Inmon approach
Bill Inmon is the father of data warehousing

<img src="/inmon.png" alt="Inmon"/>


---

# How?
- Normalized to the third normal form (3NF)
- Create the data warehouse
- Then build the marts ➡️ top down approach

---

<img src="/top_vs_bottom_wh.png" alt="Data Warehousing graph"/>

---

# Normalized (Inmon)
- **Normalized**
- **Single source of truth** for the entire organization
- **Robust to business changes** 
- Upfront investment in planning and resources
- **Querying becomes challenging** ==> a lot of joins

---

# Star Schema (Kimball)

<img src="/Ralph.jpg" alt="Ralph Kimball"/>

---

# His family

<img src="/kimball_group.png" alt="Kimball Group"/>

---

<img src="/star_schema.jpeg" alt="Star Schema"/>

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

💡 The combination of a fact table with several dimension tables is called the star schema

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

# Kimball

In this simplified model:
- The Campaign Performance table provides **metrics** on how each campaign performed on a given date.
- The Campaign Details table provides **additional context** about each campaign, such as its duration, target audience, and channel.

Allows marketing teams to quickly see how each campaign is performing and understand the context behind each campaign.

---

# ❓ What are the benefits?
- Simple
- Query simplicity
- Great for analysis (focus on the BI side)

---

# Conformed dimensions (used for integrating data)
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

---

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

# Disadvantages
- Data isn't entirely integrated before reporting: no single source of truth
- Redundant data can be added to tables

---

# ❓ Which one do you choose?

---

# Time to value ⏰

**Kimball**:
- Faster initial results due to focus on specific business needs.
- Delivers value iteratively.

**Inmon**:
- Longer initial setup due to comprehensive EDW design.
- Value realized when EDW is established and data marts are derived.

---

# Complexity & Integration ⚙️

**Kimball**:
- Initial setup is simpler.
- Complexity can arise when integrating multiple data marts.

**Inmon**:
- Initial design is complex due to enterprise-wide considerations.
- Integration is inherent, as data marts are derived from a unified EDW.

---

# Flexibility vs. Consistency 💪

**Kimball**:
- More flexible to departmental needs.
- Risk of inconsistencies across data marts.

**Inmon**:
- Consistent data model across the organization.
- Less flexibility for department-specific nuances.

---

# Maintenance & Scalability 👩‍🔧

**Kimball**:
- Maintenance can be challenging when integrating or changing multiple data marts.
- Scalable in terms of adding new data marts.

**Inmon**:
- Centralized maintenance at the EDW level.
- Scalability requires changes to the central EDW, but data marts can be easily derived.

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

