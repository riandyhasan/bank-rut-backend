import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://bdrmlwopzvjmbg:3776ab40ba8773df86013ecbf416c7eeceaa1a9a666b1cffb3a06b66fc6782aa@ec2-44-207-126-176.compute-1.amazonaws.com/ddme0h1esrkgpq"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()