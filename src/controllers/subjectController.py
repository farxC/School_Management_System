from src.models.subject import Subject , SubjectProtocol

def createSubject(obj: SubjectProtocol) -> Subject:
    return Subject(**obj)