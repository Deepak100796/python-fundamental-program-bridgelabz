"""
This programme is used to manage a list of
Doctors associated with the Clinique. This also manages the list of patients who use the
clinique. It manages Doctors by Name, Id, Specialization and Availability (AM, PM or
both). It manages Patients by Name, ID, Mobile Number and Age. The Program allows
users to search Doctor by name, id, Specialization or Availability. Also the programs
allows users to search patient by name, mobile number or id. The programs allows
patients to take appointment with the doctor. A doctor at any availability time can see
only 5 patients. If exceeded the user can take appointment for patient at different date or
availability time. Print the Doctor Patient Report. Also show which Specialization is
popular in the Clinique as well as which Doctor is popular
"""

"""
    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @import statement

# import json
# from oops.clinic_management_system.doctor import doctor
from oops.cleanic_management_system.doctorFile import doctor
from oops.cleanic_management_system.patientFile import patient
from oops.cleanic_management_system.search import find

# creating global dict
hospital_doc = dict()
# hospital_pet = dict()

print(""" ------------------------------------------------------
        |======================================================| 
        |======== Welcome To Cleanic Management System	=======|
        |======================================================|

      ------------------------------------------------------ """)

c = 2
while c > 1:
    # choice input

    print("1.Add Doctor")
    print("2.Add Patients")
    print("3.Print Doctor")
    print("4.Print Patients")
    print("5.Take Appointment")
    print("6.Print Appointment")
    print("7.Search Doctor by Name ,Id or Availability")
    print("8.Search Patients by Name ,Id or Mobile Number")
    print("9.Exit")

    choice = input("Enter your choice: ")

    # @add doctor
    if choice == '1':
        doctor.addDoctor()
        if "doctor" not in hospital_doc.keys():
            hospital_doc["doctor"] = list()
        hospital_doc["doctor"].append(doctor.toString())
        #     # doctorList.append()
        print(hospital_doc, ">>>>>>>>>>>")


    # @add patient
    elif choice == '2':
        patient.addPatient()
        if "patient" not in hospital_doc.keys():
            hospital_doc["patient"] = list()
        hospital_doc["patient"].append(patient.toString())

        print(hospital_doc, "------------->")

    # @print doctor
    elif choice == '3':
        for name in hospital_doc['doctor']:
            print(name['name'])

    # @ print patient
    elif choice == '4':
        for name in hospital_doc['patient']:
            print(name['name'])

    # search id
    elif choice == '5':
        id = input("Enter doctor ID: ")
        if find.doctorFindById(id, hospital_doc):
            date_input = input("Enter Date of Appointment(eg.10/06/2016): ")
            t = 0
            while t < 3:
                print("test")
                if date_input is None:
                    print("date format is wrong")
                else:
                    find.appoinment(date_input, id, hospital_doc)
                    for i in hospital_doc['doctor']:
                        i['pCount'] += 1
                    print(hospital_doc['doctor'])
                    break
                t += 1


    # take appointment
    elif choice == '6':
        print("print Appointment")
        pass

    # @search operation
    elif choice == '7':
        id = input("Enter id for doctor search: ")
        print(find.doctorFindById(id, hospital_doc))

        name = input("Enter doctor name for search: ")
        print(find.doctorFindByName(name, hospital_doc))

    # @search patient
    elif choice == '8':
        id = input("Enter Patient id for search: ")
        print(find.patientFinfById(id, hospital_doc))

        name = input("Enter patient name for search: ")
        print(find.patientFindByName(name, hospital_doc))

        mobile = input("Enter mobile no for search: ")
