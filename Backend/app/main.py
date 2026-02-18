from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from app.api.v1 import beds  # We will create this next
from app.db.mysql_client import get_mysql_connection

app = FastAPI(title=" Hospital Resource Management")

# LOGIC: Test MySQL on Startup
@app.on_event("startup")
def startup_db_client():
    conn = get_mysql_connection()
    if conn and conn.is_connected():
        print("✅ SUCCESS: Backend is now linked to MySQL .")
        conn.close()
    else:
        print("🚨 CRITICAL: Backend failed to connect to MySQL. Check credentials!")

# LOGIC: Allow React (usually on port 3000 or 5173) to talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you'd specify the exact URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include our bed tracking routes
app.include_router(beds.router, prefix="/api/v1", tags=["Beds"])

@app.get("/")
async def health_check():
    return {"status": "online", "system": "HRMS WaitLess Engine"}