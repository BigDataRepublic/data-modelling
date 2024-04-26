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

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">What Is Data Modeling</h1>

 <div>
  <p style="color: #00b9ad">
    <br><br>
   <h3>• Create a structured and organized representation of <b>data elements</b> and their <b>relationships</b> within a system</h3>
   <br><br>
   <h3>• Aims to support the organization objectives in analytical and operational environments</h3>
  </p>
 </div>

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
<h2 style="color: #0c2749; margin-left: -15px; font-weight:600">🎯 Goals</h2>
 <div>
  <p style="color: #00b9ad">
   <h4 style="margin-top: 15px;">• <b>Consolidation</b>: Brings data from diverse sources into one unified view.</h4>
   <h4 style="margin-top: 5px;">• <b>Reporting & Analysis</b>: Supports complex queries and reporting.</h4>
   <h4 style="margin-top: 5px;">• <b>Historical Insight</b>: Maintains historical data for trend analysis.</h4>
   <h4 style="margin-top: 5px;">• <b>Data Integrity</b>: Ensures consistent, clean, and reliable data.</h4>
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Data Mart</h1>

 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• A subset of the data warehouse</h3>
   <br>
   <h3>• Normally related to a specific team in the business (for example marketing)</h3>
    <br>
   <h3>• Only provides the data related to this business unit</h3>
  </p>
 </div>

<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Why do we break down the warehouse like this?</h2>
 <div>
  <p style="color: #00b9ad">
   <h4 style="margin-top: 15px;">• <b>Performance</b>: Faster query performance due to reduced data volume.</h4>
   <h4 style="margin-top: 5px;">• <b>Agility</b>: Quicker to build and modify.</h4>
   <h4 style="margin-top: 5px;">• <b>User-Friendly</b>: Tailored to specific business unit needs, making it more intuitive.</h4>
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Data Mart</h1>

 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• A subset of the data warehouse</h3>
   <br>
   <h3>• Normally related to a specific team in the business (for example marketing)</h3>
    <br>
   <h3>• Only provides the data related to this business unit</h3>
  </p>
 </div>

<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Okay, but how do we actually go about building our warehouse and marts?</h2>
 <div>
  <p style="color: #00b9ad">
   <h4 style="margin-top: 15px;">• <b>Requirements analysis</b>: what do the stakeholders want to derive from the data?</h4>
   <h4 style="margin-top: 5px;">• <b>Understand your sources</b>: Find all of the companies data. What is useful and what is not.</h4>
   <h4 style="margin-top: 5px;">• <b>Data Modeling</b>: Decide how you are going to model the data.</h4>
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Inmon Approach</h1>

<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Bill Inmon is the father of data warehousing</h2>

<img src="/inmon.png" alt="Bill Inmon" style="margin-top: 20px"/>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Inmon Approach</h1>

<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Bill Inmon is the father of data warehousing</h2>

<div class="grid-container">
<img src="/top_vs_bottom_wh.png" alt="Data Warehousing graph"/>
<div>
  <h4 style="color: #0c2749; margin-left: -15px; margin-top:-5px; font-weight:300">⬆️ Single <b>source of truth</b> for the entire organization.</h4>
  <h4 style="color: #0c2749; margin-left: -15px; margin-top:2px; font-weight:300">⬆️ <b>Robust to business changes.</b></h4>
  <h4 style="color: #0c2749; margin-left: -15px; margin-top:2px; font-weight:300">⬇️ Upfront investment in planning and resources.</h4>
  <h4 style="color: #0c2749; margin-left: -15px; margin-top:2px; font-weight:300">⬇️ <b>Querying becomes challenging</b> ==> a lot of joins.</h4>
  
  <h2 style="color: #0c2749; margin-left: -15px; margin-top:10px; font-weight:400">How?</h2>
  <p style="color: #00b9ad; margin-top: -2px">
   • Normalize to the third normal form (3NF).
   <br>
   • Create the data warehouse.
   <br>
   • Then build the marts ➡️ top down approach.
  </p>
 </div>

</div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Kimball Approach</h1>

<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Ralph Kimball is the father of Dimensional Modeling</h2>

<div class="grid-container">
<div>
<img src="/Ralph.jpg" alt="Ralph Kimball" style="margin-left: 15px; margin-top: -5px" width="55%"/>
</div>
<div>
<img src="/kimball_group.png" alt="Kimball Group" style="margin-top: -5px" width="67%"/>
</div>
</div>

---
class: bg-white

---
<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Kimball Approach</h1>
<h4 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">💡 The combination of a fact table with several dimension tables is called the <b>star schema</b></h4>

<div class="grid-container">
<div>
  <p style="color: #0c2749; margin-top: -4px;">
   <h4>Four-step dimensional design process</h4>
   <br>
   <h5 style="color: #00b9ad; margin-top: -15px;">&nbsp;&nbsp;- Select the business process.</h5>
   <br>
   <h5 style="color: #00b9ad; margin-top: -20px;">&nbsp;&nbsp;- Declare the grain.</h5>
   <br>
   <h5 style="color: #00b9ad; margin-top: -20px;">&nbsp;&nbsp;- Identify the dimensions.</h5>
   <br>
   <h5 style="color: #00b9ad; margin-top: -20px;">&nbsp;&nbsp;- Identify the facts.</h5>
  </p>
</div>
<div>
<img src="/star_schema.jpeg" alt="Star Schema" width="100%" style="display: block; margin: auto; margin-top:10px;"/>
</div>
</div>

---
class: bg-white

---
<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Kimball Approach</h1>
<h4 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">💡 The combination of a fact table with several dimension tables is called the <b>star schema</b></h4>

<div class="grid-container">
<div>
  <p style="color: #0c2749; margin-top: -4px;">
   <h4>Four-step dimensional design process</h4>
   <br>
   <h5 style="color: #00b9ad; margin-top: -15px;">&nbsp;&nbsp;- Select the business process.</h5>
   <br>
   <h5 style="color: #00b9ad; margin-top: -20px;">&nbsp;&nbsp;- Declare the grain.</h5>
   <br>
   <h5 style="color: #00b9ad; margin-top: -20px;">&nbsp;&nbsp;- Identify the dimensions.</h5>
   <br>
   <h5 style="color: #00b9ad; margin-top: -20px;">&nbsp;&nbsp;- Identify the facts.</h5>
  </p>
</div>
<div>
<img src="/star_schema.jpeg" alt="Star Schema" width="100%" style="display: block; margin: auto; margin-top:10px;"/>
</div>
</div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Granularity</h1>

 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• Most important design step is declaring the fact table grain.</h3>
   <br>
   <h3>• The business definition of what a single fact table record represents.</h3>
   <br>
   <h3>• Build it on the <b>lowest possible grain</b>, meaning it cannot be divided any further</h3>
   <br>
   <h3>• Once the data is aggregated, you can not disaggregate it to a finer level</h3>
  </p>
 </div>


---
class: bg-white

---
<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Facts Table: CampaignPerformance</h1>
<div>
  <h4 style="color: #0c2749; font-weight:400"></h4>
  <div>
    <br>
<table border="1" style="color: #0c2749; font-weight: 300; border-collapse: collapse;">
  <thead>
    <tr>
      <th>Date</th>
      <th>CampaignName</th>
      <th>Impressions</th>
      <th>Clicks</th>
      <th>Conversions</th>
      <th>Spend</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-09-10</td>
      <td>Summer Sale</td>
      <td>10,000</td>
      <td>1,000</td>
      <td>100</td>
      <td>$500</td>
    </tr>
    <tr>
      <td>2023-09-11</td>
      <td>Fall Launch</td>
      <td>15,000</td>
      <td>1,500</td>
      <td>150</td>
      <td>$750</td>
    </tr>
  </tbody>
</table>
  </div>
  <p style="color: #00b9ad; margin-top: 4px;">
   <br>
   <h4 style="margin-top: 1px;">&nbsp;&nbsp;- Contains identifiers that allow you to join with dimension tables.</h4>
   <br>
   <h4 style="margin-top: 1px;">&nbsp;&nbsp;- Numeric Values.</h4>
  </p>
</div>

---
class: bg-white

---
<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Dimension Table: CampaignDetails</h1>
<div>
  <h4 style="color: #0c2749; font-weight:400"></h4>
  <div>
    <br>
<table border="1" style="color: #0c2749; font-weight: 300; border-collapse: collapse;">
  <thead>
    <tr>
      <th>CampaignName</th>
      <th>StartDate</th>
      <th>EndDate</th>
      <th>TargetAudience</th>
      <th>Channel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Summer Sale</td>
      <td>2023-09-01</td>
      <td>2023-09-30</td>
      <td>Ages 18-25</td>
      <td>Facebook</td>
    </tr>
    <tr>
      <td>Fall Launch</td>
      <td>2023-09-10</td>
      <td>2023-10-10</td>
      <td>Ages 25-35</td>
      <td>Email</td>
    </tr>
  </tbody>
</table>
  </div>
  <p style="color: #00b9ad; margin-top: 4px;">
   <h4 style="margin-top: 15px;">&nbsp;&nbsp;- Will add context to a fact through attributes & descriptions.</h4>
   <h4 style="margin-top: 4px;">&nbsp;&nbsp;- Has a single primary key column.</h4>
   <h4 style="margin-top: 4px;">&nbsp;&nbsp;- Embedded as a foreign key in an associated fact table.</h4>
   <h4 style="margin-top: 4px;">&nbsp;&nbsp;- Usually flat, wide denormalized tables.</h4>
   <h4 style="margin-top: 4px;">&nbsp;&nbsp;- Need a surrogate key, as dimension values can be updated. They can be simple integers.</h4>
  </p>
</div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Kimball</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">In this simplified model:</h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• The CampaignPerformance table provides <b>metrics</b> on how each campaign performed on a given date.</h3>
   <br>
   <h3>• The CampaignDetails table provides <b>additional context</b> about each campaign, such as its duration, target audience, and channel.</h3>
    <br>
   <h3>• Allows marketing teams to quickly see how each campaign is performing and understand the context behind each campaign.</h3>
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">What Are The Benefits ❓</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">In this simplified model:</h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• Simple.</h3>
   <br>
   <h3>• Query simplicity.</h3>
    <br>
   <h3>• Great for analysis (focus on the BI side).</h3>
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Conformed Dimensions</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Used for integrating data:</h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• One dimension might be able to be joined with multiple facts table.</h3>
   <br>
   <h3>• Guarantees that a single data item is used in a similar manner across all the facts.</h3>
   <br>
   <h3>• Ensures that all departments work with the same data definitions.</h3>
   <br>
   <h3>• Example: 'CustomerID' means the same thing across all the different datasets.</h3>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Surrogate Key</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400"></h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• Unique records for records in a dimension table.</h3>
   <br>
   <h3>• Data in dimension tables can change over time (slowy changing dimensions), surrogate keys provide a consistent and unchanging reference to each record.</h3>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Slowly Changing Dimensions</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">How do you track changes in the dimension data stored in a data warehouse?</h2>
<br>
<h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">There are different types of SCD's:</h3>

 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h4>• Type 1: Overwrite old data with new data.</h4>
   <br>
   <h4>• Type 2: keep historical data by adding new records with updated info.</h4>
   <br>
   <h4>• Type 3: Store the original and the current values in the same record.</h4>
  </p>
 </div>

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Type 2</h1>

<h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Example: An employee named John, with EmployeeID = 123, moves from 'Office A' to 'Office B'. Here's how you might implement this change with a SQL query.</h3>

<h4 style="color: #00b9ad; margin-left: -15px; margin-top:30px; font-weight:400">First, update the current record for John to set its EndDate to the current date, indicating the end of this record's validity:</h4>

```sql
UPDATE Employee
SET EndDate = CURRENT_DATE
WHERE EmployeeID = 123 AND EndDate IS NULL;
```
<h4 style="color: #00b9ad; margin-left: -15px; margin-top:30px; font-weight:400">Insert a new record with the updated info:</h4>
```sql
INSERT INTO Employee (EmployeeID, EmployeeName, OfficeLocation, StartDate, EndDate)
VALUES (123, 'John', 'Office B', CURRENT_DATE, NULL);
```

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Data Quality</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400"></h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• Test for uniqueness of the primary key and the surrogate key.</h3>
   <br>
   <h3>• <b>Referential integrity</b>, make sure that all foreign keys in the fact table reference existing primary keys in the dimension tables.</h3>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Junk Dimensions</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400"></h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• Used to handle and store miscellaneous data.</h3>
   <br>
   <h3>• Common attributes are "IsPromotionalSale", "IsOnlinePurchase", or "HasWarranty".</h3>
   <br>
   <h3>• Do not want to place these in the facts table.</h3>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">📈 and 📉</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Benefits</h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• Common approach, well-documented & time-tested.</h3>
   <h3>• Capable of handling complex scenarios.</h3>
   <h3>• Provides clarity & stability to a data warehouse.</h3>
   <h3>• Fast to build, no normalization required.</h3>
   <h3>• Easy to comprehened, simplifies querying and analysis.</h3>
  </p>
 </div>
 <h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Disadvantages</h2>
 <div>
  <p style="color: #00b9ad; margin-top: 25px">
   <h3>• Data isn't entirely integrated before reporting: no single source of truth.</h3>
   <h3>• Redundant data can be added to tables.</h3>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Which One Do You Choose❓</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Time to value ⏰</h2>
<h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Kimball</h3>
 <div>
  <p style="color: #00b9ad; margin-top:2px">
   <h4>• Faster initial results due to focus on specific business needs.</h4>
   <br>
   <h4>• Delivers value iteratively.</h4>
  </p>
 </div>
 <h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Inmon</h3>
 <div>
  <p style="color: #00b9ad; margin-top: 2px">
   <h4>• Longer initial setup due to comprehensive EDW design.</h4>
   <br>
   <h4>• Value realized when EDW is established and data marts are derived.</h4>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Which One Do You Choose❓</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Complexity & Integration ⚙️</h2>
<h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Kimball</h3>
 <div>
  <p style="color: #00b9ad; margin-top:2px">
   <h4>• Initial setup is simpler.</h4>
   <br>
   <h4>• Complexity can arise when integrating multiple data marts.</h4>
  </p>
 </div>
 <h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Inmon</h3>
 <div>
  <p style="color: #00b9ad; margin-top: 2px">
   <h4>• Initial design is complex due to enterprise-wide considerations.</h4>
   <br>
   <h4>• Integration is inherent, as data marts are derived from a unified EDW.</h4>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Which One Do You Choose❓</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Flexibility vs. Consistency 💪</h2>
<h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Kimball</h3>
 <div>
  <p style="color: #00b9ad; margin-top:2px">
   <h4>• More flexible to departmental needs.</h4>
   <br>
   <h4>• Risk of inconsistencies across data marts.</h4>
  </p>
 </div>
 <h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Inmon</h3>
 <div>
  <p style="color: #00b9ad; margin-top: 2px">
   <h4>• Consistent data model across the organization.</h4>
   <br>
   <h4>• Less flexibility for department-specific nuances.</h4>
  </p>
 </div>


---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Which One Do You Choose❓</h1>
<h2 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Maintenance & Scalability 👩‍🔧</h2>
<h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Kimball</h3>
 <div>
  <p style="color: #00b9ad; margin-top:2px">
   <h4>• Maintenance can be challenging when integrating or changing multiple data marts.</h4>
   <br>
   <h4>• Scalable in terms of adding new data marts.</h4>
  </p>
 </div>
 <h3 style="color: #0c2749; margin-left: -15px; margin-top:30px; font-weight:400">Inmon</h3>
 <div>
  <p style="color: #00b9ad; margin-top: 2px">
   <h4>• Centralized maintenance at the EDW level.</h4>
   <br>
   <h4>• Scalability requires changes to the central EDW, but data marts can be easily derived.</h4>
  </p>
 </div>
 

---
class: bg-white

---

<h1 style="color: #0c2749; margin-left: -15px; font-weight:600">Hands On‼️</h1>