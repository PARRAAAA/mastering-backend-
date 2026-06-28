from models import Account
from crud import create_transaction


def test_create_transaction_updates_balance(db_session):
    account = Account(name="Checking")
    db_session.add(account)
    db_session.commit()

    create_transaction(
        db=db_session,
        account_id=account.id,
        amount=-50.0,
        description="Groceries",
        category="Food",
    )

    db_session.refresh(account)
    assert account.balance == -50.0
