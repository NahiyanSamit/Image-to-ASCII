import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import os


# Function to convert image to ASCII
def convert_image_to_ascii(image_path, output_path, width, height):
    # Open image
    image = Image.open(image_path)

    # Resize image
    image = image.resize((width, height))

    # Convert image to grayscale
    image = image.convert('L')

    # Define ASCII characters
    ascii_chars = '@%#*+=-:. '

    # Convert image to ASCII
    ascii_image = ''
    for i in range(height):
        for j in range(width):
            pixel_value = image.getpixel((j, i))
            ascii_image += ascii_chars[pixel_value // 32]
        ascii_image += '\n'

    # Write ASCII image to file with .txt extension
    with open(output_path, 'w') as f:
        f.write(ascii_image)

    # Open file
    os.system(output_path)


# Function to handle button click
def handle_click():
    # Get image path
    image_path = filedialog.askopenfilename()

    try:
        # Get width
        width = int(width_entry.get())

        # Get height
        height = int(height_entry.get())

    except ValueError:
        # Display error message
        error_message = tk.Toplevel(window)
        error_message.title('Error')
        error_message.geometry('250x100')
        error_message.resizable(False, False)
        error_label = ttk.Label(error_message, text='Please enter valid width and height first!')
        error_label.pack()
        button_error = ttk.Button(error_message, text='OK', command=error_message.destroy)
        button_error.pack()
        return

    # Get output path
    output_path = filedialog.asksaveasfilename(title="Save File As",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    # add .txt extension
    output_path += '.txt'

    # Convert image to ASCII
    convert_image_to_ascii(image_path, output_path, width, height)


# Create main window
window = tk.Tk()
window.title('Image to ASCII')
window.resizable(False, False)

# Create image button
image_button = ttk.Button(window, text='Select Image', command=handle_click)
image_button.grid(row=0, column=0, padx=5, pady=5)

# Create width label
width_label = ttk.Label(window, text='Width:')
width_label.grid(row=1, column=0, padx=5, pady=5)

# Create width entry
width_entry = ttk.Entry(window)
width_entry.grid(row=1, column=1, padx=5, pady=5)

# Create height label
height_label = ttk.Label(window, text='Height:')
height_label.grid(row=2, column=0, padx=5, pady=5)

# Create height entry
height_entry = ttk.Entry(window)
height_entry.grid(row=2, column=1, padx=5, pady=5)

# Run main loop
window.mainloop()
