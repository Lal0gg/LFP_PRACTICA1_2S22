class Curso:
    def __init__(self,idCourse,NameCourse,PreRequisite,Optionality,Semester,Credits,Status):
        self.idCourse = idCourse
        self.NameCourse = NameCourse
        self.PreRequisite = PreRequisite
        self.Optionality = Optionality
        self.Semester = Semester
        self.Credits = Credits
        self.Status = Status
        self.Counter=0
    
    def __repr__(self):
        return str(self.__dict__)

    def getidCourse(self):
        return self.idCourse
    def setidCourse(self,idCourse):
        self.idCourse=idCourse

    def getNameCourse(self):
        return self.NameCourse
    def setNameCourse(self,NameCourse):
        self.NameCourse=NameCourse
    
    def getPreRequisite(self):
        return self.PreRequisite
    def setPreRequisite(self,PreRequisite):
        self.PreRequisite=PreRequisite
    
    def getOptionality(self):
        return self.Optionality
    def setOptionality(self,Optionality):
        self.Optionality=Optionality
    
    def getSemester(self):
        return self.Semester
    def setSemester(self,Semester):
        self.Semester=Semester
    
    def getCredits(self):
        return self.Credits
    def setCredits(self,Credits):
        self.Credits=Credits

    def getStatus(self):
        return self.Status
    def setStatus(self,Status):
        self.Status=Status

