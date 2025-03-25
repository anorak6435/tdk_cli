from models.project import Project
from controllers.projectController import ProjectController

class ProjectView:
    @staticmethod
    def showProjects():
        projects = ProjectController.get_projects()
        for project in projects:
            print(project.name)