# Invoice PDF Extractor

A Python-based GUI application that automatically logs into your Gmail, searches for invoice emails with PDF attachments, extracts data from those PDFs, and exports it into a CSV file for analysis. Built with `Tkinter`, `PyPDF2`, and `pandas`.

---

## Features

-  GUI-based email login and configuration using Tkinter  
-  Automatically fetch invoice emails with PDFs using IMAP  
-  Extracts key information from PDF files (e.g., invoice number, amount)  
-  Exports data to CSV for easy viewing and analysis  
-  Save downloaded PDFs locally  
-  Detailed logging for easy debugging

---

##  GUI Preview

> Add screenshots here in the `images/` folder and reference them like below:
![App Screenshot](images/gui-screenshot.png)

---

##  Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/javidh357/Project-1.git
   cd Project-1
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Gmail App Password**

   For security, enable 2-Step Verification on your Gmail and [generate an App Password](https://support.google.com/accounts/answer/185833?hl=en) to use in this app.

---

##  How It Works

1. User logs into Gmail via GUI using App Password.
2. App connects to Gmail inbox via IMAP and searches for emails with a specific subject (e.g., "Invoice").
3. PDF attachments are downloaded and parsed for invoice data using PyPDF2.
4. Extracted data is shown in a table and exported to CSV.

---

##  File Structure

```bash
Project-1/
├── main.py               # Main application script
├── requirements.txt      # Required Python packages
├── output/               # Extracted CSV files
├── logs/                 # Log files
└── images/               # Screenshots for README
```

---

##  Requirements

- Python 3.7+
- Internet connection (for Gmail)
- Gmail App Password

---

##  Packages Used

- `Tkinter` – for the GUI
- `imaplib` – for email fetching
- `email` – for email decoding
- `PyPDF2` – for PDF reading
- `pandas` – for data manipulation and CSV export
- `logging` – for activity tracking

---

##  Security Note

> This app uses direct email login. Avoid using your main password; **use an App Password** generated via Gmail settings.

---

##  To-Do / Improvements

- [ ] Improve PDF extraction with regex or OCR
- [ ] Add progress bars or status indicators in GUI
- [ ] Add date range/email sender filters
- [ ] Package app into a standalone `.exe` (via `pyinstaller`)
- [ ] Add automated tests

---

##  Contribution

Feel free to fork this repo, improve it, and create a pull request! Suggestions, issues, and bug reports are welcome.

---

##  License

This project is licensed under the MIT License.

---

##  Author

**Javidh**  
🔗 [GitHub Profile](https://github.com/javidh357)
