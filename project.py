from app.common.database import Column, db, BaseModel


class Project(BaseModel):
    __tablename__='projects'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    title = Column(db.String)
    review = Column(db.String)
    ranking = Column(db.Integer)


