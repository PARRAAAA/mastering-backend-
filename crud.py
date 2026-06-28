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
    account.balance += amount

    try:
        db.add(transaction)
        db.refresh(transaction)
        db.commit()
    except Exception:
        db.rollback
        raise

    return transaction
