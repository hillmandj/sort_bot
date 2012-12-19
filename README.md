sort_bot
========

***This is a program I wrote to help me organize incident reports at work!***

At MedTech Risk Management, we monitor and database incidents at nursing homes all over the 
country, to track their severity and to assist if any incidents go to court. Each day, we 
receive hundreds of incidents from the facilities we monitor. In order for us to easily address
each incident, at the end of the month someone at MedTech has to contact each facility and ask
about what occurred. In order to make this easier on the person investigating, someone has
to print out all of the incident reports sent to us via email from the facilities, number the 
incident with the facility ID, and then sort all of the incidents by facility ID and Date of 
Incident.

This is a program I wrote that will parse the incident file (which is a text file downloaded
from our email client containing all of the incident emails) and places the number code for
the facility on top of each incident. It then sorts all incidents, and writes it to a blank
text file.

I've added a (fake) facility_file and incident_file in order for you to see how this works. I had 
to do this because  the real names of MedTech facilities and incidents are private and 
confidential. I've also included a write_here file, which is simply a blank text file for you to 
write to.

This program is meant to be run in Python 3.3 and does not work in previous versions of Python.

To run the program:

1. Run the script in the python shell
2. Select a facility file
3. Select an incident file
4. Select a text file to write to
5. Program completes, you can view the results in the text file you selected for writing

Thanks for checking out my program!

-d
