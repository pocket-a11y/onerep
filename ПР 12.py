import tkinter as tk
import requests
import json
import os

def fetch_and_save_data():
    """Fetches GitHub user data and saves it to a JSON file."""
    try:
        username = username_entry.get()
        filename = filename_entry.get()
        if not filename:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Please enter a filename.\n")
            return

        url = f"https://api.github.com/users/{username}"
        user_data = requests.get(url).json()

        info = {
            'company': user_data.get("company", "N/A"),
            'created_at': user_data.get("created_at", "N/A"),
            'email': user_data.get("email", "N/A"),
            'id': user_data.get("id", "N/A"),
            'name': user_data.get("name", "N/A"),
            'url': user_data.get("url", "N/A")
        }

        #Check if the file exists, add a number if it does
        base, ext = os.path.splitext(filename)
        i = 1
        while os.path.exists(filename):
            filename = f"{base}_{i}{ext}"
            i += 1

        with open(filename, 'w') as f:
            json.dump(info, f, indent=4)  # Use indent for pretty printing

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Data saved to {filename}\n")

    except requests.exceptions.RequestException as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error fetching data: {e}\n")
    except json.JSONDecodeError as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error decoding JSON: {e}\n")


# Create main window
root = tk.Tk()
root.title("GitHub User Info")

# Username entry
username_label = tk.Label(root, text="Enter GitHub Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Filename entry
filename_label = tk.Label(root, text="Enter Filename (e.g., user_data.json):")
filename_label.pack(pady=5)
filename_entry = tk.Entry(root)
filename_entry.pack(pady=5)

# Fetch and save button
button = tk.Button(root, text="Fetch and Save Data", command=fetch_and_save_data)
button.pack(pady=10)

# Output text area
output_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
output_text.pack(pady=10)

root.mainloop()