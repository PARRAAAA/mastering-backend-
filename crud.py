from decimal import Decimal
from sqlalchemy.orm import Session
from models import Account, Transaction


def create_transaction(
    db: Session, account_id: int, amount: float, description: str, category: str
) -> Transaction:
    account = db.query(Account).filter(Account.id == account_id).first()
    if account is None:
        raise ValueError("Account not found")

    transaction = Transaction(
        account_id=account_id,
        amount=amount,
        description=description,
        category=category,
    )
    account.balance += Decimal(str(amount))

    try:
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
    except Exception:
        db.rollback()
        raise

    return transaction

def create_account(db: Session, name:str) → Account:
    account = Account(name=name)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account 
    
