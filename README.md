🧾 Smart Invoice Generator – Automate Billing with Email & Download Features



👤 Author

Vedant Choudhari
AIDS, SIES Graduate School of Technology

📌 Project Overview

In the digital age, manual invoice handling is not just outdated — it’s inefficient and error-prone. The Smart Invoice Generator streamlines invoice creation with a Python-based GUI that allows users to generate, email, and download invoices in just a few clicks.

This system is ideal for freelancers, small businesses, and startups looking to simplify their billing process without relying on external tools or paid services.

🎯 Problem Solved

❌ Manual errors in invoices

⏱️ Time-consuming calculations and formatting

📤 Lack of automation in invoice distribution

The solution:

📋 Add items dynamically

📄 Auto-generate structured invoices

📧 Email invoices via Gmail

💾 Download invoice as .txt files

⚙️ Technologies Used

Component

Technology

Language

Python 3.10+

GUI

tkinter

Email

smtplib, email.mime

File Save

filedialog

🧩 Functional Modules

add_item() – Prompt-based item addition (name, quantity, price)

generate_invoice() – Formats and displays the complete invoice

email_invoice() – Sends invoice to client via SMTP

download_invoice() – Saves invoice as a text file

🖥️ System Architecture

Frontend: tkinter-based GUI

Backend: Python business logic for item management, calculations, and integration with email and filesystem

🖼️ Sample Output Screenshots

Main Application Interface



Item Addition Dialog



Quantity and Price Inputs



Invoice Display



Email Confirmation



All interactions are visual and beginner-friendly, designed for maximum usability.

🚀 How to Run

Clone the repo:

git clone https://github.com/yourusername/invoice-generator.git
cd invoice-generator

Run the app:

python invoice_generator.py

What you’ll need:

Python 3.10 or newer

Internet access (for emailing via Gmail)

🔐 Email Integration Notes

Emails are sent using smtp.gmail.com

At runtime, the app will securely prompt for:

Sender Gmail password

Recipient email address

For better security, generate an App Password if 2FA is enabled

✅ Results

The application was tested extensively with:

Multiple invoice entries

Edge cases (empty fields, invalid input)

Sending emails successfully

Invoice saving tested across multiple paths

✅ Outcome:

Smooth performance

No crashes

Clear outputs

User-friendly experience

📦 Future Improvements

Export to PDF

Add customer database

Integrate QR codes for payment links

Cloud sync / dashboard features

📃 License

This project is open-source and available under the MIT License.

🙌 Acknowledgment

Built as part of the Skill Lab at SIES Graduate School of Technology, Navi Mumbai.

