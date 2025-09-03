# exportwithYearandMonth.py

from zk import ZK
from datetime import datetime
import pandas as pd
import jdatetime
import configparser

print("✅ Script started.")

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


# Get input from user
while True:
    try:
        target_year = int(input("Enter Persian year (e.g., 1403): "))
        target_month = int(input("Enter Persian month (1 to 12): "))
        break
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

zk = ZK(device_ip, port=device_port, timeout=device_timeout)

try:
    conn = zk.connect()
    conn.disable_device()
    print("✅ Connected to device.")

    records = conn.get_attendance()
    print(f"📥 Total records received: {len(records)}")

    filtered = []
    text_lines = []

    for r in records:
        ts_shamsi = jdatetime.datetime.fromgregorian(datetime=r.timestamp)

        if ts_shamsi.year == target_year and ts_shamsi.month == target_month:
            user_id = str(r.user_id)
            month = f"{ts_shamsi.month:02d}"
            day = f"{ts_shamsi.day:02d}"
            hour = f"{ts_shamsi.hour:02d}"
            minute = f"{ts_shamsi.minute:02d}"

            custom_text = f"1{user_id}{month}{day}{hour}{minute}1"
            text_lines.append(custom_text)

            filtered.append({
                'user_id': r.user_id,
                'timestamp_miladi': r.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'timestamp_shamsi': ts_shamsi.strftime('%Y/%m/%d %H:%M:%S'),
                'status': r.status,
                'punch': r.punch
            })

    if not filtered:
        print("⚠️ No records found for this month and year.")
    else:
        excel_name = f"attendance_{target_year}_{target_month:02d}.xlsx"
        text_name = f"attendance_{target_year}_{target_month:02d}.txt"

        df = pd.DataFrame(filtered)
        df.to_excel(excel_name, index=False)
        print(f"📁 Excel saved: {excel_name}")

        with open(text_name, 'w', encoding='utf-8') as f:
            for line in text_lines:
                f.write(line + '\n')

        print(f"📄 Text file saved: {text_name}")

    conn.enable_device()
    conn.disconnect()

except Exception as e:
    print(f"❌ Error: {e}")

input("⏳ Press Enter to exit...")
