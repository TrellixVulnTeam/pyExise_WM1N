#encoding=gbk
#�������class variable������������object variable��ʾ��

class Robot:
    #��ʾһ�������ֵĻ�����
    #����һ����������ڻ�������������
    population=0
    def __init__(self, name):
        self.name = name
        print('robot {0} created'.format(self.name))

        #���˳�ʼ������������ʱ��������������1
        Robot.population += 1

    def destoy(self):
        print('{0} is died'.format(self.name))
        Robot.population -=1

        if Robot.population==0:
            print('{0} is the last one'.format(self.name))
        else:
            print('We still have {0} robots'.format(Robot.population))

    def say_hi(self):
        '''���Ի����˵�����ʺ�
        û���������ĵ���'''
        print('Greetings, my master call me {0}'.format(self.name))

    @classmethod
    def how_many(cls):
        ''''��ӡ����ǰ�Ļ����˵�����'''
        print('We have {:d} robots'.format(cls.population))

droid1=Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2=Robot('C-3P0')
droid2.say_hi()
Robot.how_many()

print('Robots can do something here')

print("Robots have done there work , let's destroy them")
droid1.destoy()
droid2.destoy()
droid2.how_many()
Robot.how_many()

