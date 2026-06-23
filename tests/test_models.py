from models import Account


def test_create_account(db_session):
    account = Account(name="Checking")
    db_session.add(account)
    db_session.commit()

    assert account.id is not None
    assert account.balance == 0.0
