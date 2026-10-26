from app.database.database import engine

from app.models.user import Base
from app.models.user import User
from app.models.scan import Scan


Base.metadata.create_all(bind=engine)

print("Tables created successfully")
