import pytest
from sqlalchemy.exc import IntegrityError
from models import Account, Transaction


def test_create_account(db_session):
    account = Account(name="Checking")
    db_session.add(account)
    db_session.commit()

    assert account.id is not None
    assert account.balance == 0.0


def test_transaction_belongs_to_account(db_session):
    account = Account(name="Checking")
    db_session.add(account)
    db_session.commit()

    transaction = Transaction(
        account_id=account.id,
        amount=-50.0,
        description="Groceries",
        category="Food",
    )
    db_session.add(transaction)
    db_session.commit()

    assert transaction.account_id == account.id
    assert transaction.account == account
    assert account.transactions == [transaction]


def test_transaction_requires_account_id(db_session):
    transaction = Transaction(
        amount=-20.0,
        description="Coffee",
        category="Food",
    )
    db_session.add(transaction)

    with pytest.raises(IntegrityError):
        db_session.commit()
