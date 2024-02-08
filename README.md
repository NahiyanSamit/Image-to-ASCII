# IMG to ASCII

Convert an image to ASCII art using Python.

## Description

IMG_to_ASCII is a Python script that allows you to convert an image into ASCII art. It uses the brightness of each pixel to determine the corresponding ASCII character and creates a new image made entirely of ASCII characters.

## Features

- Convert any image to ASCII art
- User defined height and width 
- Save the ASCII art as a text file

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/IMG_to_ASCII.git
   ```

2. Install Requirements

    ```bash
        pip install -r requirements.txt
    ```
3. Run the py file or Make extension

    ```bash
    python main.py
    ```
    or
    ```bash
    pyinstaller main.py --onefile --windowed
    ```
## User guide
1. First give height and width 
2. Then select an image from file chooser
3. lastly save the generated text file to your desired directory

## License
[The MIT License](LICENSE)
