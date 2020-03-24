from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db
from lemonqa import app
from models import User,Question,Answer


manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command(db,MigrateCommand)

if __name__ =='__main__':

    app.run()




