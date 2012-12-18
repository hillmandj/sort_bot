from tkinter.filedialog import askopenfile
import re

#The purpose of this program is to take a large number of incident reports in
#a text file and write them to a different text file, sorting them by the
#facility id, and date of incident. The program will also write the facility id
#on top of each report in the new text file.

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#MedTech services a large number of facilities, so the first step is to get all
#facilities, and their IDs, into a dictionary -- so that we can access them
#easily later. This can be done by organizing them in a specfic way in a text
#file and reading that file using this function (see precondition in the
#function for information on formatting).


def get_facilities(facility_file):
    '''(file open for reading) -> dict

    Return a dictionary from data in facility_file where the keys are
    equal to the facility_ids and the values are equal to the facility_names
    in the file. 

    Precondition: facility_file is a text file that is formatted such that
    each line is comprised of a 3 digit facility id, followed by one or more
    spaces, followed by the facility name.

    '''

    facility_dict = {}
    line = facility_file.readline()
    while line != '':
        facility_ids = line[0:3].strip()
        facility_names = line[3:].strip()
        facility_dict[facility_names] = facility_ids
        line = facility_file.readline()

    return facility_dict

 
#The next step is to put all of the incidents that occurred during into a list.
#That way we can access one incident at a time, and check for data within each
#one.

#Incident reports come to MedTech via email -- all of these emails can be
#downloaded into one text file from the email client. These emails follow a VERY
#specific format (see precondition in populate_incident_list function).

def populate_incident_list(incident_file):
    '''(file open for reading) -> list

    Return a list from incident_file with all of the incidents in file
    as an item in the list.

    Precondition: incident_file is a text file downloaded from MedTech's email
    client and is formatted such that each incident report is found between
    two lines. These lines are 39 repititions of the pattern '=-' followed by
    one last '=' at the end.
    
    '''
    master_list = []
    incident_str = incident_file.read()
    for incident in incident_str.split((('=-') * 39 + '=')):
        incident.strip()
        if len(incident) > 0:
            master_list.append(incident)
    for i in master_list:
        if i == '\n\n':
            master_list.remove(i)
        if i == '\n':
            master_list.remove(i)

    return master_list


#The next step is to create a function that will allow us to extract the
#facility name for each item in the list. Regular expressions can help us
#capture this piece of information.

def find_facility_name(incident):
    '''(str) -> str

    Return a string containing the facility name for a particular incident.

    Precondition: The string contains a Subject line where the facility name
    can be found.
    '''

    pattern = re.compile(r'Subject:.*?for\s(.+?)\n')
    findPat1 = re.search(pattern, incident)
    facility_name = findPat1.group(1)

    return facility_name


#The next step is to create a function that will allow us to extract the
#date of the incident for each item in the list. We can use Regular expressions
#to do this.

def find_date_of_incident(incident):
    '''(str) -> str

    Return a string containing the date the incident occurred from a particular
    incident.

    Precondition: The string contains a Date of Incident line where the date of
    the incident can be found.

    '''

    pattern = re.compile(r'Date of Incident:\s(.+?)\n')
    findPat2 = re.search(pattern, incident)
    incident_date = findPat2.group(1)

    return incident_date

#Now we have define our functions, we can  get the program started. The user
#has to select the text file with all of the facilities and the text file
#with all of the incident emails.

facility_file = askopenfile(mode='r', title='Please select a facility file!')
incident_file = askopenfile(mode='r', title='Please select an incident file!')
d = get_facilities(facility_file)
incident_list = populate_incident_list(incident_file)

#The next step is to find a way to easily sort the list by facility name and
#date of incident. List comprehensions can be very useful in making this happen.

final_list = [d[find_facility_name(incident)] + incident for incident in incident_list]

final_list.sort(key=lambda i: (i[0:3], find_date_of_incident(i)))

#Now we prompt the user for a text file to write to...

final_file = askopenfile(mode='w', title='Please select a text file to write to!')

for alert in final_list:
    final_file.write(alert + '\n')

final_file.close()

#DONE!!!!!! Open the text file to see the results! :)
                 
