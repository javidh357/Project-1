                                                                          # Project-1

                                                                          # 🧾 Invoice PDF Extractor

**Invoice PDF Extractor** is a Python Tkinter-based desktop application that logs into your Gmail account using an app password, searches for emails with "Invoice" in the subject, downloads PDF attachments, extracts key-value text from the PDFs, and displays/export the data in a table and CSV file.

> 🔐 Secure login using Gmail App Password  
> 📩 Filters emails with "Invoice" subject  
> 📁 Downloads PDF attachments  
> 🧾 Extracts invoice data from PDFs  
> 📊 Displays and exports structured data to CSV

---

## 📸 Screenshots

| Login Interface | Extracted Data Table |
|-----------------|----------------------|
| ![Login UI](images/login_ui.png) | ![Data Table](images/data_table.png) |

> 📷 Place your screenshots in a folder named `images/` inside this repo with these filenames.

---

## 🧠 Features

- ✅ Login to Gmail with app password (IMAP)
- ✅ Downloads PDFs with subject containing "Invoice"
- ✅ Extracts key-value pairs from invoice PDFs
- ✅ Displays data in a Treeview table using Tkinter
- ✅ Exports extracted data to `extracted_data.csv`
- ✅ Logs events to `invoice_app.log`

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/invoice-pdf-extractor.git
cd invoice-pdf-extractor

# 2. Install dependencies

pip install pandas PyPDF2

#3. Run the app

python invoice_app.py

📂 Output
attachments/ → downloaded invoice PDFs

extracted_data.csv → structured invoice data

invoice_app.log → log file for actions/debugging

🙌 Author
Made with ❤️ by Javidh
📧 javidhbharoth@gmail.com


---

