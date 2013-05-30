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

1. Create two blank text files to write to (one for incidents that happened this month, the other for incidents that occured in prior months)
2. Run the program in the Python Shell
3. Input what month the incident emails you're interested in sorting was received
4. Input the year the incident emails you're interested in sorting was received
5. Select a text files you created earlier in order to write to them when prompted
6. Program completes, you can view the results by double clicking the html files that are automatically created. These files were originally the blank text files you created.

Ways I intend to make this program better in upcoming versions:
- Automatically generate output files
- Implement exception handling

Thanks for checking out my program!

-d
