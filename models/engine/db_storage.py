#!/usr/bin/python3
"""New engine DBStorage: (models/engine/db_storage.py)"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Init constructor method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os.environ['HBNB_MYSQL_USER'],
                                              os.environ['HBNB_MYSQL_PWD'],
                                              os.environ['HBNB_MYSQL_HOST'],
                                              os.environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)
        self.__metadata = MetaData()
        self.__metadata.reflect(bind=self.__engine)
        if os.environ['HBNB_ENV'] == 'test':
            for table in reversed(self.__metadata.sorted_tables):
                table.drop(self.__engine)

    def all(self, cls=None):
        """all objects depending of the class name"""
        return_dict = {}
        if cls is None:
            db_items = self.__metadata.tables.items()
            for table_name, table in db_items:
                query = self.__session.query(table)
                class_name = table.mapped_class.__name__
                for row in query:
                    return_dict[f'{class_name}.{row.id}'] = dict(row.__dict__)
                print(return_dict)
            return return_dict

    def save(self):
        """save(self): commit all changes of the
        current database session (self.__session)"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current
        database session (self.__session)"""
        self.__session.add(obj)
        self.save()

    def delete(self, obj=None):
        """delete(self, obj=None): delete from
        the current database session obj if not None"""
        if obj is not None:
            self.__session(obj)
            self.save()

    def reload(self):
        """create all tables in the database
        (feature of SQLAlchemy) (WARNING: all
        classes wwho inherit from Base must be
        imported before calling """
        from models.base_model import Base
        from models.amenity import Amenity
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
