from models.project import Project
from services.mongoService import MongoService

def mapping_projects(x):
    return Project(id=x["_id"], name=x["name"], tag=x["tag"])

class ProjectController:
    @staticmethod
    def get_projects():
        return list(map(mapping_projects, MongoService.get_all_from_collection("projects")))
    
