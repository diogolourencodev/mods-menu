# Dark Souls Remastered Cheat Menu

A Python-based GUI application that provides memory editing capabilities for Dark Souls Remastered on Windows.

## Features

- **Infinite Estus Flask**: Toggle infinite usage of Estus Flasks
- **Max Souls**: Set your soul count to maximum (999,999,999)
- **User-friendly Interface**: Clean, dark-themed GUI built with CustomTkinter
- **Memory Safety**: Threaded operations to prevent UI freezing

## Requirements

- Windows OS
- Dark Souls Remastered running
- Python 3.7+
- Required Python packages:
  - pymem
  - customtkinter

## Installation

1. Install Python dependencies:
```
pip install pymem customtkinter
```

2. Download the script and run it:
```
python dsr-menu.py
```

## Important Note: Finding Soul Address

**You must find your current souls address using Cheat Engine before using the Max Souls feature:**

1. Open Cheat Engine
2. Attach to the DarkSoulsRemastered.exe process
3. Search for your current soul value (exact value)
4. Perform actions in-game to change your soul count
5. Refine your search in Cheat Engine with the new value
6. Once found, note the memory address and enter it in the cheat menu

## Usage

1. Launch Dark Souls Remastered
2. Run the cheat menu application
3. If connected successfully, the status will show "Connected ✓"
4. Use the toggle button to enable/disable infinite Estus
5. For souls:
   - Find your souls address using Cheat Engine (as described above)
   - Enter the address in hex format (ex: 118936A4)
   - Click "Set Max Souls" to set your souls to 999,999,999

## Disclaimer

This software is for educational purposes only. Use at your own risk. Online use may violate game terms of service and could result in account penalties.

## Troubleshooting

- Ensure Dark Souls Remastered is running before launching the cheat menu
- Run the application as administrator if experiencing connection issues
- Make sure to use the correct memory address for souls from Cheat Engine

## License

This project is provided for educational purposes only.
