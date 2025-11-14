# 🚀 Real-Time Azure ELT Framework

A complete end-to-end **real-time data engineering pipeline** built using **Azure Event Hub, ADLS Gen2, Azure Data Factory, Azure SQL Database, and Azure Databricks** following the **Bronze → Silver → Gold Medallion Architecture**.

This project demonstrates how to ingest streaming order data in real-time, land it in a data lake, clean & process it, and finally serve it for analytics.

---

## 📌 **Project Overview**

This project simulates a **real-time order data pipeline** with the following stages:

---

## 🟤 **1. Real-Time Ingestion (Bronze Layer)**

### **Technologies:**

* Python Event Producer
* Azure Event Hub
* Azure Data Lake Storage Gen2
* Azure Data Factory (Copy Activity)

### **What happens here:**

✔ A Python script continuously generates order events:

```json
{
  "order_id": 1234,
  "amount": 450,
  "timestamp": 1763120674.343
}
```

✔ The events are sent to **Azure Event Hub**.
✔ ADF **Event Hub -> ADLS** pipeline stores raw JSON files in Bronze.
✔ Data is NOT modified — only captured as-is.

📍 **Purpose:** Store raw, immutable events for traceability.

---

## ⚪ **2. Transformation & Deduplication (Silver Layer)**

### **Technologies:**

* Azure Data Factory (Data Flow)

### **Processing done:**

✔ Data cleaning:

* Cast columns to correct datatypes
* Rename `timestamp` → `event_time`
* Convert Unix timestamp to datetime
* Remove invalid or null rows

✔ **Deduplication** using:

* order_id
* event_time

✔ **Incremental load logic**:

* Filter only new data from Bronze
* Maintain watermarking using ADF

📍 **Purpose:** Create a clean, validated, deduplicated dataset ready for business logic.

---

## 🟡 **3. Business Aggregations (Gold Layer)**

### **Technologies:**

* Azure Data Factory
* Azure SQL Database

### **Gold transformations include:**

✔ Daily order summary
✔ Total revenue summary
✔ Number of orders per hour
✔ Top customers (if available)

✔ Gold tables example:

**gold_daily_orders**

| date | total_orders | total_amount |
| ---- | ------------ | ------------ |

**gold_hourly_revenue**
| hour | revenue |

📍 **Purpose:** Highly optimized analytical tables for Power BI & reporting.

---

## 🧱 **Architecture Diagram**

**(Describe or upload diagram manually)**
Bronze → Silver → Gold Medallion Architecture using Azure services.

---

## 🧪 **Tech Stack**

| Layer           | Technology                        |
| --------------- | --------------------------------- |
| Ingestion       | Azure Event Hub + Python Producer |
| Landing         | ADLS Gen2                         |
| Orchestration   | Azure Data Factory                |
| Cleaning        | ADF Data Flow                     |
| Storage         | ADLS / Azure SQL DB               |
| Version Control | GitHub                            |

---

## 📁 **Project Structure**

```
real-time-azure-elt-framework/
│
├── python_producer/
│   └── producer.py
│
├── python_consumer/
│   └── consumer.py
│
├── adf/
│   ├── pipelines/
│   ├── datasets/
│   └── dataflows/
│
└── README.md
```

---

## 🎯 **Key Features**

* Fully automated end-to-end real-time pipeline
* Event Hub parallel consumers
* Error handling & retries
* Azure Data Factory ELT orchestration
* Deduplication and incremental loading
* Business-ready Gold tables
* Production-ready architecture

---

## 🚀 **How to Run This Project**

### **1️⃣ Run the Python event producer**

```
python producer.py
```

### **2️⃣ ADF picks messages from Event Hub**

Stores raw JSON → ADLS Bronze.

### **3️⃣ Run the Silver Data Flow**

This cleans + dedupes → ADLS Silver.

### **4️⃣ Run Gold Pipeline**

Loads aggregated results → Azure SQL DB.

---

## 📌 **Use Cases**

* Real-time eCommerce analytics
* Order monitoring and fraud detection
* IoT sensor streaming
* Live dashboards for operations

---

## ⭐ **Author**

**Farhan**
Data Engineer | Cloud & Azure Specialist

