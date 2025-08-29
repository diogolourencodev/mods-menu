import pymem
import customtkinter as ctk
from threading import Thread
import sys

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class DarkSoulsCheatGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Dark Souls Remastered Cheat Menu")
        self.geometry("700x500")
        self.resizable(False, False)
        
        self.pm = None
        self.module_base = None
        self.estus_enabled = False
        
        self.initialize_memory()
        self.create_widgets()
        
    def initialize_memory(self):
        try:
            self.pm = pymem.Pymem("DarkSoulsRemastered.exe")
            self.module_base = pymem.process.module_from_name(
                self.pm.process_handle, "DarkSoulsRemastered.exe"
            ).lpBaseOfDll
            self.connection_status = "Connected ✓"
            self.connection_color = "#2ECC71"

        except pymem.exception.ProcessNotFound:
            self.connection_status = "Process Not Found ✗"
            self.connection_color = "#E74C3C" 
            self.pm = None

        except Exception as e:
            self.connection_status = f"Error: {str(e)}"
            self.connection_color = "#E74C3C"
            self.pm = None
    
    def create_widgets(self):
        
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        header_frame.pack(pady=(15, 10), fill="x", padx=20)
        
        title_label = ctk.CTkLabel(
            header_frame, 
            text="Dark Souls Remastered",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title_label.pack(side="left")
        
        self.status_label = ctk.CTkLabel(
            header_frame, 
            text=self.connection_status,
            text_color=self.connection_color,
            font=ctk.CTkFont(weight="bold")
        )
        self.status_label.pack(side="right")
        
        ctk.CTkFrame(main_frame, height=2, fg_color="#34495E").pack(fill="x", padx=20, pady=10)
        
        cheats_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        cheats_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        estus_frame = ctk.CTkFrame(cheats_frame, corner_radius=10)
        estus_frame.pack(fill="x", pady=(0, 15), padx=5)
        
        estus_header = ctk.CTkFrame(estus_frame, fg_color="transparent")
        estus_header.pack(fill="x", padx=15, pady=(10, 5))
        
        estus_label = ctk.CTkLabel(
            estus_header, 
            text="Infinite Estus Flask",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        estus_label.pack(side="left")
        
        self.estus_status = ctk.CTkLabel(
            estus_header, 
            text="Disabled",
            text_color="#E74C3C",
            font=ctk.CTkFont(weight="bold")
        )
        self.estus_status.pack(side="right")
        
        estus_btn_frame = ctk.CTkFrame(estus_frame, fg_color="transparent")
        estus_btn_frame.pack(fill="x", padx=15, pady=(5, 15))
        
        self.estus_toggle_btn = ctk.CTkButton(
            estus_btn_frame,
            text="Enable Infinite Estus",
            command=self.toggle_estus,
            width=200,
            height=35,
            fg_color="#27AE60",
            hover_color="#219A52"
        )
        self.estus_toggle_btn.pack(pady=5)
        
        souls_frame = ctk.CTkFrame(cheats_frame, corner_radius=10)
        souls_frame.pack(fill="x", pady=(0, 15), padx=5)
        
        souls_header = ctk.CTkFrame(souls_frame, fg_color="transparent")
        souls_header.pack(fill="x", padx=15, pady=(10, 5))
        
        souls_label = ctk.CTkLabel(
            souls_header, 
            text="Max Souls",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        souls_label.pack(side="left")
        
        self.souls_status = ctk.CTkLabel(
            souls_header, 
            text="Not Set",
            text_color="#E74C3C",
            font=ctk.CTkFont(weight="bold")
        )
        self.souls_status.pack(side="right")
        
        souls_input_frame = ctk.CTkFrame(souls_frame, fg_color="transparent")
        souls_input_frame.pack(fill="x", padx=15, pady=(5, 10))
        
        self.souls_address_entry = ctk.CTkEntry(
            souls_input_frame,
            placeholder_text="Address (ex: 118936A4)"
        )
        self.souls_address_entry.pack(side="left", fill="x", expand=True, padx=(0,10))
        
        souls_btn_frame = ctk.CTkFrame(souls_frame, fg_color="transparent")
        souls_btn_frame.pack(fill="x", padx=15, pady=(5, 15))
        
        self.souls_set_btn = ctk.CTkButton(
            souls_btn_frame,
            text="Set Max Souls",
            command=self.set_max_souls,
            width=200,
            height=35,
            fg_color="#3498DB",
            hover_color="#2980B9"
        )
        self.souls_set_btn.pack(pady=5)
        
        footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        footer_frame.pack(fill="x", padx=20, pady=(10, 15))
        
        exit_btn = ctk.CTkButton(
            footer_frame,
            text="Exit",
            command=self.quit_app,
            width=100,
            height=30,
            fg_color="#E74C3C",
            hover_color="#C0392B"
        )
        exit_btn.pack(side="right")
        
        if not self.pm:
            self.disable_all_buttons()
    
    def toggle_estus(self):
        def thread_target():
            try:
                if not self.estus_enabled:
                    result, color = self.infinit_exus(True)
                    if "Activated" in result:
                        self.estus_enabled = True
                        self.estus_status.configure(text="Enabled", text_color="#27AE60")
                        self.estus_toggle_btn.configure(
                            text="Disable Infinite Estus",
                            fg_color="#E74C3C",
                            hover_color="#C0392B"
                        )
                else:
                    result, color = self.infinit_exus(False)
                    if "Deactivated" in result:
                        self.estus_enabled = False
                        self.estus_status.configure(text="Disabled", text_color="#E74C3C")
                        self.estus_toggle_btn.configure(
                            text="Enable Infinite Estus",
                            fg_color="#27AE60",
                            hover_color="#219A52"
                        )
            except Exception as e:
                self.estus_status.configure(text=f"Error: {str(e)}", text_color="#E74C3C")
        
        Thread(target=thread_target, daemon=True).start()
    
    def set_max_souls(self):
        def thread_target():
            try:
                addr_str = f"0x{self.souls_address_entry.get().strip()}"
                val_str = 999999999
                
                if not addr_str or not val_str:
                    self.souls_status.configure(text="Fill in address and amount", text_color="#F39C12")
                    return
                
                if addr_str.startswith("0x") or addr_str.startswith("0X"):
                    address = int(addr_str, 16)
                else:
                    address = int(addr_str)
                
                value = int(val_str)
                self.pm.write_int(address, value)
                
                self.souls_status.configure(text=f"Souls set to {value}!", text_color="#27AE60")
            except Exception as e:
                self.souls_status.configure(text=f"Error: {str(e)}", text_color="#E74C3C")
        
        Thread(target=thread_target, daemon=True).start()
    
    def infinit_exus(self, enable):
        if not self.pm:
            return "Not Connected", "red"
        
        address_exus = self.module_base + 0x74F2A8
        if enable:
            self.pm.write_bytes(address_exus, b"\x90\x90\x90\x90", 4)
            return "Infinit Exus Activated", "lightgreen"
        else:
            original_bytes = b"\x41\x89\x41\x08"
            self.pm.write_bytes(address_exus, original_bytes, len(original_bytes))
            return "Infinit Exus Deactivated", "red"
    
    def disable_all_buttons(self):
        self.estus_toggle_btn.configure(state="disabled")
        self.souls_set_btn.configure(state="disabled")
        self.status_label.configure(text="Not Connected ✗", text_color="#E74C3C")
    
    def quit_app(self):
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = DarkSoulsCheatGUI()
    app.mainloop()
