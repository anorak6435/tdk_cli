from views.projectView import ProjectView
from enum import Enum, auto

class Screen(Enum):
    Projects = auto()


def main():
    print("tea Data Kettle")
    ProjectView.showProjects()

if __name__ == "__main__":
    main()