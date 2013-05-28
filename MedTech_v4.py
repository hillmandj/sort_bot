from tkinter.filedialog import askopenfile
from datetime import datetime
import re
import os
import cgi


def get_facilities(facility_file):
    '''(file open for reading) -> dict

    Return a dictionary from data in facility_file where the keys are
    equal to the facility_names and the values are equal to the facility_ids
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

 
def populate_incident_list(incident_file):
    '''(file open for reading) -> list

    Return a list from incident_file with all of the incidents in file
    as an item in the list.

    Precondition: incident_file is a text file downloaded from MedTech's email
    client and is formatted such that each incident report is found between
    two lines. These lines are 39 repetitions of the pattern '=-' followed by
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

    return datetime.strptime(incident_date, '%m/%d/%Y').strftime('%m/%d/%Y')


def find_date_submitted(incident):
    '''(str) -> str

    Return a string containing the date submitted of a particular
    incident.

    Precondition: The string contains a Date Submitted line where the date 
    can be found.

    '''

    pattern = re.compile(r'Date:(.+?),\s(.+?)\n')
    findPat3 = re.search(pattern, incident)
    incident_date = findPat3.group(2)

    return datetime.strptime(incident_date, '%B %d, %Y, %I:%M:%S %p').strftime('%m/%d/%Y %I:%M:%S %p')


def find_DS_forSort(incident):
    '''(str) -> datetime object

    Return a datetime object containing the date submitted of a particular
    incident. This function is identical to find_date_submitted, except it does not
    convert the final result into a string. This is to eliminate errors when sorting the final_list.

    Precondition: The string contains a Date Submitted line where the date 
    can be found.

    '''

    pattern = re.compile(r'Date:(.+?),\s(.+?)\n')
    findPat3 = re.search(pattern, incident)
    incident_date = findPat3.group(2)

    return datetime.strptime(incident_date, '%B %d, %Y, %I:%M:%S %p')


def boolComments(incident):
    '''
    (str) -> BOOL

    Return a BOOL that indicates if there are MedTech comments in a particular incident.

    Precondition: The strings with comments contain a "MedTech Comments:" line where the comments
    can be found.

    '''

    Comment = None
    pattern = re.compile(r'MedTech Comments:')
    findPat4 = re.search(pattern, incident)
    if findPat4 == None:
        Comment = False
    else:
        med_com = findPat4.group()
        Comment = True

    return Comment


def renamePath(file_obj):
    '''(closed_file.txt) -> (closed_file.html)

    This function changes the file extension from txt to html.

    '''
    
    filename = str(file_obj.name)
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + '.html')


def Run():
    m = input('Please select a month, format mm: ')
    y = input('Please select a year, format yyyy: ')
    comment_option = input('Would you like MedTech Comment emails to be included? Y/N: ')
    yes_var = ['Yes', 'YES', 'y', 'Y']
    no_var = ['No', 'NO', 'n', 'N']

    facility_file = open('facilityList.txt', 'r')
    incident_file = askopenfile(mode='r', title='Please select an incident file!')
    d = get_facilities(facility_file)
    incident_list = populate_incident_list(incident_file)
    
    mincident_list = list(filter(lambda x: find_date_submitted(x)[0:2] == m, incident_list))  

    myincident_list = list(filter(lambda x: find_date_submitted(x)[6:10] == y, mincident_list))

    if comment_option in yes_var:
        final_list = [('\t' * 15) + d[find_facility_name(incident)] + '\n' + incident for incident in myincident_list]

    if comment_option in no_var:
        final_list = [('\t' * 15) + d[find_facility_name(incident)] + '\n' + incident for incident in myincident_list if boolComments(incident) == False]
        
    final_list.sort(key=lambda i: (i[15:18], find_DS_forSort(i)))

    date_of_incident_before_m = []

    for alert in final_list:
        if find_date_of_incident(alert)[0:2] != m:
            date_of_incident_before_m.append(alert)

    new_final_list = list(filter(lambda alert: find_date_of_incident(alert)[0:2] == m, final_list)) 
    
    final_file = askopenfile(mode='w', title='Please select a text file to write this month\'s DOIs\'s to!')
    prior_file = askopenfile(mode='w', title='Please select a text file to write prior month\'s DOIs\'s to!')

    html_styling = ('<html>' + '<head>' + '<style>' + 'hr { page-break-before: always;}' + '''pre {
    white-space: pre-wrap; white-space: -moz-pre-wrap; white-space: -pre-wrap; white-space: -o-pre-wrap;
    word-wrap: break-word;}''' + '</style>' + '</head>' + '<body>')
    
    final_file.write(html_styling)

    for alert in new_final_list:
        final_file.write('<pre>' + '<font size= "4" face= "Ariel">' +
                         cgi.escape(alert) + '</font>' + '</pre>' + '<hr>')    

    final_file.write('</body>' + '</html>')

    final_file.close()

    prior_file.write(html_styling)

    for alert in date_of_incident_before_m:
        prior_file.write('<pre>' + '<font size= "4" face= "Ariel">' +
                         cgi.escape(alert) + '</font>' + '</pre>' + '<hr>')

    prior_file.write('</body>' + '</html>')

    prior_file.close()

    renamePath(final_file)

    renamePath (prior_file)

    print('Sorting complete! Please open html files to see results.')

Run()

                 
