# Expense Tracker

A simple and intuitive expense tracking application built with Python and Kivy.

## Features

- Track income and expenses
- Categorize transactions
- View balance and transaction history
- Simple and clean user interface
- Local SQLite database storage

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd expense_tracker
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

## Usage

1. **Dashboard**
   - View your current balance
   - See income and expense totals
   - Quick access to add new transactions

2. **Add Transaction**
   - Choose between income and expense
   - Enter amount and select category
   - Add an optional description

3. **View History**
   - See all your transactions
   - Filter by date and category (coming soon)

## Project Structure

```
expense_tracker/
├── main.py          # Application entry point
├── models.py        # Database models and setup
├── requirements.txt # Dependencies
├── db.sqlite3       # Database file (created on first run)
└── ui/             # UI components
    ├── __init__.py
    ├── dashboard.kv
    ├── dashboard.py
    ├── add_txn.kv
    ├── add_transaction.py
    └── styles.kv
```

## Dependencies

- Python 3.7+
- Kivy 2.0.0+
- SQLAlchemy 1.4.0+

## License

MIT
