#encoding=gbk
#��̳�ʾ��

class SchoolMember:
    '''����ѧУ����κγ�Ա'''
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print('Initializing memeber {}'.format(self.name))

    def tell(self):
        '''�������й��ҵ�ϸ��'''
        print('name:{},age:{}'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    '''������Ϊ��ʦ'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary=salary
        print('(Initialized teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''����һλѧ��'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
        print("Initialized student {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Student's marks is {:d}".format(self.marks))

t=Teacher("Mrs Liu",40,30000)
s=Student("xiao zhang",20,85)

#��ӡ�հ���
print()

members=[t,s]
for member in members:
    member.tell()