 #!/usr/bin/env python
import os
import logging

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from flask_migrate import Migrate, MigrateCommand

from sqlalchemy.engine import reflection
from sqlalchemy import create_engine
from sqlalchemy.schema import (
    MetaData,
    Table,
    DropTable,
    ForeignKeyConstraint,
    DropConstraint,
    )

from mathsonmars import create_app
from mathsonmars.models import User, db
from setuptables import setup_strategies, setup_topics_and_categories,\
    setup_users, setup_level_1_add_sub, setup_level_2_add_sub, \
    setup_level_3_add_sub, setup_level_2_mult, setup_level_3_mult, \
    setup_level_4_mult, create_name_pass_for_user, drop_user_by_username,\
    drop_student_by_user_id, dummy_create_user
    
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# default to prod config 
env = os.environ.get('MARS_ENV', 'prod')
app_name = 'mathsonmars.settings.%sConfig' % env.capitalize()
logger.debug("manage.py starting app_name:{0}".format(app_name))

app = create_app(app_name)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command('db', MigrateCommand)


    
'''
@manager.command
def setup_db_drop_given(table_drop_list):
    
'''

@manager.command
def modify_only():
    drop_student_by_user_id(db, 4)
    drop_user_by_username(db, 'sm0324')
    #dev db only
    #dummy_create_user(db, 'Steve@mcquillans.com')
    create_name_pass_for_user(db, 'Steve@mcquillans.com', 'dolphin2', '2031hpx')
    
@manager.command
def populate_level_tables():
    setup_topics_and_categories(db)
    setup_strategies(db)
    setup_level_1_add_sub(db);
    setup_level_2_add_sub(db);
    setup_level_2_mult(db);
    setup_level_3_add_sub(db);
    setup_level_3_mult(db);
    setup_level_4_mult(db);
    db.session.commit()
    
def populate_all_tables():
    logger.debug(">>populate_all_tables()")
    setup_topics_and_categories(db)
    setup_strategies(db)
    setup_level_1_add_sub(db);
    setup_level_2_add_sub(db);
    setup_level_2_mult(db);
    setup_level_3_add_sub(db);
    setup_level_3_mult(db);
    setup_level_4_mult(db);
    setup_users(db)
    #setup_test_users(db)
    db.session.commit()

def drop_tables_in_list(table_names_to_drop):
    #@praram table_names_to_drop: [str]
    #eg [funchunks','friendlyandfix','memorize','boxmodelmads','boxmethod','numberbonds','topic','category','strategy','activity']
    conn=db.engine.connect()
    # the transaction only applies if the DB supports
    # transactional DDL, i.e. Postgresql, MS SQL Server
    trans = conn.begin()
    inspector = reflection.Inspector.from_engine(db.engine)

    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in 
    # a transaction.
    metadata = MetaData()
    tbs = []
    all_fks = []
    for table_name in table_names_to_drop:
        fks = []
        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(
                ForeignKeyConstraint((),(),name=fk['name'])
                )
        t = Table(table_name,metadata,*fks)
        tbs.append(t)
        all_fks.extend(fks)
    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))
    for table in tbs:
        conn.execute(DropTable(table))
    trans.commit() 
    
@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """
    return dict(app=app, db=db, User=User)

@manager.command
def create_tables():
    "Create relational database tables."
    "Conditional by default, will not attempt to recreate tables already present in the target database."
    db.create_all()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()
    
@manager.command
def setup_db():
    logger.debug(">>setup_db")
    db_dropEverything()
    db.drop_all()
    db.create_all()
    db.session.commit()
    populate_all_tables();
   
@manager.command
def db_dropEverything():
    # From http://www.mbeckler.org/blog/?p=218 and http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything
    conn=db.engine.connect()
    # the transaction only applies if the DB supports
    # transactional DDL, i.e. Postgresql, MS SQL Server
    trans = conn.begin()
    inspector = reflection.Inspector.from_engine(db.engine)
    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in 
    # a transaction.
    metadata = MetaData()
    tbs = []
    all_fks = []
    for table_name in inspector.get_table_names():
        fks = []
        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(
                ForeignKeyConstraint((),(),name=fk['name'])
                )
        t = Table(table_name,metadata,*fks)
        tbs.append(t)
        all_fks.extend(fks)
    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))
    for table in tbs:
        conn.execute(DropTable(table))
    trans.commit()
    
@manager.command
def db_drop_activities():
    tables_to_repopulate = ['funchunks','friendlyandfix','memorize','boxmodelmads','boxmethod','numberbonds','topic','category','strategy','activity']
    drop_tables_in_list(tables_to_repopulate)
    

    
'''
@manager.command
def populate_activity_tables():
    #[funchunks','friendlyandfix','memorize','boxmodelmads','boxmethod','numberbonds','activity']
    logger.debug(">>populate_activity_tables()")
    setup_topics_and_categories(db)
    setup_strategies(db)
    persist_numberbond_addition_activities(db)
    persist_fun_chunk_addition_activities(db)
    persist_fun_chunk_subtraction_activities(db)
    persist_friendly_and_fix_addition_activities(db)
    persist_friendly_and_fix_subtraction_activities(db)
    persist_multiplication_tables(db)
    setup_box_model_addition(db)
    setup_box_model_multiplication(db)
    logger.debug("<<populate_activity_tables()")
'''
    
'''
def drop_non_user_related():
    tableName.__table__.drop(self._engine)
    
def create_non_user_related():
    tableName.__table__.drop(self._engine)
'''
      

if __name__ == "__main__":
    manager.run()
