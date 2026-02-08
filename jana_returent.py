import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Requires `pillow` package

menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80
}

order_total = 0
selected_items = []
image_refs = {}  # To prevent images from being garbage-collected

def add_item(item):
    global order_total
    order_total += menu[item]
    selected_items.append(item)
    messagebox.showinfo("Item Added", f"{item.capitalize()} added to your order!")

def show_total():
    order_summary = "\n".join(f"- {item.capitalize()} : Rs{menu[item]}" for item in selected_items)
    messagebox.showinfo("Order Summary", f"Your Order:\n{order_summary}\n\nTotal: Rs{order_total}")

def clear_order():
    global order_total, selected_items
    order_total = 0
    selected_items = []
    messagebox.showinfo("Order Cleared", "Your order has been cleared.")

# GUI Setup
root = tk.Tk()
root.title("Jana Restaurant")
root.geometry("400x600")

tk.Label(root, text="Welcome to Jana Restaurant", font=("Helvetica", 16, "bold")).pack(pady=10)
tk.Label(root, text="Select items to order:", font=("Helvetica", 12)).pack(pady=5)

# Add food items with images
for item, price in menu.items():
    frame = tk.Frame(root)
    frame.pack(pady=5)

    # Load and resize image
    try:
        img = Image.open(f"{item}.png")
        img = img.resize((50, 50), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        image_refs[item] = img_tk  # Keep a reference
        tk.Label(frame, image=img_tk).pack(side="left", padx=5)
    except Exception as e:
        tk.Label(frame, text="No Image").pack(side="left", padx=5)

    tk.Button(frame, text=f"{item.capitalize()} - Rs{price}", width=20, command=lambda i=item: add_item(i)).pack(side="left")

# Buttons
tk.Button(root, text="Show Total", bg="green", fg="white", command=show_total).pack(pady=15)
tk.Button(root, text="Clear Order", bg="red", fg="white", command=clear_order).pack(pady=5)

root.mainloop()
