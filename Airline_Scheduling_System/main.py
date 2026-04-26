import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

flights = []
cargo = []

root = tk.Tk()
root.title("Airline Scheduling & Cargo Scheduling")
root.geometry("1400x850")
root.configure(bg="#edf2f7")

# =====================================================
# HEADER
# =====================================================
header = tk.Frame(root, bg="#0b2f6b", height=70)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="Airline Scheduling & Cargo Scheduling",
    bg="#0b2f6b",
    fg="white",
    font=("Arial", 20, "bold")
).pack(side="left", padx=30)

clock = tk.Label(
    header,
    bg="#0b2f6b",
    fg="white",
    font=("Arial", 11)
)
clock.pack(side="right", padx=30)

def update_clock():
    clock.config(text=datetime.now().strftime("%d %b %Y   %I:%M:%S %p"))
    root.after(1000, update_clock)

update_clock()

# =====================================================
# MAIN LAYOUT
# =====================================================
sidebar = tk.Frame(root, bg="white", width=240)
sidebar.pack(side="left", fill="y")

main = tk.Frame(root, bg="#edf2f7")
main.pack(side="right", fill="both", expand=True)

content = tk.Frame(main, bg="#edf2f7")
content.pack(fill="both", expand=True, padx=25, pady=25)

# =====================================================
# PAGES
# =====================================================
dashboard_page = tk.Frame(content, bg="#edf2f7")
flight_page = tk.Frame(content, bg="#edf2f7")
cargo_page = tk.Frame(content, bg="#edf2f7")
schedule_page = tk.Frame(content, bg="#edf2f7")
chatbot_page = tk.Frame(content, bg="#edf2f7")

for page in (dashboard_page, flight_page, cargo_page, schedule_page, chatbot_page):
    page.place(relx=0, rely=0, relwidth=1, relheight=1)

def show_page(page):
    page.tkraise()
    refresh_all()

# =====================================================
# SIDEBAR
# =====================================================
btn_style = {
    "bg": "#2563eb",
    "fg": "white",
    "font": ("Arial", 13, "bold"),
    "width": 18,
    "height": 1,
    "bd": 0,
    "cursor": "hand2"
}

tk.Label(sidebar, text="", bg="white").pack(pady=8)

tk.Button(sidebar, text="Dashboard", command=lambda: show_page(dashboard_page), **btn_style).pack(pady=4, padx=12)
tk.Button(sidebar, text="Flights", command=lambda: show_page(flight_page), **btn_style).pack(pady=4, padx=12)
tk.Button(sidebar, text="Cargo", command=lambda: show_page(cargo_page), **btn_style).pack(pady=4, padx=12)
tk.Button(sidebar, text="Schedule", command=lambda: show_page(schedule_page), **btn_style).pack(pady=4, padx=12)
tk.Button(sidebar, text="Chatbot", command=lambda: show_page(chatbot_page), **btn_style).pack(pady=4, padx=12)

# =====================================================
# DASHBOARD
# =====================================================
cards_frame = tk.Frame(dashboard_page, bg="#edf2f7")
cards_frame.pack(fill="x", pady=(0,20))

stats = []

for title in ["Flights","Cargo","Assigned","Profit"]:
    card = tk.Frame(cards_frame,
                    bg="white",
                    width=280,
                    height=110,
                    bd=1,
                    relief="solid")
    card.pack(side="left", padx=8, expand=True, fill="x")
    card.pack_propagate(False)

    tk.Label(card,
             text=title,
             bg="white",
             fg="#555",
             font=("Arial",12,"bold")).pack(pady=10)

    val = tk.Label(card,
                   text="0",
                   bg="white",
                   fg="black",
                   font=("Arial",24,"bold"))
    val.pack()

    stats.append(val)

# Middle Section
middle = tk.Frame(dashboard_page, bg="#edf2f7")
middle.pack(fill="both", expand=True)

# Recent Flights
box1 = tk.Frame(middle, bg="white", bd=1, relief="solid")
box1.pack(side="left", fill="both", expand=True, padx=(0,10))

tk.Label(box1, text="Recent Flights", bg="white",
         font=("Arial", 14, "bold")).pack(pady=10)

dash_flight = ttk.Treeview(box1, columns=("id","cap"), show="headings", height=10)
dash_flight.heading("id", text="Flight ID")
dash_flight.heading("cap", text="Capacity")
dash_flight.pack(fill="both", expand=True, padx=10, pady=10)

# Recent Cargo
box2 = tk.Frame(middle, bg="white", bd=1, relief="solid")
box2.pack(side="left", fill="both", expand=True, padx=(10,0))

tk.Label(box2, text="Recent Cargo", bg="white",
         font=("Arial", 14, "bold")).pack(pady=10)

dash_cargo = ttk.Treeview(box2, columns=("id","pf"), show="headings", height=10)
dash_cargo.heading("id", text="Cargo ID")
dash_cargo.heading("pf", text="Profit")
dash_cargo.pack(fill="both", expand=True, padx=10, pady=10)

# Bottom Status
status_box = tk.Frame(dashboard_page, bg="white", height=90, bd=1, relief="solid")
status_box.pack(fill="x", pady=20)
status_box.pack_propagate(False)

system_status = tk.Label(
    status_box,
    text="System Active | Waiting for Scheduling",
    bg="white",
    fg="#111",
    font=("Arial", 13, "bold")
)
system_status.pack(pady=30)

# =====================================================
# FLIGHT PAGE
# =====================================================
tk.Label(flight_page, text="Flight Management",
         bg="#edf2f7", font=("Arial", 20, "bold")).pack(pady=10)

flight_form = tk.Frame(flight_page, bg="white", bd=1, relief="solid")
flight_form.pack(fill="x", pady=10)

tk.Label(flight_form, text="Flight ID", bg="white").grid(row=0,column=0,padx=15,pady=15)
tk.Label(flight_form, text="Capacity", bg="white").grid(row=0,column=2,padx=15)

flight_id = tk.Entry(flight_form, width=18)
flight_cap = tk.Entry(flight_form, width=18)

flight_id.grid(row=0,column=1)
flight_cap.grid(row=0,column=3)

flight_table = ttk.Treeview(flight_page, columns=("id","cap","rem"), show="headings", height=18)
flight_table.heading("id", text="Flight ID")
flight_table.heading("cap", text="Capacity")
flight_table.heading("rem", text="Remaining")
flight_table.pack(fill="both", expand=True, pady=15)

# =====================================================
# CARGO PAGE
# =====================================================
tk.Label(cargo_page, text="Cargo Management",
         bg="#edf2f7", font=("Arial", 20, "bold")).pack(pady=10)

cargo_form = tk.Frame(cargo_page, bg="white", bd=1, relief="solid")
cargo_form.pack(fill="x", pady=10)

tk.Label(cargo_form, text="Cargo ID", bg="white").grid(row=0,column=0,padx=15,pady=15)
tk.Label(cargo_form, text="Weight", bg="white").grid(row=0,column=2,padx=15)
tk.Label(cargo_form, text="Profit", bg="white").grid(row=0,column=4,padx=15)

cargo_id = tk.Entry(cargo_form, width=18)
cargo_weight = tk.Entry(cargo_form, width=18)
cargo_profit = tk.Entry(cargo_form, width=18)

cargo_id.grid(row=0,column=1)
cargo_weight.grid(row=0,column=3)
cargo_profit.grid(row=0,column=5)

cargo_table = ttk.Treeview(cargo_page, columns=("id","wt","pf"), show="headings", height=18)
cargo_table.heading("id", text="Cargo ID")
cargo_table.heading("wt", text="Weight")
cargo_table.heading("pf", text="Profit")
cargo_table.pack(fill="both", expand=True, pady=15)

# =====================================================
# SCHEDULE PAGE
# =====================================================
tk.Label(schedule_page, text="Optimization Result",
         bg="#edf2f7", font=("Arial", 20, "bold")).pack(pady=10)

result_box = tk.Text(schedule_page, font=("Consolas",11))
result_box.pack(fill="both", expand=True, pady=15)

# =====================================================
# CHATBOT PAGE
# =====================================================
tk.Label(chatbot_page,
         text="🤖 Airline AI Assistant",
         bg="#edf2f7",
         font=("Arial",20,"bold")).pack(anchor="w", pady=10)

chat_area = tk.Text(chatbot_page, font=("Arial",11), height=22)
chat_area.pack(fill="x", pady=10)

chat_entry = tk.Entry(chatbot_page, font=("Arial",11))
chat_entry.pack(fill="x", pady=8)

# =====================================================
# FUNCTIONS
# =====================================================
def refresh_all():
    for i in flight_table.get_children():
        flight_table.delete(i)

    for f in flights:
        flight_table.insert("", "end", values=(f["id"], f["capacity"], f["remaining"]))

    for i in cargo_table.get_children():
        cargo_table.delete(i)

    for c in cargo:
        cargo_table.insert("", "end", values=(c["id"], c["weight"], c["profit"]))

    for i in dash_flight.get_children():
        dash_flight.delete(i)

    for f in flights[-8:]:
        dash_flight.insert("", "end", values=(f["id"], f["capacity"]))

    for i in dash_cargo.get_children():
        dash_cargo.delete(i)

    for c in cargo[-8:]:
        dash_cargo.insert("", "end", values=(c["id"], c["profit"]))

    stats[0].config(text=str(len(flights)))
    stats[1].config(text=str(len(cargo)))

def add_flight():
    try:
        cap = int(flight_cap.get())

        flights.append({
            "id": flight_id.get(),
            "capacity": cap,
            "remaining": cap,
            "cargo": [],
            "profit": 0
        })

        flight_id.delete(0,"end")
        flight_cap.delete(0,"end")
        refresh_all()

    except:
        messagebox.showerror("Error","Invalid Flight Data")

def add_cargo():
    try:
        cargo.append({
            "id": cargo_id.get(),
            "weight": int(cargo_weight.get()),
            "profit": int(cargo_profit.get())
        })

        cargo_id.delete(0,"end")
        cargo_weight.delete(0,"end")
        cargo_profit.delete(0,"end")
        refresh_all()

    except:
        messagebox.showerror("Error","Invalid Cargo Data")

def run_schedule():
    assigned = 0
    total = 0

    for f in flights:
        f["remaining"] = f["capacity"]
        f["cargo"] = []
        f["profit"] = 0

    items = sorted(cargo, key=lambda x:x["profit"], reverse=True)

    for item in items:
        for f in flights:
            if f["remaining"] >= item["weight"]:
                f["cargo"].append(item["id"])
                f["remaining"] -= item["weight"]
                f["profit"] += item["profit"]
                assigned += 1
                total += item["profit"]
                break

    result_box.delete("1.0","end")

    for f in flights:
        result_box.insert("end",
            f"Flight : {f['id']}\n"
            f"Cargo  : {', '.join(f['cargo']) if f['cargo'] else 'None'}\n"
            f"Remain : {f['remaining']}\n"
            f"Profit : ₹{f['profit']}\n\n"
        )

    stats[2].config(text=str(assigned))
    stats[3].config(text=str(total))
    system_status.config(text="Scheduling Completed Successfully")
    refresh_all()

def chatbot():
    msg = chat_entry.get().lower().strip()
    if msg == "":
        return

    chat_area.insert("end","You: "+msg+"\n")

    if msg in ["hi","hello"]:
        reply = "Hello! I am Airline Assistant."
    elif msg == "help":
        reply = """Commands:
total flights
show flights
total cargo
show cargo
highest flight
highest cargo
total profit
assigned cargo"""
    elif msg == "total flights":
        reply = f"Total flights: {len(flights)}"
    elif msg == "show flights":
        reply = "\n".join([f"{x['id']} Capacity:{x['capacity']}" for x in flights]) if flights else "No flights added."
    elif msg == "total cargo":
        reply = f"Total cargo: {len(cargo)}"
    elif msg == "show cargo":
        reply = "\n".join([f"{x['id']} Profit:{x['profit']}" for x in cargo]) if cargo else "No cargo added."
    elif msg == "highest flight":
        reply = max(flights,key=lambda x:x["capacity"])["id"] if flights else "No flights"
    elif msg == "highest cargo":
        reply = max(cargo,key=lambda x:x["profit"])["id"] if cargo else "No cargo"
    elif msg == "total profit":
        reply = "₹"+stats[3]["text"]
    elif msg == "assigned cargo":
        reply = stats[2]["text"]
    else:
        reply = "Unknown command. Type help"

    chat_area.insert("end","Bot: "+reply+"\n\n")
    chat_entry.delete(0,"end")

# =====================================================
# BUTTONS
# =====================================================
tk.Button(flight_form, text="Add Flight",
          bg="#2563eb", fg="white",
          width=14, command=add_flight).grid(row=0,column=5,padx=15)

tk.Button(cargo_form, text="Add Cargo",
          bg="#2563eb", fg="white",
          width=14, command=add_cargo).grid(row=0,column=6,padx=15)

tk.Button(schedule_page, text="Run Optimization",
          bg="green", fg="white",
          font=("Arial",12,"bold"),
          width=18, command=run_schedule).pack(pady=10)

tk.Button(chatbot_page, text="Send",
          bg="#2563eb", fg="white",
          width=14, command=chatbot).pack(pady=5)

show_page(dashboard_page)

root.mainloop()