# GoProLRVTHM Cleaner

A simple utility script to delete `.THM` and `.LRV` files from GoPro camera folders to free up space. This script can be run directly in Python or as an executable to quickly clean up specified directories or the directory it resides in.

## Description

GoPro cameras create `.THM` and `.LRV` files for thumbnails and low-resolution previews of videos. While useful for some, these files can take up unnecessary space. `goprolrvthm.py` is a Python script that automates the deletion of these files from specified folders or the folder where the script (or its executable) is located.

## Installation

### Prerequisites

- Python 3.x installed on your machine.

### Steps

1. Clone the repository or download the `goprolrvthm.py` script directly.
   ```
   git clone https://github.com/konashevich/GoPro-LRV-THM-Cleaner.git
   ```
2. (Optional) Convert the script to an executable using PyInstaller for ease of use without Python:
   ```
   pip install pyinstaller
   pyinstaller --onefile goprolrvthm.py
   ```

## Usage

### As a Python Script

Run the script in a terminal or command prompt:
```
python goprolrvthm.py [folder_path]
```
If `[folder_path]` is not provided, the script will operate in the directory it's located in.

### As an Executable

After converting to an executable:
```
./goprolrvthm.exe [folder_path]
```
Download exe file from dist folder, make use of the bat example as well. 

### With a Batch File

Create a `.bat` file to run the executable with a predefined path:
```
path\to\goprolrvthm.exe "F:\DCIM\100GOPRO"
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

0. Hit STAR to this project
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the APACHE 2.0 License. See `LICENSE` for more information.