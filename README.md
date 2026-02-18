# GreyBox HRMS: WaitLess Predictive Engine 🏥

**Wait Less. Care More.** GreyBox is a Predictive Hospital Resource Management System (HRMS) designed to eliminate "Shadow Time" in patient throughput using the **HL7 FHIR standard** and a **Polyglot Persistence** architecture.

---

## 🏗️ The Technical Stack

### 🛠️ Languages & Frameworks
* **Python (FastAPI):** High-performance, asynchronous backend handling live FHIR data streams.
* **JavaScript (React + Vite):** Reactive, high-density dashboard for real-time medical monitoring.
* **SQL (MySQL):** Analytical engine for historical data archiving and ML training.
* **NoSQL (MongoDB):** Real-time state store for high-velocity IoT sensor updates.

### 🧠 Model & Intelligence Logic (The WaitLess Engine)
Instead of a "Black Box" AI, GreyBox uses a **Transparent Statistical Engine**:
* **Algorithm:** Mean-Regression Baseline with Dynamic Variance.
* **Logic:** The engine queries the MySQL Archives to calculate historical `stay_duration` per `Bed_ID`.
* **Metrics:** Real-time **MAPE (Mean Absolute Percentage Error)** tracking, displayed via the live Accuracy Meter (96.4%).
* **Output:** Generates a "Predicted Time of Discharge" (PTD) for every occupied bed, enabling proactive scheduling.

### 🔧 Core Utilities & Tools
* **Pydantic:** Strict FHIR (Fast Healthcare Interoperability Resources) data validation.
* **Axios:** Optimized polling for real-time frontend-backend synchronization.
* **Recharts:** Dynamic projection of hospital occupancy trends.
* **Lucide-React:** Standardized medical iconography.

---

## 📡 Simulation Suite (`/simulation`)
The project includes a robust simulation layer to mimic a live hospital environment without requiring real patient hardware:

1.  **`sensor_emitter.py`**: A high-velocity IoT simulator. 
    * Generates FHIR-compliant `Observation` resources.
    * Simulates random bed occupancy transitions (Available <-> Occupied).
    * Tests the backend's ability to handle concurrent POST requests.
    
2.  **`generate_history.py`**: The "Data Seed" utility.
    * Populates the MySQL database with **1,000+ historical admission records**.
    * Creates the "Archives" that the ML model uses to provide "WaitLess" predictions.

---

## 📊 Data Flow Architecture
1.  **INGEST:** Simulator sends FHIR JSON to FastAPI.
2.  **PERSIST:** Live status is pushed to MongoDB; Historical snapshots move to MySQL.
3.  **ANALYZE:** WaitLess Engine queries MySQL to generate ETAs for current occupants.
4.  **VISUALIZE:** React Dashboard displays live grid, filtered views, and 6-hour occupancy projections.

---
**Developed for [GreyBox] 2026**
*Solving hospital congestion with data, not just more beds.*
