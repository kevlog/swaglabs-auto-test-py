# 🧪 QA Automation Functional Testing

Automated functional testing for the login feature on [saucedemo.com](https://www.saucedemo.com) using Python, Selenium, Pytest, and Allure.

---

## 📂 Project Structure

```bash
saucedemo_automation/
├── conftest.py
├── tests/
│   ├── test_login_positive.py
│   └── test_login_negative.py
├── pages/
│   └── login_page.py
├── utils/
│   └── config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone Repository & Install Dependencies

```bash
git clone https://github.com/kevlog/swaglabs-auto-test-py
cd saucedemo_automation
pip install -r requirements.txt
```

### 2. Create a file `.env`

```bash
SAUCE_USERNAME=standard_user
SAUCE_PASSWORD=secret_sauce
```

### 3. Run Test

```bash
pytest --alluredir=report/
```

### 4. Generate Report

```bash
allure serve report/
```

---

## ✅ Test Scenarios

- Login with valid credential (positive case)
- Login with wrong password (negative case)
- Login with blank of username (negative case)
- Login with blank of password (negative case)

---

## 🧪 Tools

- Python
- Selenium WebDriver
- Pytest
- Allure Reporting
- Dotenv

---

## 📹 Video & Repository

* Video: [YouTube Link](https://www.youtube.com/watch?v=KWv5qShYTng)
  *🕒 Tersedia mulai 18 Juli 2025 pukul 19.00 WIB*
  
* Repository: [GitHub Link](https://github.com/kevlog/swaglabs-auto-test-py)

---

## 📣 Notes

> “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” — *Martin Fowler*