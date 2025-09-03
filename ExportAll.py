# ExportAll.py

from zk import ZK
from datetime import datetime
import pandas as pd
import jdatetime
import configparser

# Read configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

try:
    device_ip = config.get('ZKTeco', 'IP_ADDRESS')
    device_port = config.getint('ZKTeco', 'PORT')
    device_timeout = config.getint('ZKTeco', 'TIMEOUT')
except (configparser.NoSectionError, configparser.NoOptionError):
    print("❌ Error: config.ini file not found or is missing required values.")
    print("Please make sure 'config.ini' exists and contains [ZKTeco] section with IP_ADDRESS, PORT, and TIMEOUT.")
    input("⏳ Press Enter to exit...")
    exit()

zk = ZK(device_ip, port=device_port, timeout=device_timeout)

try:
    conn = zk.connect()
    conn.disable_device()
    print("✅ Connected to device.")

    records = conn.get_attendance()
    print(f"📥 Total records found: {len(records)}")

    filtered = []
    text_lines = []

    for r in records:
        ts_shamsi = jdatetime.datetime.fromgregorian(datetime=r.timestamp)

        user_id = str(r.user_id)
        month = f"{ts_shamsi.month:02d}"
        day = f"{ts_shamsi.day:02d}"
        hour = f"{ts_shamsi.hour:02d}"
        minute = f"{ts_shamsi.minute:02d}"

        custom_text = f"1{user_id}{month}{day}{hour}{minute}1"
        text_lines.append(custom_text)

        filtered.append({
            'user_id': r.user_id,
            'timestamp_gregorian': r.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'timestamp_persian': ts_shamsi.strftime('%Y/%m/%d %H:%M:%S'),
            'status': r.status,
            'punch': r.punch
        })

    # Save Excel file
    df = pd.DataFrame(filtered)
    df.to_excel('attendance_all.xlsx', index=False)
    print("📁 Excel output saved: attendance_all.xlsx")

    # Save text file
    with open('attendance_all.txt', 'w', encoding='utf-8') as f:
        for line in text_lines:
            f.write(line + '\n')
    print("📄 Text file saved: attendance_all.txt")

    conn.enable_device()
    conn.disconnect()

except Exception as e:
    print(f"❌ Error: {e}")

input("⏳ Press Enter to exit...")
