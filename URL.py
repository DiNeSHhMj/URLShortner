import requests
import json
import tkinter as tk
from tkinter import messagebox

ACCESS_TOKEN = "ACCESS_TOKEN"

def shorten_url(long_url):
    """Shorten the long_url using the Bitly API"""
    api_url = f"https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": long_url
    }
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    response_data = json.loads(response.text)
    return response_data.get("link")

def shorten_link():
    """Callback function for the 'Shorten' button"""
    long_url = input_entry.get()
    try:
        short_url = shorten_url(long_url)
        output_label.config(text=short_url)
        copy_button.config(state="normal")
    except requests.exceptions.HTTPError as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")
        output_label.config(text="")
        copy_button.config(state="disabled")

def copy_to_clipboard():
    """Callback function for the 'Copy' button"""
    root.clipboard_clear()
    root.clipboard_append(output_label.cget("text"))
    messagebox.showinfo("Success", "URL copied to clipboard!")

# Create the tkinter GUI
root = tk.Tk()
root.title("URL Shortener")
input_label = tk.Label(root, text="Enter URL:")
input_label.pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()
shorten_button = tk.Button(root, text="Shorten", command=shorten_link)
shorten_button.pack()
output_label = tk.Label(root, text="")
output_label.pack()
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, state="disabled")
copy_button.pack()
root.mainloop()
