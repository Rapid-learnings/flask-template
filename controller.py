from sqlalchemy import true

#from app.lib.rabbitmq.publisher import Publisher
from app.v1.project import project
from app.v1.project.models.project import Project
from flask import jsonify,request
from extensions import db
# from app.common.exceptions import resource_not_found

@project.post('/tablepost')
def post():
    # Publisher.add('test')
    # db.session.add(Project(name='apoorv'))
    # db.session.commit()
    db.session.add(Project(name='Virat',title='Kohali',review='Exellent',ranking='18'))
    db.session.commit()
    return {'data': 'post success'}


@project.post('/delete')
def delete():
    # db.session.query(Project).delete()
    # db.session.commit()
    record_obj = db.session.query(Project).filter(Project.id == 5).first()
    db.session.delete(record_obj)
    db.session.commit()
    return jsonify({'data': 'delete successful'})

@project.post("/update")
def update():
    change=Project.query.filter_by(id=6).first()
    change.name='kevin'

    db.session.commit()

    return jsonify({'data':'update succesfuly,'})


@project.get('/tableget')
def get():
    all_projects=[]
    projects=Project.query.all()
    for pro in projects:
        result={
            "pro_id": pro.id,
            "pro_name": pro.name,
            "pro_title": pro.title,
            "pro_review": pro.review,
            "pro_ranking":pro.ranking,
        }
        all_projects.append(result)

    return jsonify({"success":True,"projects":all_projects, "total_projects":len(projects),

    })


















