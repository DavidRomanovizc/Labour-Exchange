import datetime

import sqlalchemy as sql

from db.postgres import metadata

jobs = sql.Table(
    "jobs", metadata,
    sql.Column("id", sql.INTEGER, primary_key=True, autoincrement=True, unique=True),
    sql.Column("user_id", sql.INTEGER, sql.ForeignKey("user.id"), nullable=False),
    sql.Column("title", sql.String),
    sql.Column("description", sql.String),
    sql.Column("salary_from", sql.String),
    sql.Column("salary_to", sql.String),
    sql.Column("is_active", sql.Boolean),
    sql.Column("created_at", sql.DateTime, default=datetime.datetime.utcnow),
    sql.Column("updated_at", sql.DateTime, default=datetime.datetime.utcnow)
)
