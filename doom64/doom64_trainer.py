import pymem
import customtkinter as ctk
import threading
import time

try:
    pm = pymem.Pymem("DOOM64_x64.exe")
except pymem.exception.ProcessNotFound:
    print("Error: DOOM64_x64.exe process not found!")
    exit()

addresses = [0x14075B298, 0x14075B29C, 0x14075B250, 0x14075B254]
god_value = 999

running = False
ammo_enabled = False
armor_enabled = False

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 

def update_values_loop():
    """Continuous loop to update values in memory"""
    global running, ammo_enabled, armor_enabled
    
    while running:
        try:
            if ammo_enabled:
                pm.write_int(addresses[0], god_value) 
                pm.write_int(addresses[1], god_value)
            
            if armor_enabled:
                pm.write_int(addresses[2], god_value)
                pm.write_int(addresses[3], god_value) 
                
            time.sleep(0.1)
        except Exception as e:
            print(f"Write error: {e}")
            running = False
            status.set("Error: Game disconnected")
            status_label.configure(text_color="red")
            break

def set_ammo(enable: bool):
    """Toggles infinite ammo"""
    global ammo_enabled
    ammo_enabled = enable
    
    if enable:
        return "Infinite Ammo Activated", "#2E8B57" 
    else:
        return "Infinite Ammo Deactivated", "#DC143C" 
def set_armor(enable: bool):
    """Toggles infinite armor"""
    global armor_enabled
    armor_enabled = enable
    
    if enable:
        return "Infinite Armor Activated", "#2E8B57" 
    else:
        return "Infinite Armor Deactivated", "#DC143C" 

def toggle_ammo():
    "Ammo checkbox callback"""
    msg, color = set_ammo(checkbox_ammo.get())
    status.set(msg)
    status_label.configure(text_color=color)

def toggle_armor():
    """Armor checkbox callback"""
    msg, color = set_armor(checkbox_armor.get())
    status.set(msg)
    status_label.configure(text_color=color)

def on_closing():
    """Function called when closing the window"""
    global running
    running = False
    app.destroy()

app = ctk.CTk()
app.title("DOOM64 Trainer")
app.geometry("500x400")
app.resizable(False, False)
app.protocol("WM_DELETE_WINDOW", on_closing)

main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

title_label = ctk.CTkLabel(main_frame, text="DOOM64 TRAINER", 
                          font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=(20, 10))

subtitle_label = ctk.CTkLabel(main_frame, text="Game Memory Editor", 
                             font=ctk.CTkFont(size=14), text_color="gray")
subtitle_label.pack(pady=(0, 20))

options_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
options_frame.pack(pady=10, padx=30, fill="both")

checkbox_ammo = ctk.CTkCheckBox(options_frame, text="💣 Infinite Ammo", 
                               command=toggle_ammo, font=ctk.CTkFont(size=16))
checkbox_ammo.pack(anchor="w", pady=15, padx=20)

checkbox_armor = ctk.CTkCheckBox(options_frame, text="🛡️ Infinite Armor", 
                                command=toggle_armor, font=ctk.CTkFont(size=16))
checkbox_armor.pack(anchor="w", pady=15, padx=20)

separator = ctk.CTkFrame(main_frame, height=2, fg_color="gray")
separator.pack(fill="x", padx=40, pady=20)

status = ctk.StringVar(value="Select options to activate cheats")
status_label = ctk.CTkLabel(main_frame, textvariable=status, 
                           font=ctk.CTkFont(size=14, weight="bold"))
status_label.pack(pady=20)

info_frame = ctk.CTkFrame(main_frame, fg_color="#1c1c1c")
info_frame.pack(pady=10, padx=20, fill="x")

info_text = """
• Make sure DOOM64 is running before activating cheats
• Cheats are applied in real-time to game memory
• Disable cheats before closing the game
"""
info_label = ctk.CTkLabel(info_frame, text=info_text, justify="left",
                         font=ctk.CTkFont(size=12), text_color="lightgray")
info_label.pack(pady=10, padx=10)

running = True
update_thread = threading.Thread(target=update_values_loop, daemon=True)
update_thread.start()

def main():
    app.mainloop()

if __name__ == "__main__":
    main()
