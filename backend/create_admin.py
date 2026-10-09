from app.database.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password

db = SessionLocal()

email = "admin@lamjingedutech.com"
password = "admin123"
full_name = "Lamjing Admin"


existing_user = db.query(User).filter(User.email == email).first()

if existing_user:
    print("Admin user already exists.")
else:
    admin = User(
        email=email,
        hashed_password=hash_password(password),
        full_name=full_name,
        role="admin",
        is_active=True,
    )

    db.add(admin)
    db.commit()

    print("Admin user created successfully.")


db.close()
