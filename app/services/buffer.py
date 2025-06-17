def get_buffer_status():
    return {
        "currentLogs": 12,
        "maxCapacity": 5000,
        "unsyncedLogs": 3
    }

def flush_buffer():
    return {"message": "Buffer flush făcut!"}
