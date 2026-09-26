# 🎂 Automated Birthday Wisher

A Python automation project that reads birthday information from a CSV file and automatically sends a personalized birthday email to the person whose birthday is today.

This project was created as part of the **100 Days of Code - Python** course by Angela Yu.

---

## ✨ Features

- 📋 Reads birthday information from a CSV file
- 📅 Automatically checks today's date
- 🔎 Finds matching birthdays using a Python dictionary
- 🎲 Randomly selects a birthday letter template
- ✏️ Personalizes the message with the person's name
- 📧 Sends the birthday wish automatically through Gmail
- 🗂️ Supports multiple birthday letter templates

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** – Reading and processing CSV data
- **Datetime** – Getting the current date
- **Random** – Selecting a random birthday template
- **SMTP** – Sending emails
- **OS** – Working with template files
- **Gmail SMTP Server**

---

## 📁 Project Structure

```text
Birthday-Wisher/
│
├── main.py
├── birthdays.csv
│
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
│
└── README.md
