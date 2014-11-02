#!/usr/bin/python
import getpass
from fedora.client.fas2 import AccountSystem
import codecs

def calc_list():
    '''Generate data'''
    output = []
    people_list = []
    flag = 0
    group_name = 'cla_done'
    username = raw_input("Username: ")
    password = raw_input("Password: ")

    fas = AccountSystem(username=username, password=password)

    print 'Generating data file. Waiting...'  
    data = fas.people_by_key(key='username', search=u'*', fields=['human_name', 'username', 'email', 'status', 'country_code'])

    output_file = codecs.open('/tmp/FAS-Hungarian-members.txt', encoding='utf-8', mode='w+')

    for item in data.values():
	if str(item['country_code']) == 'HU' and item['status'] == 'active':
	    output_data = item['human_name'] + " " + item['username'] + " " + item['email'] + " " + str(item['country_code']) + " " + item['status'] + "\n"
	    output_file.write(output_data)

    output_file.close()

    print 'File successfully generated!'

if __name__ == "__main__":
    calc_list()
