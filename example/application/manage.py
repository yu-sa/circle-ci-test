from flaskext.script import Server, Manager
from flasksample import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
