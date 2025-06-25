from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Rectangle, Canvas
from kivy.metrics import dp
from models import Session, Transaction, TransactionType
from datetime import datetime, timedelta
from kivy.utils import get_color_from_hex

class TransactionItem(BoxLayout):
    transaction_type = StringProperty('')
    amount = StringProperty('0.00')
    category = StringProperty('')
    date = StringProperty('')
    description = StringProperty('')
    
    def __init__(self, transaction, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 60
        self.padding = [10, 5]
        self.spacing = 15
        
        # Debug print
        print(f"Creating TransactionItem: {transaction.id} - {transaction.transaction_type} {transaction.amount}")
        
        # Store the raw transaction for debugging
        self._transaction = transaction
        
        # Set properties - this will trigger the property observers
        self.transaction_type = 'income' if transaction.transaction_type == TransactionType.INCOME else 'expense'
        self.amount = f"{float(transaction.amount):,.2f}"  # Ensure it's a float
        self.category = transaction.category or 'Uncategorized'
        self.date = transaction.date.strftime('%b %d, %Y') if transaction.date else 'Unknown Date'
        self.description = transaction.description or ''
        
        # Debug print after setting properties
        print(f"  - Type: {self.transaction_type}")
        print(f"  - Amount: {self.amount}")
        print(f"  - Category: {self.category}")
        print(f"  - Date: {self.date}")
        print(f"  - Description: {self.description}")

class DashboardScreen(Screen):
    balance = StringProperty("₹0.00")
    income = StringProperty("₹0.00")
    expense = StringProperty("₹0.00")
    transactions_container = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._session = None
        self.update_balance()
        
    @property
    def session(self):
        if self._session is None:
            self._session = Session()
        return self._session
        
    def refresh_session(self):
        """Close the current session and create a new one"""
        if self._session:
            self._session.close()
            self._session = None
        return self.session
        
    def on_enter(self):
        # Update the balance and recent transactions when the screen is shown
        self.update_balance()
        
        # Force a refresh of the layout
        if hasattr(self, 'transactions_container'):
            self.transactions_container.height = self.transactions_container.minimum_height
            self.transactions_container.do_layout()
        
    def update_balance(self):
        print("\n=== Starting update_balance ===")
        try:
            self.refresh_session()
            today = datetime.now()
            first_day = today.replace(day=1)
            
            print(f"Fetching transactions from {first_day} to {today}")
            
            # Fetch monthly transactions
            monthly_transactions = self.session.query(Transaction).filter(
                Transaction.date >= first_day,
                Transaction.date <= today
            ).all()
            
            # Fetch recent transactions (last 10)
            recent_transactions = self.session.query(Transaction).order_by(
                Transaction.date.desc()
            ).limit(10).all()
            
            # Debug print transactions
            print(f"\n=== Monthly Transactions ({len(monthly_transactions)}) ===")
            for t in monthly_transactions:
                print(f"- {t.date}: {t.transaction_type} - {t.amount} ({t.category})")
                
            print(f"\n=== Recent Transactions ({len(recent_transactions)}) ===")
            for t in recent_transactions:
                print(f"- {t.date}: {t.transaction_type} - {t.amount} ({t.category})")
            
            # Calculate totals
            total_income = 0.0
            total_expense = 0.0
            
            for t in monthly_transactions:
                if t.transaction_type == TransactionType.INCOME:
                    total_income += float(t.amount) if t.amount else 0.0
                else:
                    total_expense += float(t.amount) if t.amount else 0.0
            
            # Update properties
            balance = total_income - total_expense
            self.balance = f"₹{balance:,.2f}"
            self.income = f"₹{total_income:,.2f}"
            self.expense = f"₹{total_expense:,.2f}"
            
            print(f"\n=== Calculated Totals ===")
            print(f"Total Income: {total_income}")
            print(f"Total Expense: {total_expense}")
            print(f"Balance: {balance}")
            
            # Update recent transactions - ensure we have a fresh list
            print(f"\nUpdating recent transactions with {len(recent_transactions)} items")
            self.update_recent_transactions(recent_transactions)
            
            # Force UI update
            if hasattr(self, 'ids'):
                print("Triggering UI layout update...")
                for widget_id, widget in self.ids.items():
                    if hasattr(widget, 'do_layout'):
                        print(f"  - Updating layout for widget: {widget_id}")
                        widget.do_layout()
            
            print("=== End update_balance ===\n")
            return True
            
        except Exception as e:
            print(f"Error in update_balance: {e}")
            import traceback
            traceback.print_exc()
            return False
            
    def update_recent_transactions(self, transactions):
        print(f"\n=== Updating recent transactions: {len(transactions)} transactions ===")
        
        # Get the transactions container
        if not hasattr(self, 'transactions_container') or not self.transactions_container:
            print("Error: transactions_container not found")
            return
            
        # Clear existing transactions
        self.transactions_container.clear_widgets()
        
        if not transactions:
            no_transactions = Label(
                text="No recent transactions.\nAdd your first transaction!",
                halign='center',
                color=(0.5, 0.5, 0.5, 1),
                font_size='14sp',
                size_hint_y=None,
                height=100
            )
            self.transactions_container.add_widget(no_transactions)
            return
            
        # Add all transactions
        for transaction in transactions:
            print(f"Adding transaction: {transaction.id} - {transaction.transaction_type} {transaction.amount}")
            try:
                # Create a new TransactionItem with the transaction data
                item = TransactionItem(transaction)
                self.transactions_container.add_widget(item)
            except Exception as e:
                print(f"Error creating transaction item: {e}")
                import traceback
                traceback.print_exc()
        
        # Force layout update
        self.transactions_container.height = self.transactions_container.minimum_height
        self.transactions_container.do_layout()
        
        print(f"Total widgets in container: {len(self.transactions_container.children)}")
        print("=== Finished updating transactions ===\n")
        
    def add_transaction(self):
        self.manager.current = 'add_transaction'
        
    def view_transactions(self):
        # TODO: Implement transaction list view
        pass
        
    def view_reports(self):
        # TODO: Implement reports view
        pass
