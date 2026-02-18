🏥 GreyBox HRMS: WaitLess Predictive Engine
Feature-Complete Prototype | Hackathon 2026

GreyBox is a high-performance Hospital Resource Management System designed to eliminate "Shadow Time" in patient throughput. By using a hybrid-database architecture and the HL7 FHIR standard, GreyBox predicts bed vacancy before it happens.
🏗️ The Technical Manifest
🛠️ Languages & Core Frameworks

    Python (FastAPI): High-performance, asynchronous backend handling live FHIR data streams.

    JavaScript (React + Vite): Reactive, high-density dashboard for real-time medical monitoring.

    SQL (MySQL): Analytical engine for historical data archiving and ML training.

    NoSQL (MongoDB): Real-time state store for high-velocity IoT sensor updates.

🧠 The WaitLess Intelligence (ML Logic)

Instead of a "Black Box" AI, GreyBox uses a Transparent Statistical Engine:

    Algorithm: Mean-Regression Baseline with Dynamic Variance.

    Logic: The engine queries MySQL Archives to calculate historical stay_duration per Bed_ID.

    Metrics: Real-time MAPE (Mean Absolute Percentage Error) tracking, displayed via a live Accuracy Meter (96.4%).

    Output: Generates a "Predicted Time of Discharge" (PTD) for every occupied bed, enabling proactive scheduling.

📁 Project Architecture & Features
1. 🖥️ /frontend (The Command Center)

A "Medical Console" style UI focused on actionable data.

    Real-time Bed Grid: Visualizes 50+ beds with dynamic color-coding (Green = Vacant, Red = Occupied).

    Multi-View Filtering: Integrated logic to isolate "Available" or "Occupied" beds instantly.

    Modular Trend Chart: A 6-hour occupancy projection built with Recharts. Features a "Plug & Run" Toggle to enable/disable the chart from both the UI and the code.

    Tech: React, Lucide-Icons, Axios, Recharts.

⚙️ 2. /backend (The Intelligence Layer)

The traffic controller for medical data validation and prediction.

    FHIR Standardization: Every update is validated as an HL7 FHIR Observation resource via Pydantic models.

    Polyglot Persistence: * MongoDB: Stores the "Now" (Live Status) for sub-50ms dashboard responsiveness.

        MySQL: Stores the "Then" (Historical Archives) for analytical processing.

    Tech: FastAPI, Pydantic, Motor, MySQL-Connector.

📡 3. /simulation (The Digital Twin)

A robust suite to mimic a live hospital environment:

    sensor_emitter.py: Simulates IoT bed sensors sending FHIR-compliant signals to the backend.

    generate_history.py: Seeds the MySQL database with 1,000+ historical admission records to provide the ML model with immediate "learned" data.

🏁 Feature-Complete Status

    [x] Full-Stack Sync: Real-time communication between FastAPI and React via Axios.

    [x] Hybrid DB Logic: Seamless data flow between NoSQL (Live) and SQL (Analytical).

    [x] WaitLess Engine: Functional "Predicted Wait Time" displayed on all occupied beds.

    [x] Interactive UI: Filtering, accuracy tracking, and feature-toggled charts.

    [x] Medical Interoperability: Strict adherence to FHIR data structures.

💡 Information for the Team

    Setup: Ensure mongodb and mysql services are running before starting the backend.

    Data Seeding: Run simulation/generate_history.py once to ensure the "WaitLess" engine has historical data to query.

    Live Demo: Keep the sensor_emitter.py running during the presentation to demonstrate the real-time grid updates and accuracy meter fluctuations.

"Turning hospital data into hospital foresight."
