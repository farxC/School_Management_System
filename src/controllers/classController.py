from src.database.fetch import fetchData
from src.models.grade import ClassProtocol, Class

def createClass(obj: ClassProtocol):
    return Class(obj["name"], obj["id"], obj["year"])