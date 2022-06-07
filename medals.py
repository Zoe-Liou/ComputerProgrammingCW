#!/usr/bin/env python
# coding: utf-8

# # Activity 3

# ## 3.1 CountryMedals class and methods

# In[15]:


import json


# In[16]:


class CountryMedals:
    def __init__(self, country_name, gold, silver, bronze):
        self.country_name = str(country_name).title()
        self.gold = int(gold)
        self.silver = int(silver)
        self.bronze = int(bronze)
        self.total = self.gold + self.silver + self.bronze
    
    # export json reprsetation of the object
    # country name as the key and the number medals as the value
    def to_json(self, filename=None):
        medal_dic = {
            self.country_name: 
            {'gold': self.gold,
             'silver': self.silver,
             'bronze': self.bronze,
             'total': self.total
            }}
        return medal_dic
    
    # get the number of specified medal of the object
    def get_medals(self, medal_type):
        self.medal_type = str(medal_type).lower()
        if self.medal_type == 'gold':
            return self.gold
        
        elif self.medal_type == 'silver':
            return self.silver
            
        elif self.medal_type == 'bronze':
            return self.bronze
        
        elif self.medal_type == 'total':
            return self.total
        
        else:
            print('None')
    
    # return formatted text summary of the number of medal for a given country
    def print_summary(self):
        print(self.country_name, 'received', str(self.total), 'in total;',
             str(self.gold), 'gold,', str(self.silver), 'silver, and', str(self.bronze), 'bronze.')
    
    def get_country(self):
        return self.country_name

    # a fuction that compares four types of medal between two countries in formatted text
    # and shows the differences in each type of medal
    # country object as the attribute
    def compare(self, compared_country):
        print('Medals comparison between ’' + self.country_name + '’ and ’' + compared_country.get_country() + ':')
        
        # compare the number of gold medal
        if self.gold == compared_country.get_medals('gold'):
            print('- Both', self.country_name, 'and', compared_country.get_country(), 'received', str(self.gold), 'gold medal(s).')
        elif self.gold > compared_country.get_medals('gold'):
            print('- ' + self.country_name + ' received '+ str(self.gold) +' gold medal(s), '+ str(abs(self.gold - compared_country.get_medals('gold'))) + ' more than ' + compared_country.get_country() + ', which received ' + str(compared_country.get_medals('gold')) + '.')
        elif self.gold < compared_country.get_medals('gold'):
            print('- ' + self.country_name + ' received '+ str(self.gold) +' gold medal(s), '+ str(abs(self.gold - compared_country.get_medals('gold'))) + ' fewer than ' + compared_country.get_country() + ', which received ' + str(compared_country.get_medals('gold')) + '.')
        
        # compare the number of silver medal
        if self.silver == compared_country.get_medals('silver'):
            print('- Both', self.country_name, 'and', compared_country.get_country(), 'received', str(self.silver), 'silver medal(s).')
        elif self.silver > compared_country.get_medals('silver'):
            print('- ' + self.country_name + ' received '+ str(self.silver) +' silver medal(s), '+ str(abs(self.silver - compared_country.get_medals('silver'))) + ' more than '+ compared_country.get_country() + ', which received ' + str(compared_country.get_medals('silver')) + '.')
        elif self.silver < compared_country.get_medals('silver'):
            print('- ' + self.country_name + ' received '+ str(self.silver) +' silver medal(s), '+ str(abs(self.silver - compared_country.get_medals('silver'))) + ' fewer than ' + compared_country.get_country() + ', which received ' + str(compared_country.get_medals('silver')) + '.')
        
        # compare the number of bronze medal
        if self.bronze == compared_country.get_medals('bronze'):
            print('- Both', self.country_name, 'and', compared_country.get_country(), 'received', str(self.bronze), 'bronze medal(s).')
        elif self.bronze > compared_country.get_medals('bronze'):
            print('- ' + self.country_name + ' received '+ str(self.bronze) +' bronze medal(s), '+ str(abs(self.bronze - compared_country.get_medals('bronze'))) + ' more than ' + compared_country.get_country() + ', which received ' + str(compared_country.get_medals('bronze')) + '.')
        elif self.bronze < compared_country.get_medals('bronze'):
            print('- ' + self.country_name + ' received '+ str(self.bronze) +' bronze medal(s), '+ str(abs(self.bronze - compared_country.get_medals('bronze'))) + ' fewer than ' + compared_country.get_country() + ', which received ' + str(compared_country.get_medals('bronze')) + '.')
        
        # compare the total number of medal
        if self.total == compared_country.get_medals('total'):
            print("")
            print('Overall, Both', self.country_name, 'and', compared_country.get_country(), 'received', str(self.total), 'medal(s).')
        elif self.total > compared_country.get_medals('total'):
            print("")
            print('Overall, ' + self.country_name + ' received '+ str(self.total) +' medal(s), '+ str(abs(self.total - compared_country.get_medals('total'))) + ' more than ' + compared_country.get_country() + ', which received ' + str(compared_country.get_medals('total')) + ' medal(s).')
        elif self.total < compared_country.get_medals('total'):
            print("")
            print('Overall, ' + self.country_name + ' received '+ str(self.total) +' medal(s), '+ str(abs(self.total - compared_country.get_medals('total'))) + ' fewer than ' + compared_country.get_country() + ', which received ' + str(compared_country.get_medals('total')) + ' medal(s).')


# ## 3.2 Loading the data

# In[17]:


import csv

filepath = '/Users/zoeliu/Documents/ KCLDS/Computerprogramming/'
countries = {}

# open Medals.csv file and store it to the countries dictionary
# with country name as the key and country object as the value
with open(filepath+'Medals.csv', newline='') as country_medal:
    medal = csv.DictReader(country_medal)
    for row in medal:
        countries[row['Team/NOC'].title()] = CountryMedals(country_name = row['Team/NOC'], gold = row['Gold'],
                                                   silver = row['Silver'], bronze = row['Bronze'])


# ## 3.3 Defining useful functions

# In[18]:


# alphabetically sorted country name
def get_sorted_list_of_country_names(countries):
    return sorted(list(countries.keys()))


# In[19]:

# sort the country name by the number of medals in ascending order
def sort_countries_by_medal_type_ascending(countries, medal_type):
    return list(l[1] for l in sorted(countries.items(), key=lambda a: a[1].get_medals(medal_type)))


# In[20]:

# sort the country name by the number of medals in descending order
def sort_countries_by_medal_type_descending(countries, medal_type):
    return list(l[1] for l in sorted(countries.items(), key=lambda a: a[1].get_medals(medal_type), reverse=True))


# In[21]:

# if it is not a positive integer, then prompt user to enter again
def read_positive_integer():
    while True:
        try:
            input_num = int(input('Enter the threshold (a positive integer): '))
            check_int = isinstance(input_num, int)
            if check_int == True and input_num >= 0:
                return int(input_num)
        except:
            print('Please input a positive integer!')


# In[22]:

# check the country name is in countries.keys()
def read_country_name():
    while True:
        input_country = str(input('Insert a country name: ')).title()
        if input_country in list(countries.keys()):
            return input_country
        else:
            print('Please input the country name again!')
            print('Available country names: ')
            print(' ')
            print(list(countries.keys()))


# In[23]:

# check the country name is in the medal type_set
def read_medal_type():
    while True:
        input_type = str(input('Insert a medal type (choose among \'gold\', \'silver\', \'bronze\', or \'total\'):')).lower()
        type_set = ['gold', 'silver', 'bronze', 'total']
        if input_type in type_set:
            return input_type
        else:
            print('Please input the medal type again!')
            print('Available medal types: ')
            print(type_set)


# In[24]:

# check the file name containing '.json'
def check_file():
    while True:
        filename = input('Enter the file name (without \'.json\'): ')
        if filename.find('.json') == -1:
            return filename
        else:
            print('Please enter a file name without \'.json\'')


# ## 3.4 Execution loop

# In[25]:


while True:
    a = input('Insert a command (Type \'H\' for help ): ')
    
    # provide helpful function to user
    if a == 'Help' or a == 'H' or  a == 'h' or a == 'help':
        print('List of commands:')
        print('- (H)elp shows the list of comments;')
        print('- (L)ist shows the list of countries present in the dataset')
        print('- (S)ummary prints out a summary of the medals won by a single country;')
        print('- (C)ompare allows for a comparison of the medals won by two countries;')
        print('- (M)ore, given a medal type, lists all the countries that received more medals than a treshold;')
        print('- (F)ewer, given a medal type, lists all the countries that received fewer medals than a treshold;')
        print('- (E)xport, save the medals table as \'.json\' file;')
        print('- (Q)uit.')
    
    # return alphabetically sorted country name list
    elif a == 'List' or a == 'L' or  a == 'l' or a == 'list':
        cnt = ', '.join(get_sorted_list_of_country_names(countries))
        print('The data set contain {} countries: {}'.format(len(list(countries.keys())), cnt))
    
    # print formatted text summary of a given country
    elif a == 'Summary' or a == 'S' or  a == 's' or a == 'summary':
        country = read_country_name()
        countries[country].print_summary()
    
    # compare two country
    elif a == 'Compare' or a == 'C' or  a == 'c' or a == 'compare':
        print('Compare two countries')
        country_1 = read_country_name()
        print('Insert the name of the country you want to compare against \'{}\''.format(country_1))
        country_2 = read_country_name()
        # index country objects using country name in dictionary countries
        countries[country_1].compare(countries[country_2])

    # return all the countries that received more medals than a given integer with a given medal type
    # the returned list is sorted by the number of medals in descending order
    elif a == 'More' or a == 'M' or  a == 'm' or a == 'more':
        print('Given a medal type, lists all the countries that received more medals than a treshold;')
        medal_type = read_medal_type()
        threshold = read_positive_integer()
        countries_des = sort_countries_by_medal_type_descending(countries, medal_type)

        print('Countries that received more than {} \'{}\' medals:'.format(threshold, medal_type))
        for i in range(len(countries_des)):
            if countries_des[i].get_medals(medal_type) > threshold:
                print(' - {} received {}'.format(countries_des[i].get_country(), countries_des[i].get_medals(medal_type)))
    
    # return all the countries that received fewer medals than a given integer with a given medal type
    # the returned list is sorted by the number of medals in ascending order
    elif a == 'Fewer' or a == 'F' or  a == 'f' or a == 'fewer':
        print('Given a medal type, lists all the countries that received fewer medals than a treshold;')
        medal_type = read_medal_type()
        
        threshold = read_positive_integer()
        countries_asc = sort_countries_by_medal_type_ascending(countries, medal_type)
        
        print('Countries that received fewer than {} \'{}\' medals:'.format(threshold, medal_type))
        for i in range(len(countries_asc)):
            if countries_asc[i].get_medals(medal_type) < (threshold):
                print(' - {} received {}'.format(countries_asc[i].get_country(), countries_asc[i].get_medals(medal_type)))
        
    # export all country medals to a json file
    elif a == 'Export' or a == 'E' or  a == 'e' or a == 'export':
        # check and input the file name
        filename = check_file()

        medal_j = {}
        country_name = list(countries.keys())
        for i in range(len(country_name)):
            medal_j[country_name[i]] = countries[country_name[i]].to_json()[country_name[i]]
            
        json.dump(medal_j, open(filename, 'w'))
        print('File \'{}\' correctly saved.'.format(filename))
        
        # if the user wants to read and load json now
        read_json = str(input('Enter Y/N to read the saved json file: ').title())
        if read_json == 'Y' or read_json == 'yes' or read_json == 'Yes' or read_json == 'y':
            # read json
            with open(filename, 'r') as mymedal_json:
                data = mymedal_json.read()

            # load json
            medal_json = json.loads(data)
            print(medal_json)
        elif read_json == 'N' or read_json == 'no' or read_json == 'No' or read_json == 'n':
            print('You can check the json file later!')
        else:
            print("Invalid commands")
        
    # quit the while loop
    elif a == 'Quit' or a == 'Q' or  a == 'q' or a == 'quit':
        print('Goodbye')
        break
    
    # unrecognised commands
    else:
        print('Command not recognised. Please try again')


# In[ ]:




