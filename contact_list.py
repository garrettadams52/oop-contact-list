class ContactList():
    def __init__(self, contact_group, contacts_list):
        self.contacts_list = contacts_list
        self.contact_group = contact_group

    def add_contact(self,contact):
        def sortName(j):
            return j['name']
        self.contacts_list.append(contact)
        self.contacts_list.sort(key=sortName)

    def remove_contact(self,name):
        for i,x in enumerate(self.contacts_list):
            if(x['name']==name):
                self.contacts_list.pop(i)

    def find_shared_contacts(self, contact_list):
        return [k for k in self.contacts_list if k in contact_list.contacts_list]




friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]
my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

my_friends_list.add_contact({'name':'Amber', 'number':'888-8888'})
my_work_buddies.remove_contact('Carlos')

print(my_friends_list.contact_group,my_friends_list.contacts_list)
print(my_work_buddies.contact_group,my_work_buddies.contacts_list)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)