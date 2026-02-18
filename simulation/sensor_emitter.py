import requests
import time
import random

BASE_URL = "http://127.0.0.1:8000/api/v1"
TOTAL_BEDS = 50

def simulate_bed_updates():
    print(f"🚀 Starting GreyBox Digital Twin: Simulating {TOTAL_BEDS} beds...")
    
    while True:
        # Pick a random bed to change status
        bed_id = f"BED-{random.randint(1, TOTAL_BEDS):02d}"
        new_status = random.choice(["Occupied", "Available"])
        
        # Construct FHIR-compliant payload
        payload = {
            "resourceType": "Observation",
            "id": bed_id,
            "status": "final",
            "code": {"text": "Bed Occupancy Status"},
            "valueString": new_status
        }
        
        try:
            start_time = time.time()
            response = requests.post(f"{BASE_URL}/update-status", json=payload)
            latency = (time.time() - start_time) * 1000 # convert to ms
            
            if response.status_code == 200:
                print(f"✅ {bed_id} -> {new_status} | Latency: {latency:.2f}ms")
            else:
                print(f"❌ Failed to update {bed_id}")
                
        except Exception as e:
            print(f"⚠️ Connection Error: {e}")
            break
            
        # Wait a bit before next update to simulate real-world movement
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    simulate_bed_updates()