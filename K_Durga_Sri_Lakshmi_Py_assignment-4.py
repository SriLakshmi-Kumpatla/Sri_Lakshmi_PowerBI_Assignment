class Department:
    tot_depts = 0  

    def __init__(self, dept_id, name, location, hod):
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.hod = hod
        Department.tot_depts += 1

    def display_info(self):
        print(f"\nDepartment ID: {self.dept_id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"HOD: {self.hod}")

    @classmethod
    def display_total_departments(cls):
        print(f"\nTotal number of departments in the organization: {cls.tot_depts}")

depts = []

num = int(input("Enter the number of departments: "))


for i in range(num):
    print(f"\nEnter details for department {i+1}")
    dept_id = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    hod = input("Enter HOD Name: ")

    dept = Department(dept_id, name, location, hod)
    depts.append(dept)

print("\nAll Department Information:")
for dept in depts:
    dept.display_info()


search_id = input("\nEnter Department ID to search: ")
found = False
for dept in depts:
    if dept.dept_id == search_id:
        print("\nDepartment found:")
        dept.display_info()
        found = True
        break
if not found:
    print("Department ID not found.")

s_nm = input("\nEnter Department Name to search (startswith/in/endswith): ").lower()

print("\nDepartments matching the search criteria:")
mf = False
for dept in depts:
    nm_low = dept.name.lower()
    if nm_low.startswith(s_nm) or s_nm in nm_low or nm_low.endswith(s_nm):
        dept.display_info()
        mf = True

if not mf:
    print("No department found with the given name search pattern.")

Department.display_total_departments()
