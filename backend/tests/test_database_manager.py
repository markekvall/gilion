from datetime import datetime
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.company_data_db_model import Base, CompanyDataDBModel
from database.database_manager import DatabaseManager
from models.company_data_dto import CompanyDataDTO


class TestDatabaseManager(TestCase):

    def setUp(self):

        self.test_engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.test_engine)
        self.test_session = sessionmaker(bind=self.test_engine)()
        self.db_manager = DatabaseManager(self.test_engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.test_engine)
        self.test_session.close()

    def test_create(self):
        
        self.db_manager.create(CompanyDataDTO(company_name="123"))
        created_data = self.test_session.query(CompanyDataDBModel).first()
        self.assertIsNotNone(created_data)
        self.assertEqual(created_data.company_name, "123")
