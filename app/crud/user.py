from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.user import User
from app.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password_plain: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not pwd_context.verify(password_plain, user.password_hash):
        return None
    return user
