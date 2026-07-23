from app.database import SessionLocal, engine, Base
from app.models import User, Branch, Stock
from app.security.password import hash_password


# Création des tables si elles n'existent pas
Base.metadata.create_all(bind=engine)


db = SessionLocal()


def seed():

    # Vérifier si la base contient déjà des données
    existing_user = db.query(User).first()

    if existing_user:
        print("Database already initialized")
        return


    # --------------------
    # Branches
    # --------------------

    branch1 = Branch(
        name="Brussels",
        address="Brussels Center"
    )

    branch2 = Branch(
        name="Paris",
        address="Paris Center"
    )


    db.add(branch1)
    db.add(branch2)

    db.commit()

    db.refresh(branch1)
    db.refresh(branch2)


    # --------------------
    # Admin
    # --------------------

    admin = User(
        username="admin",
        password_hash=hash_password("admin123"),
        role="ADMIN",
        branch_id=None
    )


    # --------------------
    # Common users
    # --------------------

    user1 = User(
        username="alice",
        password_hash=hash_password("alice123"),
        role="USER",
        branch_id=branch1.id
    )


    user2 = User(
        username="bob",
        password_hash=hash_password("bob123"),
        role="USER",
        branch_id=branch2.id
    )


    db.add(admin)
    db.add(user1)
    db.add(user2)

    db.commit()


    # --------------------
    # Stock
    # --------------------

    stocks = [

        Stock(
            branch_id=branch1.id,
            product_id="P001",
            quantity=20
        ),

        Stock(
            branch_id=branch1.id,
            product_id="P002",
            quantity=10
        ),

        Stock(
            branch_id=branch2.id,
            product_id="P001",
            quantity=5
        ),

        Stock(
            branch_id=branch2.id,
            product_id="P003",
            quantity=15
        )
    ]


    db.add_all(stocks)

    db.commit()


    print("Database seeded successfully")


if __name__ == "__main__":
    seed()
