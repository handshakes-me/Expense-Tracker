# 💰 PyBudget – Personal Expense Tracker

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, intuitive, and powerful expense tracking application built with Python and Kivy. Keep track of your income and expenses with ease.

---

## ✨ Features

- Track income and expenses with ease  
- View detailed transaction history  
- See monthly and yearly financial summaries  
- Categorize transactions for better insights  
- Persist data with an SQLite database  
- Enjoy a clean and intuitive user interface  
- Responsive design for desktop and mobile platforms  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher  
- pip (Python package manager)  
- Kivy 2.0.0 or higher  
- SQLAlchemy 1.4.0 or higher  

### Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/handshakes-me/Expense-Tracker.git
   cd Expense-Tracker
   ```

2. Create and activate a virtual environment  
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Once dependencies are installed, start the app with:

```bash
python -m expense_tracker.main
```

---

## 🎨 Project Structure

```
Expense-Tracker/
├── expense_tracker/         # Main application package
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models.py            # Database models
│   └── ui/                  # UI components
│       ├── __init__.py
│       ├── dashboard.kv     # Dashboard UI markup
│       ├── dashboard.py     # Dashboard logic
│       ├── add_transaction.py  # Add transaction screen
│       └── styles.kv        # Global styles
├── assets/                  # Static assets (images, icons)
├── .gitignore
├── LICENSE                  # MIT License
├── README.md
└── requirements.txt
```

---

## 📝 Usage

### Adding a Transaction

- Click on **Add New Transaction**  
- Select transaction type (Income or Expense)  
- Enter amount and category  
- Add an optional description  
- Click **Save**  

### Viewing Transactions

- Recent transactions appear on the dashboard  
- Check monthly summaries and totals  
- Monitor your financial health at a glance  

---

## 🤝 Contributing

Contributions are welcome! To propose a change:

1. Fork the repository  
2. Create your feature branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes  
   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. Push to the branch  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request  

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Kivy](https://kivy.org/)  
- Icons from [Material Design Icons](https://material.io/resources/icons/)  
- Inspired by modern expense tracking applications  
