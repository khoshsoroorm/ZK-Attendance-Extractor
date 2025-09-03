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
