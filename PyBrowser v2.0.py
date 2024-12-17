import tkinter as tk
import webbrowser

def open_url():
    url = url_entry.get()
    if url:
        loading_label.config(text="Loading...")
        root.update()  # Refresh the UI to show the loading message
        webbrowser.open(url)
        loading_label.config(text="")

def open_credits():
    credits_window = tk.Toplevel(root)
    credits_window.title("Credits")
    credits_window.geometry("400x300")
    credits_window.config(bg=bg_color)  # Set background color for the credits window

    # Create a frame to hold the credits content
    credits_frame = tk.Frame(credits_window, bg=bg_color)
    credits_frame.pack(fill=tk.BOTH, expand=True, pady=20, padx=20)

    # Bold "Credits:" part
    bold_label = tk.Label(credits_frame, text="Credits:", font=(default_font_name, 12, "bold"), fg="black", bg=bg_color, justify=tk.LEFT)
    bold_label.pack(anchor="w")

    # Normal font for the rest
    credits_label = tk.Label(credits_frame, text="\nThatPythonGuy-95 (AKA ThatTechGuy) - Creator\n\nSwitzerlandr - Logo Design\n\nMicrosoft Copilot - Resources", font=default_font, fg="black", bg=bg_color, justify=tk.LEFT)
    credits_label.pack(anchor="w")

# Define theme colors and fonts
bg_color = "#8FBC8F"  # Dark Sea Green
fg_color = "#2E8B57"  # Sea Green
default_color = fg_color
default_font_name = "Helvetica"
default_font = (default_font_name, 12)
title_font = (default_font_name, 24, "bold")
slogan_font = (default_font_name, 14, "italic")
entry_font = (default_font_name, 12)
button_font = (default_font_name, 12, "bold")

# Main application window
root = tk.Tk()
root.title("PyBrowser")
root.geometry("600x400")
root.config(bg=bg_color)

# Make the window start maximized
root.state('zoomed')

# Browser name in the top left
browser_name = tk.Label(root, text="PyBrowser", font=title_font, fg=default_color, bg=bg_color)
browser_name.place(x=10, y=10)

# Credits button in the top right with margin
credits_button = tk.Button(root, text="Credits", command=open_credits, font=button_font, fg=bg_color, bg=default_color)
credits_button.place(relx=0.98, rely=0.03, anchor="ne")  # Adjusted y position to add vertical margin

# Separator line
separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN, bg="black")
separator.pack(fill=tk.X, pady=(80, 50))  # Increased top padding to ensure separation

# Centering Frame
center_frame = tk.Frame(root, bg=bg_color)
center_frame.pack(expand=True)

# URL entry field (centered)
url_entry = tk.Entry(center_frame, width=50, font=entry_font, fg="black", bg="white", insertbackground=default_color)
url_entry.insert(0, "Insert URL Here")
url_entry.pack(pady=10)

# Go button (below the URL entry field)
go_button = tk.Button(center_frame, text="Go", command=open_url, font=button_font, fg=bg_color, bg=default_color)
go_button.pack(pady=5)

# Loading label (below the Go button)
loading_label = tk.Label(center_frame, text="", font=entry_font, fg=default_color, bg=bg_color)
loading_label.pack(pady=5)

# Footer (bottom center)
footer = tk.Label(root, text="This is ThatTechGuy LLC open-source software.", font=default_font, fg=default_color, bg=bg_color)
footer.pack(side=tk.BOTTOM, pady=10)

# Run the application
root.mainloop()
