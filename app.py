import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Directory")
app.geometry("1920x1080")

# Header
header_label = ctk.CTkLabel(app, text="WEBCAM SCANNER", font=("Arial", 20, "bold"))
header_label.pack(pady=20)

# Create main container frame
main_container = ctk.CTkFrame(app)
main_container.pack(padx=20, pady=10, fill="both", expand=True)

# Configure grid layout for main container
main_container.grid_columnconfigure(0, weight=1)
main_container.grid_columnconfigure(1, weight=1)
main_container.grid_rowconfigure(0, weight=1)

# Documents Section (Left Column)
doc_frame = ctk.CTkFrame(main_container)
doc_frame.grid(row=0, column=0, padx=(0, 10), sticky="nsew")

ctk.CTkLabel(doc_frame, text="Documents", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)

# Document Items
doc_items = [
    ("📁 Stomple folder", "#2CC985"),
    ("📄 somplefile.pdf", "#2CC985")
]

for text, color in doc_items:
    item = ctk.CTkLabel(doc_frame, text=text, font=("Arial", 12),
                        fg_color=color, corner_radius=5)
    item.pack(anchor="w", padx=10, pady=5, fill="x")

# Properties Section (Right Column)
prop_frame = ctk.CTkFrame(main_container)
prop_frame.grid(row=0, column=1, padx=(10, 0), sticky="nsew")

ctk.CTkLabel(prop_frame, text="Properties", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)

# Export Format
format_frame = ctk.CTkFrame(prop_frame, fg_color="transparent")
format_frame.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(format_frame, text="Export format:", width=100).pack(side="left")
format_combo = ctk.CTkComboBox(format_frame, values=["pdf", "docx", "png"], width=100)
format_combo.pack(side="left")
format_combo.set("pdf")

# Export Location
loc_frame = ctk.CTkFrame(prop_frame, fg_color="transparent")
loc_frame.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(loc_frame, text="Export Location:", width=100).pack(side="left")
ctk.CTkLabel(loc_frame, text="Doc/example folder/sample...", 
            fg_color="#2A2D2E", corner_radius=5).pack(side="left", fill="x", expand=True)

# Drop Area
drop_frame = ctk.CTkFrame(app, height=100, fg_color="#1F1F1F")
drop_frame.pack(padx=20, pady=20, fill="x", expand=True)
ctk.CTkLabel(drop_frame, text="Drop files here or capture photo", 
             text_color="#666666").place(relx=0.5, rely=0.5, anchor="center")

# Export Button
export_btn = ctk.CTkButton(app, text="Export", fg_color="#2CC985", hover_color="#229660",
                          height=40, font=("Arial", 14, "bold"))
export_btn.pack(padx=20, pady=(0, 20), fill="x")

app.mainloop()