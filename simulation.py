import tkinter as tk
from tkinter import ttk
import random
import time
import threading

class RoboRakshaCommandCenter:
    def __init__(self, root):
        self.root = root
        self.root.title("ROBO RAKSHA - AI EMERGENCY RESPONSE UNIT")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0a0a0a")

        # System Variables
        self.robot_location = "Sector Alpha-7"
        self.is_patrolling = True
        self.emergency_types = {
            "FIRE": {"units": "Fire Brigade", "base_count": 5, "color": "#ff4444"},
            "VIOLENCE/MURDER": {"units": "Tactical Police", "base_count": 4, "color": "#ff0055"},
            "EARTHQUAKE": {"units": "Disaster Response Force", "base_count": 10, "color": "#ffaa00"},
            "MEDICAL EMERGENCY": {"units": "Ambulance/Paramedics", "base_count": 2, "color": "#00ffcc"}
        }

        self.setup_ui()
        self.start_ai_logic()

    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="SYSTEM STATUS: PROTECTING CITY SECTOR 01", font=("Courier", 20, "bold"), fg="#00ffcc", bg="#0a0a0a")
        header.pack(pady=10)

        # Main Layout: Left (Live Feed) and Right (Data)
        main_frame = tk.Frame(self.root, bg="#0a0a0a")
        main_frame.pack(fill="both", expand=True, padx=20)

        # --- LIVE FEED SIMULATION ---
        self.feed_frame = tk.Frame(main_frame, width=600, height=400, bg="#1a1a1a", highlightbackground="#00ffcc", highlightthickness=2)
        self.feed_frame.pack(side="left", padx=10)
        self.feed_frame.pack_propagate(False)

        self.feed_label = tk.Label(self.feed_frame, text="[ LIVE FEED - RAKSHA-01 ]", fg="#00ffcc", bg="#1a1a1a", font=("Courier", 10))
        self.feed_label.pack()

        self.canvas = tk.Canvas(self.feed_frame, width=580, height=350, bg="black", highlightthickness=0)
        self.canvas.pack(pady=5)
        
        # --- DATA SIDEBAR ---
        sidebar = tk.Frame(main_frame, bg="#0a0a0a")
        sidebar.pack(side="right", fill="both", expand=True)

        self.status_box = tk.Text(sidebar, height=15, width=40, bg="#000", fg="#00ffcc", font=("Courier", 10), state="disabled")
        self.status_box.pack(pady=5)

        self.intensity_label = tk.Label(sidebar, text="THREAT LEVEL: NONE", font=("Courier", 14, "bold"), fg="#00ffcc", bg="#0a0a0a")
        self.intensity_label.pack(pady=20)

        self.dispatch_btn = tk.Button(sidebar, text="SYSTEMS ACTIVE", font=("Courier", 12, "bold"), bg="#00ffcc", fg="black", state="disabled")
        self.dispatch_btn.pack(pady=10, fill="x")

    def log_event(self, message):
        self.status_box.config(state="normal")
        self.status_box.insert("end", f"> {message}\n")
        self.status_box.see("end")
        self.status_box.config(state="disabled")

    def update_visual_feed(self, alert=False):
        """Simulates visual AI scanning on the canvas."""
        self.canvas.delete("all")
        color = "#00ffcc" if not alert else "red"
        
        # Draw scanning lines
        for _ in range(5):
            x = random.randint(0, 580)
            self.canvas.create_line(x, 0, x, 350, fill=color, dash=(4, 4))
        
        # Draw random "Detection Boxes"
        for _ in range(random.randint(1, 3)):
            x1, y1 = random.randint(50, 400), random.randint(50, 250)
            self.canvas.create_rectangle(x1, y1, x1+100, y1+60, outline=color, width=2)
            self.canvas.create_text(x1+50, y1-10, text="SCANNING...", fill=color, font=("Courier", 8))

    def trigger_emergency(self):
        # Randomly select a threat
        threat_name = random.choice(list(self.emergency_types.keys()))
        intensity = random.choice(["LOW", "MID", "HIGH", "CRITICAL"])
        data = self.emergency_types[threat_name]
        
        # Calculate personnel needed
        multiplier = {"LOW": 1, "MID": 2, "HIGH": 4, "CRITICAL": 8}
        personnel_count = data['base_count'] * multiplier[intensity]
        
        # UI Update
        self.intensity_label.config(text=f"THREAT: {threat_name}\nLEVEL: {intensity}", fg=data['color'])
        self.log_event(f"!!! {threat_name} DETECTED !!!")
        self.log_event(f"LOCATION: {random.randint(100, 999)}:{random.randint(100,999)}")
        self.log_event(f"INTENSITY: {intensity}")
        self.log_event(f"DISPATCHING: {personnel_count} {data['units']}")
        
        # Visual alert
        for _ in range(6):
            self.feed_frame.config(highlightbackground="red")
            self.root.update()
            time.sleep(0.1)
            self.feed_frame.config(highlightbackground="#00ffcc")
            self.root.update()
            time.sleep(0.1)

    def start_ai_logic(self):
        def loop():
            while True:
                # Update feed visuals
                self.update_visual_feed()
                
                # Random chance of emergency
                if random.random() < 0.2: # 20% chance every cycle
                    self.trigger_emergency()
                    time.sleep(4) # Pause to show the emergency
                else:
                    self.intensity_label.config(text="THREAT LEVEL: NONE", fg="#00ffcc")
                    self.log_event(f"Patrolling {random.choice(['Sector A', 'Sector B', 'Sector C'])}...")
                
                time.sleep(1)

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = RoboRakshaCommandCenter(root)
    root.mainloop()