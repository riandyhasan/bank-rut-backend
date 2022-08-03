import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://mtdciouacmckni:bc5a36a38fa66dadad7fa22313bca236754cbd8d065580e1153127cb7d0271db@ec2-54-208-104-27.compute-1.amazonaws.com/d1cjc3jptg3kd1"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()