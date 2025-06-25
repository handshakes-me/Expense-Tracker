from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from models import init_db
import os

# Import screens
from ui.dashboard import DashboardScreen
from ui.add_transaction import AddTransactionScreen

class ExpenseTrackerApp(App):
    def build(self):
        # Initialize database
        if not os.path.exists('db.sqlite3'):
            init_db()
        
        # Load all .kv files
        Builder.load_file('ui/dashboard.kv')
        Builder.load_file('ui/add_txn.kv')
        Builder.load_file('ui/styles.kv')
        
        # Create screen manager
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(AddTransactionScreen(name='add_transaction'))
        
        return sm

if __name__ == '__main__':
    Window.size = (400, 700)  # Mobile-like window size
    ExpenseTrackerApp().run()
