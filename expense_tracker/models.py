from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import enum

# Create SQLAlchemy engine and session
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class TransactionType(enum.Enum):
    INCOME = "Income"
    EXPENSE = "Expense"

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String(200))
    category = Column(String(50), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    date = Column(Date, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Transaction(amount={self.amount}, type={self.transaction_type.value}, category={self.category})>"

def init_db():
    # Create all tables
    Base.metadata.create_all(engine)
    
    # Create a default session
    session = Session()
    
    # Add some default categories
    # Note: In a real app, you might want to manage categories separately
    default_transactions = [
        # Add sample transactions here if needed
    ]
    
    try:
        session.add_all(default_transactions)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
