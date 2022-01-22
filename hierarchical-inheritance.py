class Details:
    def__init__(self):
    self._id="<no_id>"
    self._name="<no_name>"
    self._gender="<no_gender>"
    def setData(self,id,name,gender):
        self._id=id
        self._name=name
        self._gender=gender
    def showData(self):
        print("ID:",self._id)
        print("name:",self._name)
        print("gender:",self._gender)
class Employee(Details):
    def__init__(self):
    self.company="<no_company>"
    self.department="<no_department"
    def setEmployee(self,id,name,gender,company,department):
        self.company=company
        self.department=department
    def showEmployee(self):



