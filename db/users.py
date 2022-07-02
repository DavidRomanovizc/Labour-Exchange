import datetime

import sqlalchemy as sql

from db.postgres import metadata

users = sql.Table(
    "user", metadata,
    sql.Column("id", sql.INTEGER, primary_key=True, autoincrement=True, unique=True),
    sql.Column("email", sql.String, primary_key=True, unique=True),
    sql.Column("name", sql.String),
    sql.Column("hashed_password", sql.String),
    sql.Column("is_company", sql.Boolean),
    sql.Column("created_at", sql.DateTime(timezone=True), default=datetime.datetime.utcnow),
    sql.Column("updated_at", sql.DateTime(timezone=True), default=datetime.datetime.utcnow)
)
