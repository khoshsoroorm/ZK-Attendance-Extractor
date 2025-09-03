#!/bin/bash

# Define paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
PYTHON_EXE="$VENV_DIR/bin/python"

# Check if venv exists
if [ ! -f "$PYTHON_EXE" ]; then
    echo "❌ Virtual environment not found in .venv/"
    echo "Please run 'python3 -m venv .venv' and 'source .venv/bin/activate && pip install -r requirements.txt' first."
    read -p "Press Enter to exit..."
    exit 1
fi
echo "✅ Virtual environment found."

# Function to display menu
show_menu() {
    clear
    echo "====================================="
    echo "      💻 Attendance Export System      "
    echo "====================================="
    echo
    echo "1. Export data for a specific month"
    echo "2. Export all records"
    echo "0. Exit the program"
    echo
}

# Main loop
while true; do
    show_menu
    read -p "Please enter your choice: " choice

    case $choice in
        1)
            echo "✅ Running exportwithYearandMonth.py ..."
            "$PYTHON_EXE" "$SCRIPT_DIR/exportwithYearandMonth.py"
            read -p "Press Enter to return to the menu..."
            ;;
        2)
            echo "✅ Running ExportAll.py ..."
            "$PYTHON_EXE" "$SCRIPT_DIR/ExportAll.py"
            read -p "Press Enter to return to the menu..."
            ;;
        0)
            echo "👋 Goodbye!"
            break
            ;;
        *)
            echo "❌ Invalid option! Please try again."
            read -p "Press Enter to continue..."
            ;;
    esac
done
