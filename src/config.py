
class Config:
    SECRET_KEY = '229e422d0579f4672f670372b03845a3'
    # tworzymy lokalizację bazy danych, odnośnik do bazy
    # trzy /// to znaczy, że baza będzie w tym samym folderze
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'