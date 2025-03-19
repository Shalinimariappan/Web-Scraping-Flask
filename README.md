# 🏆 University of Madras Results Scraper using Flask

This is a **Flask-based web scraping project** that automates the extraction of student results from the **University of Madras results portal**. It uses **Selenium**, **BeautifulSoup**, and **Pandas** to extract data and generate a downloadable report in Excel format. The project also includes an email feature to send the extracted data directly to the user.

---

## 🚀 **Features**
✅ Extracts multiple student results from the University of Madras portal.  
✅ Supports batch processing using Excel input files.  
✅ Generates downloadable reports in Excel format.  
✅ Sends extracted results via email.  
✅ Simple and responsive UI using HTML + CSS.  

---

## 📂 **Project Structure**
├── app.py ├── scraper.py ├── email_service.py ├── templates │ ├── index.html │ └── results.html ├── static │ ├── style.css │ └── Hero.png ├── uploads ├── student_results.xlsx ├── README.md └── requirements.txt


---

## ⚙️ **Technologies Used**
- **Flask** – For building the web application.  
- **Selenium** – For automating the scraping process.  
- **BeautifulSoup** – For parsing and extracting HTML content.  
- **Pandas** – For processing and structuring the extracted data.  
- **SMTP** – For sending emails with extracted results.  
- **HTML + CSS** – For creating a clean and responsive UI.  

---

## 🏗️ **Setup & Installation**
### 1. **Clone the repository**
```bash
git clone https://github.com/your-username/university-madras-scraper.git
cd university-madras-scraper
