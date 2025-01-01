# Unzippy

Unzippy is a simple Python application with a graphical user interface (GUI) built using Tkinter. It allows users to quickly and easily extract the contents of ZIP files to a specified destination folder.

## Features

- Browse and select a source ZIP file.
- Choose a destination folder for extracted files.
- Lightweight and easy to use.

## Requirements

To run Unzippy, you need to have the following installed:

- Python 3.7 or later
- The following Python libraries:
  - `tkinter` (usually included with Python)
  - `zipfile`

## Installation

1. Clone the repository or download the project files:

   ```bash
   git clone https://github.com/your-username/unzippy.git
   cd unzippy
   ```

2. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Run the `run.py` script:

   ```bash
   python run.py
   ```

2. A graphical interface will appear with the following options:

   - **Source File**: Browse and select the ZIP file you want to extract.
   - **Destination Folder**: Browse and select the folder where you want the files to be extracted.
   - **Unzip Button**: Click to extract the contents of the ZIP file.

3. Once the extraction is complete, a confirmation message will appear, or in case of an error, an error message will appear.

## How It Works

Unzippy uses Python's built-in `zipfile` module to handle ZIP file extraction. The Tkinter library provides the user-friendly graphical interface for selecting files and folders.

## Project Structure

```plaintext
unzippy/
├──.gitignore
├── main.py        # Contains the script for building the GUI
├── README.md      # Project documentation
├── run.bat
├── run.py         # Run this script
└── unzip.py       # Containts the script for unzipping files
```

## Contributing

Contributions are welcome! If you'd like to improve Unzippy, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python and Tkinter.
- Inspired by the need for a simple ZIP extraction tool.
