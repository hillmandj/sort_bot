sort_bot
========

***This is a program I wrote to help me organize incident reports at work!***

At MedTech Risk Management, we monitor and database incidents at nursing homes all over the 
country, to track their severity and to assist if any incidents go to court. Each day, we 
receive hundreds of incidents from the facilities we monitor. In order for us to easily address
each incident, at the end of the month someone at MedTech has to contact each facility and ask
about what occurred. In order to make this easier on the person investigating, someone has
to print out all of the incident reports sent to us via email from the facilities, number the 
incident with the facility ID, and then sort all of the incidents by facility ID and then by the date/time the email was received.

This is a program I wrote that will parse the incident file (which is a text file downloaded
from our email client containing all of the incident emails) and places the number code for
the facility on top of each incident. It then writes all incidents where the Date of Incident is in the current month to one text file, and all incidents from prior months to another text file (if there are no incidents from previous months, the final output for this file will be blank). This makes it easier for the people at MedTech to investigate each incident.

I've added a (fake) facility_file and incident_file in order for you to see how this works. I had 
to do this because  the real names of MedTech facilities and incidents are private and 
confidential.

This program is meant to be run in Python 3.3 and does not work in previous versions of Python.

To run the program:

1. Run the program in the Python Shell
2. Input what month the incident emails you're interested in sorting were received
3. Input the year the incident emails you're interested in sorting were received
4. Choose a name for the file that will contain this month's sorted alerts.
5. Choose a name for the file that will contain prior month's sorted alerts.
6. Program completes, you can view the results by double clicking the html files that are automatically created.
7. If the program encounters an email where the name of the facility is spelled slightly differently, or if there is a new facility, the user will be alerted to add that to the facility file. The exact spelling of the name as it appears in the email will be provided.

IMPORTANT NOTE: The default/initial directory in the calls to asksaveasfile are currently the path to the Desktop for MedTech's designated sort_bot computer. These values must be changed if you are going to run the script on your own computer.

Ways I intend to improve this program:

-Add a way to merge previous outputs of sort_bot to generate one large file. This is important because this program was originally designed to be executed monthly, after we received all the alerts for the month. However, since we are able to process alerts faster using sort_bot, we now process alerts weekly or even less. This means that occasionally, someone has to hand-sort previous outputs of sort_bot with newer ones. Though this is much easier to do, since both outputs are already sorted by facility ID and date received, it would be much better to be able to select a number of files, extract content, and re-sort. 

-Update exception handling to automatically add new facility name values to the facility file if encountered. The only required input from the user following this would be the Facility ID number associated with that facility name.

Thanks for checking out my program!

-d
