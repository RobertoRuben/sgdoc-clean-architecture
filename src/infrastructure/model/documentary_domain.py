from sqlmodel import Field, SQLModel, Column, BigInteger, Text, CheckConstraint

class DocumentaryDomain(SQLModel, table=True):
    __tablename__ = "documentary_domains"
    __table_args__ = (
        CheckConstraint("LENGTH(domain_name) >= 3", name="ck_domain_name_length")
    )
    id: int | None = Field(default=None, sa_column=Column(BigInteger, primary_key=True))
    domain_name: str = Field(sa_column=Column(Text, unique=True))