# ZKTeco Data Exporter

## 🚀 Overview

This Python-based solution provides a direct and efficient way to extract attendance and time-tracking data from ZKTeco-compatible devices. It's designed to bypass common limitations encountered with vendor-provided software, especially when dealing with large volumes of records, and offers flexible output formats for further analysis and system integration.

## ✨ Features

* **Direct Device Communication:** Connects directly to ZKTeco devices via network (port 4370) using the `pyzk` library.
* **Flexible Data Extraction:**
    * **All Records:** Extracts all available attendance records from the device.
    * **Monthly Export:** Allows users to specify a particular year and month to export records, making data management easier for periodic reports.
* **Multiple Output Formats:**
    * Generates a clean and readable **Excel (.xlsx)** file for human-friendly reports and analysis.
    * Produces a **custom-formatted text (.txt)** file, tailored for seamless integration with other internal systems (e.g., accounting or HR software).
* **Secure Configuration:** Separates sensitive device connection details into an external `config.ini` file, ensuring no sensitive information is committed to version control.

## 📦 Project Structure
ZKTeco-Data-Exporter/
│
├── .gitignore               # Specifies intentionally untracked files to ignore
├── config.ini.example       # Example configuration file (rename to config.ini)
├── exportwithYearandMonth.py # Script to export data for a specific month
├── ExportAll.py             # Script to export all attendance records
├── run.bat                  # Batch script for Windows to run the main menu
├── run.sh                   # Shell script for Linux/macOS to run the main menu
└── requirements.txt         # Lists Python dependencies
└── README.md                # This file


**Note:** The actual `config.ini` file (containing your device's IP) should **not** be committed to Git, as specified in `.gitignore`. A `config.ini.example` is provided for guidance.

## 🚀 Getting Started

Follow these steps to set up and run the exporter:

### 1. Prerequisites

* Python 3.x installed.
* Access to your ZKTeco device's IP address and network port (default is 4370).

### 2. Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/ZKTeco-Data-Exporter.git](https://github.com/YourUsername/ZKTeco-Data-Exporter.git)
    cd ZKTeco-Data-Exporter
    ```
2.  **Create and Activate Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On Linux/macOS:
    source .venv/bin/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Device Details:**
    * Rename `config.ini.example` to `config.ini`.
    * Open `config.ini` and update the `IP_ADDRESS` and `PORT` to match your ZKTeco device.
    ```ini
    [ZKTeco]
    IP_ADDRESS = your_device_ip_here
    PORT = 4370
    TIMEOUT = 5
    ```

### 3. Running the Exporter

#### On Windows:

Simply run the `run.bat` file:
```bash
run.bat

This will open a menu in the command prompt, allowing you to choose between exporting a specific month's data or all records.

On Linux/macOS:
Grant execute permissions to the script:

Bash

chmod +x run.sh
Run the script:

Bash

./run.sh
This will open a menu in your terminal, providing the same options as the Windows script.

🤝 Contribution
Feel free to fork this repository, submit pull requests, or open issues if you encounter any problems or have suggestions for improvements.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
