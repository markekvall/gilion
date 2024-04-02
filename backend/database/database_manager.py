from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from database.company_data_db_model import Base, CompanyDataDBModel
from models.company_data_dto import CompanyDataDTO

class DatabaseManager:

    def __init__(self, engine):
        self.engine = engine
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)


    def create(self, company_data_dto: CompanyDataDTO):
        try:
            company_data = CompanyDataDBModel.from_dto(company_data_dto)

            with self.Session() as session:
                session.add(company_data)
                session.commit()
        except SQLAlchemyError as e:
            if "UNIQUE constraint failed" in str(e):
                print("Error, database entry already exsists, use update endpoint instead")
            else:
                print(f"Error adding company data in database: {e}")


    def read_data_by_company_name(self, company_name: str) -> CompanyDataDTO:
        try:
            with self.Session() as session:
                company_db_model: CompanyDataDBModel = session.query(CompanyDataDBModel).filter(CompanyDataDBModel.company_name == company_name).first()
                return CompanyDataDTO.from_db_model(company_db_model)
        except SQLAlchemyError as e:
            print(f"Error retrieving data by company: {company_name}, error: {e}")


    #def delete_data_method
            
    #def update_data_method
