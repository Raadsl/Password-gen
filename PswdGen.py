import random
import string
import tkinter as tk

def generate_password(length, num_special_chars):
  password = ""
  # Generate a random password of the given length
  for i in range(length):
    # Randomly choose a lowercase letter, uppercase letter, or digit
    password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
  # Add the required number of special characters to the password
  for i in range(num_special_chars):
    password += random.choice(string.punctuation)
  return password

# Create the main window
window = tk.Tk()
window.title("Password Generator")

window.iconbitmap('lock.ico')


# Create the length label and entry
length_label = tk.Label(text="Length of password:")
length_entry = tk.Entry()
length_label.pack()
length_entry.pack()

# Create the number of special characters label and entry
special_chars_label = tk.Label(text="Number of special characters:")
special_chars_entry = tk.Entry()
special_chars_label.pack()
special_chars_entry.pack()

# Create the generate button and password label
def generate_button_clicked():
  try:
    length = int(length_entry.get())
  except:
    length = 16
  try:
    num_special_chars = int(special_chars_entry.get())
  except:
    num_special_chars = 6

  password = generate_password(length, num_special_chars)
  password_label.config(text=password)

generate_button = tk.Button(text="Generate", command=generate_button_clicked)
generate_button.pack()
password_label = tk.Label(text="")
password_label.pack()

# Create the copy button
def copy_button_clicked():
  window.clipboard_clear()
  window.clipboard_append(password_label.cget("text"))

copy_button = tk.Button(text="Copy", command=copy_button_clicked)
copy_button.pack()

# Run the main loop
window.mainloop()
