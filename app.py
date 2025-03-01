import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Directory")
app.geometry("1920x1080")

# Header
header_label = ctk.CTkLabel(app, text="WEBCAM SCANNER", font=("Poppins", 20, "bold"))
header_label.pack(pady=15)

# Main container with 3 columns
main_frame = ctk.CTkFrame(app, fg_color="transparent")
main_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Configure 3 equal columns
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=4)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Left Column - Documents
doc_frame = ctk.CTkFrame(main_frame)
doc_frame.grid(row=0, column=0, padx=5, sticky="nsew")

ctk.CTkLabel(doc_frame, text="Documents", font=("Poppins", 14, "bold")).pack(anchor="w", padx=10, pady=5)

# Document items
doc_items = ["Somplete folder", "somplefile.pdf"]
for item in doc_items:
    ctk.CTkLabel(doc_frame, 
                text=f"📁 {item}" if "folder" in item else f"📄 {item}",
                fg_color="#2A2D2E",
                corner_radius=5).pack(pady=2, padx=10, fill="x")

# Middle Column - Capture Photo
capture_frame = ctk.CTkFrame(main_frame)
capture_frame.grid(row=0, column=1, padx=5, sticky="nsew")

ctk.CTkButton(capture_frame, 
             text="📸 Capture a Photo",
             fg_color="#2CC985",
             hover_color="#229660",
             height=60,
             font=("Poppins", 14, "bold")).place(relx=0.5, rely=0.5, anchor="center")

# Right Column - Properties
prop_frame = ctk.CTkFrame(main_frame)
prop_frame.grid(row=0, column=2, padx=10, sticky="nsew")

ctk.CTkLabel(prop_frame, text="Properties", font=("Poppins", 14, "bold")).pack(anchor="w", padx=10, pady=5)

# Export Format
format_frame = ctk.CTkFrame(prop_frame, fg_color="transparent")
format_frame.pack(pady=5, padx = 10, fill="x")
ctk.CTkLabel(format_frame, text="Export format:").pack(side="left")
format_combo = ctk.CTkComboBox(format_frame, values=["pdf", "docx", "png"], width=100)
format_combo.pack(padx = 10, side="left")
format_combo.set("pdf")


# Export Location
loc_frame = ctk.CTkFrame(prop_frame, fg_color="transparent")
loc_frame.pack(pady=5, padx = 10, fill="x")
ctk.CTkLabel(loc_frame, text="Export Location:").pack(side="left")
ctk.CTkLabel(loc_frame, 
            text="Doc/kompte folder/kompte...",
            fg_color="#2A2D2E",
            corner_radius=5).pack( padx = 10, fill="x")


# Export Button
export_btn = ctk.CTkButton(prop_frame, 
                          text="Export",
                          fg_color="#2CC985",
                          hover_color="#229660",
                          height=40,
                          font=("Poppins", 14, "bold"))
export_btn.pack(pady=20, fill="x", padx=20, side="bottom")

app.mainloop()