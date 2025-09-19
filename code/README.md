
# Requisition System
This is my Requisition system project. This program makes requisitions and shows current requisition details; it gets info inputted by a user and then displays the statistics and info of the requisition. 

Program features:
This requisition program has 6 methods

Staff_info() - Gets staff info (ID, Date, Name) and stores them in an empty dictionary, also checks if nothing was input and display a message if so.

Requisition_details() – Gets price input by user and returns the added the total.

Requisition_approval() – Uses total from Requisition_details() and checks if it is under $500,
If it is the requisition will be approved, otherwise it will be pending until the requisition gets a response.

Respond_requisition() – If requisition status is pending this will display current details, then ask if you want to approve it or not and subtracts 1 from pending status counter.

Display_requisition() – Displays info of current requisition, shows error if any info is missing

Requisition_statistics() – Shows how many requisitions have been made and checks how many of them are still pending or have been approved or not approved.

Software design principles used:
KISS – used dictionary instead of three separate variables to store user information.

Clean code > clever code – everything is easy to read. Makes it easy to change problems if they occur.

YAGNI – in requisition_details() the item variable is not being used and could be removed.

Refactor, refactor, refactor – code can be improved by removing useless lines, fixing small mistakes and adding a menu method.

Single responsibility – each method does one function and only needs changes if there is a problem or if it could be improved,
DRY – Not much code is re-used in different methods.

Ways to improve Code:

The program could have used another method for a main menu that takes a user’s input to ask if they want to make another requisition, respond to a requisition and then ask if they want to display requisition after making one. So that we don’t have to make a new object each time we want a requisition.

Few mistakes in code:

The item variable in the Requisition details method could also be changed to just check if the user wants to end the loop as the items are never used or displayed in any of the methods.

Pending doesn’t subtract by 1 when requisition is approved or not, adds 1 to pending any time total is above 500, easily fixed by adding Global pending so that it can update the global variable.
