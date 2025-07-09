import tkinter as tk
from tkinter import messagebox, scrolledtext
from fpdf import FPDF

class PDFResume(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, f"{self.name} - Resume", ln=True, align="C")
        self.ln(5)
     
    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln(4)

def generate_pdf():
    pdf = PDFResume()
    pdf.name = name_entry.get()

    pdf.add_page()
    
    #Header Info
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, name_entry.get(), ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, location_entry.get(), ln=True)
    pdf.cell(0, 10, contact_entry.get(), ln=True)
    pdf.ln(10)

    #Summary
    pdf.chapter_title("Summary")
    pdf.chapter_body(summary_text.get("1.0", tk.END))

    #Skills
    pdf.chapter_title("Core Technical Skills")
    pdf.chapter_body(skills_text.get("1.0", tk.END))

    #Experience
    pdf.chapter_title("Professional Experience")
    pdf.chapter_body(experience_text.get("1.0", tk.END))

    #Education
    pdf.chapter_title("Education")
    pdf.chapter_body(education_text.get("1.0", tk.END))

    try:
        filename = name_entry.get().replace(" ", "_") +"_Resume.pdf"
        pdf.output(filename)
        messagebox.showinfo("Success", f"PDF Resume saved as {filename}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

#GUI
root = tk.Tk()
root.title("PDF Resume Builder")
root.geometry("700x800")

def labeled_entry(label_text):
    tk.Label(root, text=label_text).pack()
    entry = tk.Entry(root, width=100)
    entry.pack(pady=2)
    return entry

def labeled_textbox(label_text, height=6):
    tk.Label(root, text=label_text).pack()
    box = scrolledtext.ScrolledText(root, height=height, width=100)
    box.pack(pady=2)
    return box

name_entry =labeled_entry("Full Name:")
location_entry = labeled_entry("Location:")
contact_entry =labeled_entry("Email and Phone:")
links_entry = labeled_entry("Links (GitHub, Gumroad, etc.):")

summary_text = labeled_textbox("Summary / Headline:")
skills_text = labeled_textbox("Skill:")
experience_text = labeled_textbox("Experience:")
education_text = labeled_textbox("Education:")

tk.Button(root, text="Generate PDF Resume", command=generate_pdf, bg="#4CAF50", fg="white", height=2).pack(pady=10)

root.mainloop()
 
