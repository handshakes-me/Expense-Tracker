from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock
from models import Session, Transaction, TransactionType
from datetime import datetime

class AddTransactionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._session = None
        self.transaction_type = 'expense'  # Default to expense
        self.categories = {
            'income': ['Salary', 'Freelance', 'Gift', 'Other'],
            'expense': ['Food', 'Transportation', 'Shopping', 'Bills', 'Entertainment', 'Other']
        }
        
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
    
    def on_pre_enter(self):
        # Reset form when entering the screen
        self.ids.amount_input.text = ''
        self.ids.description_input.text = ''
        self.ids.category_spinner.values = self.categories[self.transaction_type]
        if self.ids.category_spinner.values:
            self.ids.category_spinner.text = self.ids.category_spinner.values[0]
    
    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type
        # Update categories based on transaction type
        self.ids.category_spinner.values = self.categories[transaction_type]
        if self.ids.category_spinner.values:
            self.ids.category_spinner.text = self.ids.category_spinner.values[0]
    
    def save_transaction(self):
        try:
            # Get a fresh session
            self.refresh_session()
            
            amount = float(self.ids.amount_input.text)
            description = self.ids.description_input.text.strip()
            category = self.ids.category_spinner.text
            
            if amount <= 0:
                self.show_message('Error', 'Amount must be greater than 0')
                return
                
            if not category:
                self.show_message('Error', 'Please select a category')
                return
            
            try:
                # Create new transaction
                transaction = Transaction(
                    amount=amount,
                    description=description,
                    category=category,
                    transaction_type=TransactionType.INCOME if self.transaction_type == 'income' else TransactionType.EXPENSE,
                    date=datetime.now()
                )
                
                self.session.add(transaction)
                self.session.commit()
                
                # Commit the transaction
                self.session.commit()
                print("Transaction saved successfully")
                
                # Clear the form
                self.ids.amount_input.text = ''
                self.ids.description_input.text = ''
                
                # Commit the transaction
                self.session.commit()
                print("Transaction saved successfully")
                
                # Clear the form
                self.ids.amount_input.text = ''
                self.ids.description_input.text = ''
                
                # Get the dashboard and update it directly
                dashboard = self.manager.get_screen('dashboard')
                dashboard.refresh_session()
                
                # Switch back to dashboard
                self.manager.current = 'dashboard'
                
                # Update the dashboard UI
                dashboard.update_balance()
                
                # Force a UI update
                if hasattr(dashboard, 'ids'):
                    for widget in dashboard.ids.values():
                        if hasattr(widget, 'do_layout'):
                            widget.do_layout()
                
            except Exception as e:
                self.session.rollback()
                raise e
            
        except ValueError:
            self.show_message('Error', 'Please enter a valid amount')
        except Exception as e:
            self.session.rollback()
            self.show_message('Error', f'Failed to save transaction: {str(e)}')
    
    def show_message(self, title, message):
        # In a real app, you might want to show a popup here
        print(f"{title}: {message}")
    
    def go_back(self):
        self.manager.current = 'dashboard'
