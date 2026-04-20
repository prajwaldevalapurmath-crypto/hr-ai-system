from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:PMD@localhost:5432/hr_ai"

engine = create_engine(DATABASE_URL)