from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

def run_scraper(input_file, output_file):
    # ✅ Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")

    # ✅ Set up Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # ✅ Open the website
    url = "https://egovernance.unom.ac.in/results/ugresult.asp"

    # ✅ Load data from Excel
    data = pd.read_excel(input_file)

    # ✅ Store results
    all_results = []

    for index, row in data.iterrows():
        register_number = str(row["Register Number"])
        dob = str(row["Date of Birth"])

        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='regno']")))

            driver.find_element(By.XPATH, "//input[@name='regno']").send_keys(register_number)
            driver.find_element(By.XPATH, "//input[@name='pwd']").send_keys(dob)

            driver.find_element(By.XPATH, "//input[@value='Get Result']").click()
            time.sleep(3)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            student_info = soup.find_all('table', class_='bordered')[1]
            student_name = student_info.find_all('td')[0].text.strip()

            table = soup.find_all('table', class_='bordered')[2]
            rows = table.find_all('tr')[1:]

            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 5:
                    all_results.append([
                        register_number, dob, student_name,
                        cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip(),
                        cols[3].text.strip(), cols[4].text.strip()
                    ])

        except Exception as e:
            print(f"Error scraping data for {register_number}: {e}")

    driver.quit()

    # ✅ Save results to Excel
    df_results = pd.DataFrame(all_results, columns=[
        "Register Number", "Date of Birth", "Student Name", "Subject Code",
        "UE", "IA", "Total", "Result"
    ])
    df_results.to_excel(output_file, index=False)

