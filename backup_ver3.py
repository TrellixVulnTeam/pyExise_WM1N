#coding=gbk
#�ļ����ݸĽ��棬�Ե�������ΪĿ¼��Ĭ����ʱ��Ϊzip�ļ����֣�����û����뱸ע����ʱ��+��ע��Ϊ�ļ�����
import os
import time


#��Ҫ���ݵ��ļ�Ŀ¼�б�
source=[r'C:\Users\zk\Pictures', r'"C:\Users\zk\Documents\WeChat Files\zhengknight\Files"']

#Ŀ���ļ���
target_dir=r'e:\backup'
#���Ŀ��Ŀ¼�������򴴽�
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#�����ļ���
today=target_dir + os.sep + time.strftime('%Y%m%d')

#����ǰʱ����Ϊ���ݵ��ļ���
now = time.strftime('%H%M%S')
#��ȡ�û����뱸ע��Ϣ
comment = input('�����뱸ע��Ϣ-->')
#����û��Ƿ����뱸ע
if len(comment)==0:
   target=today + os.sep + now + '.zip'
else:
    #�˴�һ�������л��е�ʱ��pycharm�Զ������Ϸ�б����
    target = today + os.sep + now + '_'\
             +comment.replace(' ','_') + '.zip'
#��������ļ��в������򴴽�
if not os.path.exists(today):
    os.mkdir(today)
    print('�����ļ���Ŀ¼�����ɹ�',today)

#����zip������
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('zip_command')
print(zip_command)
print('Running')
if os.system(zip_command)==0:
    print('�ѳɹ����ݵ�',target)
else:
    print('����ʧ�ܣ�����')
