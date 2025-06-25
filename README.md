# 💰 PyBudget - Personal Expense Tracker

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, intuitive, and powerful expense tracking application built with Python and Kivy. Keep track of your income and expenses with ease.

![PyBudget Dashboard](assets/screenshot.png)
*Dashboard view showing transaction history and financial summary*

## ✨ Features

- 💰 Track income and expenses with ease
- 📊 View detailed transaction history
- 📅 Monthly and yearly financial summaries
- 🏷️ Categorize transactions for better insights
- 🔄 Data persistence with SQLite database
- 🎨 Clean and intuitive user interface
- 📱 Responsive design that works on multiple platforms

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/handshakes-me/Expense-Tracker.git
   cd Expense-Tracker
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python -m expense_tracker.main
   ```

## 📦 Project Structure

```
Expense-Tracker/
├── expense_tracker/       # Main application package
│   ├── __init__.py
│   ├── main.py           # Application entry point
│   ├── models.py         # Database models
│   └── ui/               # UI components
│       ├── __init__.py
│       ├── dashboard.kv  # Dashboard UI
│       ├── dashboard.py  # Dashboard logic
│       ├── add_transaction.py  # Add transaction screen
│       └── styles.kv     # Global styles
├── assets/               # Static assets (images, etc.)
├── .gitignore
├── README.md
└── requirements.txt
```

## 📝 Usage

1. **Adding a Transaction**
   - Click on "Add New Transaction"
   - Select transaction type (Income/Expense)
   - Enter amount and category
   - Add an optional description
   - Click "Save"

2. **Viewing Transactions**
   - The dashboard shows recent transactions
   - View monthly summaries and totals
   - Track your financial health at a glance

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Kivy](https://kivy.org/)
- Icons from [Material Design Icons](https://material.io/resources/icons/)
- Inspired by modern expense tracking applications

## Requirements

- Python 3.7+
- Kivy 2.0.0+
- SQLAlchemy 1.4.0+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PyBudget.git
   cd PyBudget
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python -m expense_tracker.main
```

## Project Structure

```
PyBudget/
├── expense_tracker/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── ui/
│       ├── __init__.py
│       ├── dashboard.kv
│       ├── dashboard.py
│       ├── add_transaction.py
│       └── styles.kv
├── README.md
├── requirements.txt
└── .gitignore
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
