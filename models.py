import sqlalchemy as _sql
import database as _database

class Users(_database.Base):
    __tablename__ = "users"
    user_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    full_name = _sql.Column(_sql.String, index=True)
    username = _sql.Column(_sql.String, index=True, unique=True)
    password = _sql.Column(_sql.String, index=True)
    ktp = _sql.Column(_sql.String)
    balance = _sql.Column(_sql.Integer, default=0, index=True)
    status = _sql.Column(_sql.Integer, default=0, index=True)
    role = _sql.Column(_sql.Integer, default=0)

class Requests(_database.Base):
    __tablename__ = "requests"
    request_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey('users.user_id'), index=True)
    nominal = _sql.Column(_sql.Integer, index=True)
    jenis = _sql.Column(_sql.Integer, index=True)
    status = _sql.Column(_sql.Integer, index=True)

class Transactions(_database.Base):
    __tablename__ = "transactions"
    transaction_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    sender_id = _sql.Column(_sql.Integer, _sql.ForeignKey('users.user_id'), index=True)
    receiver_id = _sql.Column(_sql.Integer, _sql.ForeignKey('users.user_id'), index=True)
    nominal = _sql.Column(_sql.Integer, index=True)