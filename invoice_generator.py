import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class InvoiceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Generator")

        self.company_name_label = tk.Label(root, text="Company Name:")
        self.company_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.company_name_entry = tk.Entry(root)
        self.company_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.items = []

        self.add_item_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.generate_invoice_button = tk.Button(root, text="Generate Invoice", command=self.generate_invoice)
        self.generate_invoice_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.invoice_text = scrolledtext.ScrolledText(root, width=50, height=20)
        self.invoice_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.email_button = tk.Button(root, text="Email Invoice", command=self.email_invoice)
        self.email_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.download_button = tk.Button(root, text="Download Invoice", command=self.download_invoice)
        self.download_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_item(self):
        item_name = simpledialog.askstring("Input", "Enter item name:")
        if item_name is None:
            return
        quantity = simpledialog.askinteger("Input", "Enter quantity:")
        if quantity is None:
            return
        price = simpledialog.askfloat("Input", "Enter price per item:")
        if price is None:
            return

        self.items.append({
            'name': item_name,
            'quantity': quantity,
            'price': price
        })
        messagebox.showinfo("Success", f"Added {item_name} (Quantity: {quantity}, Price: {price})")

    def generate_invoice(self):
        company_name = self.company_name_entry.get()
        if not company_name:
            messagebox.showwarning("Warning", "Please enter a company name.")
            return

        self.invoice_text.delete(1.0, tk.END)  # Clear previous invoice

        self.invoice_text.insert(tk.END, "="*30 + "\n")
        self.invoice_text.insert(tk.END, f"Invoice for: {company_name}\n")
        self.invoice_text.insert(tk.END, "="*30 + "\n")
        self.invoice_text.insert(tk.END, f"{'Item Name':<20} {'Quantity':<10} {'Price':<10} {'Total':<10}\n")
        self.invoice_text.insert(tk.END, "-"*60 + "\n")

        total_sum = 0

        for item in self.items:
            item_name = item['name']
            quantity = item['quantity']
            price = item['price']
            total = quantity * price
            total_sum += total
            self.invoice_text.insert(tk.END, f"{item_name:<20} {quantity:<10} {price:<10} {total:<10}\n")

        self.invoice_text.insert(tk.END, "="*60 + "\n")
        self.invoice_text.insert(tk.END, f"{'Total Sum:':<40} {total_sum:<10}\n")
        self.invoice_text.insert(tk.END, "="*30 + "\n")

    def email_invoice(self):
        sender_email = "xyzxyz@gmail.com"  # Replace with your email
        password = simpledialog.askstring("Input", "Enter your email password:", show='*') #the app specific password
        receiver_email = simpledialog.askstring("Input", "Enter recipient's email:")

        if not receiver_email:
            messagebox.showwarning("Warning", "Please enter a recipient's email.")
            return

        # Prepare the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Invoice from " + self.company_name_entry.get()

        # Create the body of the email
        body = self.invoice_text.get(1.0, tk.END)  # Get the invoice text
        message.attach(MIMEText(body, "plain"))

        try:
            # Send the email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")

    def download_invoice(self):
        # Get the invoice text
        invoice_content = self.invoice_text.get(1.0, tk.END)
        if not invoice_content.strip():
            messagebox.showwarning("Warning", "No invoice to download.")
            return

        # Ask the user where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(invoice_content)
                messagebox.showinfo("Success", "Invoice downloaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save invoice: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InvoiceGenerator(root)
    root.mainloop()
