def detect_volume_ddos(traffic_log):
    threshold = 100
    print("📊 Monitoring incoming request volume...\n")

    for time_slot, request_count in traffic_log.items():
        print(f"{time_slot}: {request_count} requests")
        if request_count > threshold:
            print("🚨 ALERT: Potential DDoS detected in this time slot!")



# Simulated traffic data
traffic = {
    "12:00": 80,
    "12:01": 110,
    "12:02": 95,
    "12:03": 130
}



detect_volume_ddos(traffic)