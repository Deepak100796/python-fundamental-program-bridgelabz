import json
"""
    @date   : 2/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @class find
class Find:

     # @find by id
    def doctorFindById(self, id, hospital_doc):
        for iD in hospital_doc['doctor']:
            if id == iD['Id']:
                return True
        return False

    # find by name
    def doctorFindByName(self, name, hospital_doc):
        for findName in hospital_doc['doctor']:
            if name == findName['name']:
                return name
        return False

    # find id
    def patientFinfById(self, id, hospital_doc):
        for iD in hospital_doc['patient']:
            if id == iD['Id']:
                return True
        return False

    # @find name
    def patientFindByName(self, name, hospital_doc):
        for findName in hospital_doc['patient']:
            if name == findName['name']:
                return True
        return False

    # find by mobile number
    def patientFindByMobile(self, mobile, hospital_doc):
        for mNo in hospital_doc['patient']:
            if mobile == mNo['mobile']:
                return True
        return False

    # @find appointment
    def appoinment(self, date_input, id, hospital_doc):
        for i in hospital_doc['doctor']:
            if i['Id'] == id and i['pCount'] < 5:
                print("Appointment Scheduled on " + date_input + " " + " with Doctor Id  " + id)


# @creating object
find = Find()