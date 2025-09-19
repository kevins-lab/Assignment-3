'''
requisiton system code from Part A updated to use Classes
'''
counter = 1
id_counter = 1
approved = 0
not_approved = 0
pending = 0
class RequisitonSystems():

    def __init__(self):
        # keeps requisition id at 10000 and info empty each time object is made
        self.requisition_id = 10000 
        self.info = {}
    
    # method that gets the date, staff id and name; adds them to dictionary(info)
    def staff_info(self):
        global id_counter
        while True:
            self.info['date'] = input("enter the date: ")
            self.info['staff id'] = input("enter ID: ").upper()
            self.info['name'] = input('enter name: ').title()
            if self.info['date'] == "" or self.info['name'] == "" or self.info['staff id'] == "": # if nothing is input gives message then tries again
                print("nothing entered")
                continue
            else:
                break
        self.requisition_id += id_counter #adds from global variable
        id_counter += 1 
    
    # method to get total
    def requisitions_details(self):
        sum = 0
        while True:
            #YAGNI - "item" not being used, so it can be removed
            item = input('enter name of requisiton item type, "end" if done: ')
            if item.lower() == 'end':
                break
            else:
                try: # checks if number is input gives error message if not and restarts
                    price = float(input('enter price of item: '))
                    sum += price
                except:
                    print("invalid input please enter float value")
                    continue
            self.total = sum
    
    # method to approve requisiton, if total < 500 it approves, pending if total > 500
    def requisition_approval(self):
        global approved 
        global pending
        try:
            if self.total < 500:
                self.status = "approved"
                approved += 1 # adds to approved counter if it was approved
                self.approval_reference_number = self.info['staff id'] + str(self.requisition_id)[:2]
                print(f"{self.approval_reference_number} and {self.status}")
            else:
                self.status = 'pending'
                pending += 1 # adds to pending counter if not
                self.approval_reference_number = "Not Available" # if no response to requisition
        except:
            print("missing info") # if no total gives error message
    
    # method to respond to pending requisitions
    # refactor,refactor, refactor - pending not -1 when approved or not
    def respond_requsition(self):
        global not_approved
        global approved
        while True:
            try: 
                if self.status == "pending": # prints info of pending requisition
                    print(f'date requested: {self.info['date']}')
                    print(f'staff ID: {self.info['staff id']}')
                    print(f'name: {self.info['name']}')
                    print(f'requisition ID: {self.requisition_id}')
                    print(f'total: ${self.total}')
                    print(f'Status: {self.status}')
                    print(f'Reference number: {self.approval_reference_number}')
                    user_input = input("would you like to approve this request? 'y' if yes 'n' if no: ")
                    if user_input.lower() == 'n':
                        self.status = "not approved"
                        not_approved += 1
                        pending -= 1
                        break
                    elif user_input.lower() == 'y':
                        self.status = "approved"
                        approved += 1
                        pending -= 1
                        break
                else:
                    print("request is approved")
                    break
            except:
                print("missing info")
                break
    
    # method to display all the details
    def display_requisition(self):
        try: 
            print(f'Displaying Requisitions....')
            print(f'date requested: {self.info['date']}')
            print(f'staff ID: {self.info['staff id']}')
            print(f'name: {self.info['name']}')
            print(f'requisition ID: {self.requisition_id}')
            print(f'total: ${self.total}')
            print(f'Status: {self.status}')
            print(f'Reference number: {self.approval_reference_number}\n')
        except:
            print("missing info")
    
    # method to display how statistics of requisitions made
    def requisition_statistics(self):
        global counter
        print("Requisition Statistics:")
        print(f"Requisitons made: {counter}")
        print(f"Approved requisitions: {approved}")
        print(f"Pending requisitions: {pending}")
        print(f"Not approved requisitions: {not_approved}\n")
        counter += 1 #everytime obj is made adds to counter to use for printing how many Requisitions made 

req1 = RequisitonSystems() #test1
req1.staff_info()
req1.requisitions_details()
req1.requisition_approval()
req1.respond_requsition()
req1.display_requisition()
req1.requisition_statistics()

req2 = RequisitonSystems() #test2
req2.staff_info()
req2.requisitions_details()
req2.requisition_approval()
req2.display_requisition()
req2.requisition_statistics()

req3 = RequisitonSystems() #test3
req3.staff_info()
req3.requisitions_details()
req3.requisition_approval()
req3.respond_requsition()
req3.display_requisition()
req3.requisition_statistics()

req4 = RequisitonSystems() #test4
req4.staff_info()
req4.requisitions_details()
req4.requisition_approval()
req4.respond_requsition()
req4.display_requisition()
req4.requisition_statistics()

req5 = RequisitonSystems() #test5
req5.staff_info()
req5.requisitions_details()
req5.requisition_approval()
req5.respond_requsition()
req5.display_requisition()
req5.requisition_statistics()