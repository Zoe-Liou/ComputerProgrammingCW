#!/usr/bin/env python
# coding: utf-8

# # Activity 1

# ## 1.1 The domain classes

# In[1]:


import json


# In[23]:

# Product class with json output, summary, getting attributes, EAD check, and quantity changing fuction.
class Product:
    # define a empty set to store unique EAD to check if the EAD exists
    unique_id_set = set()
    
    def __init__(self, name, price, quantity, unique_identifier, brand):
            self.name = str(name)
            self.price = float(price)
            self.quantity = int(quantity)
            self.unique_identifier = str(unique_identifier)
            self.brand = str(brand)
    
    # export json representation output
    # return key-value pairs of the product attributes
    def to_json(self):
        product_list = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'unique_identifier': self.unique_identifier,
            'brand': self.brand
        }
        # save json
        json.dump(product_list, open('result.json', 'w'))
        
        # read json
        #code from https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/
        with open('result.json', 'r') as myproduct_json:
            data = myproduct_json.read()

        # load json
        converted_list = json.loads(data)
        
        return converted_list
    
    # print formatted summary of the product
    def product_summary(self):
        return (self.name, self.price, self.quantity, self.unique_identifier, self.brand)
    
    # get value for each attributes
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_quantity(self):
        return self.quantity
    
    def get_id(self):
        return self.unique_identifier
    
    # re-define the product quantity
    def set_quantity(self, quantity):
        self.quantity = int(quantity)
        
    # check if unique EAD exists
    def id_check(self):
        try:
            # code from: https://www.pythonpool.com/python-check-if-string-is-integer/
            isInt = True
            try:
                # make sure EAD is a digit sequence
                int(self.unique_identifier)
            except ValueError:
                isInt = False
            
            # if the EAD lenght is 13 and not in the EAD set, and then return boolean value True
            if isInt and len(self.unique_identifier) == 13 and (self.unique_identifier not in Product.unique_id_set):
                Product.unique_id_set.add(self.unique_identifier)
                return True
            
            # if the EAD lenght is 13 but in the EAD set, and then return boolean value False
            if isInt and len(self.unique_identifier) == 13 and (self.unique_identifier in Product.unique_id_set):
                return False
        except:
            print('Please enter a new id!')
    
    def remove_id(self, existing_EAD):
        self.existing_EAD = existing_EAD
        Product.unique_id_set.remove(self.existing_EAD)


# In[24]:

# Clothing class with two addtional attributes: cloth size and matrial
class Clothing(Product):
    
    # define sub-class for specific product
    # with additionational atrributs: size and material
    def __init__(self, name, price, quantity, unique_identifier, brand, size, material):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.size = str(size).upper()
        self.material = str(material)
    
    # export json representation output
    # return key-value pairs of the product attributes
    def to_json(self):
        product_list = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'unique_identifier': self.unique_identifier,
            'brand': self.brand,
            'size': self.size,
            'material': self.material
        }
        # save json
        json.dump(product_list, open('result.json', 'w'))
        
        # read json
        # code from https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/
        with open('result.json', 'r') as myproduct_json:
            data = myproduct_json.read()

        # load json
        converted_list = json.loads(data)
        
        return converted_list
    
    # print formatted summary of the product
    def product_summary(self):
        return (self.name, self.price, self.quantity, self.unique_identifier, self.brand,
                self.size, self.material)


# In[25]:

# Foof class with three addtional attributes: expiry date, gluten free check and vegan free check
class Food(Product):
    
    # define sub-class for specific product
    # with additionational atrributs: expiry_date, gluten_free, and suitable_for_vegans
    def __init__(self, name, price, quantity, unique_identifier, brand, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.expiry_date = str(expiry_date) # YYYY-MM-DD
        self.gluten_free = bool(gluten_free) # True or False
        self.suitable_for_vegans = bool(suitable_for_vegans) # True or False
    
    # export json representation output
    # return key-value pairs of the product attributes
    def to_json(self):
        product_list = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'unique_identifier': self.unique_identifier,
            'brand': self.brand,
            'expiry_date': self.expiry_date,
            'suitable_for_vegans': self.suitable_for_vegans
            
        }
        # save json
        json.dump(product_list, open('result.json', 'w'))
        
        # read json
        # code from https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/
        with open('result.json', 'r') as myproduct_json:
            data = myproduct_json.read()

        # load json
        converted_list = json.loads(data)
        return converted_list
    
    # print formatted summary of the product
    def product_summary(self):
        return (self.name, self.price, self.quantity, self.unique_identifier, self.brand,
                self.expiry_date, self.gluten_free, self.suitable_for_vegans)


# In[26]:

# Phone class with two addtional attributes: phone color and network type
class Phone(Product):
    
    # define sub-class for specific product
    # with additionational atrributs: colour and network types
    def __init__(self, name, price, quantity, unique_identifier, brand, colour, network):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.colour = str(colour)
        self.network = str(network) #2G, 3G, 4G or 5G
    
    # export json representation output
    # return key-value pairs of the product attributes    
    def to_json(self):
        product_list = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'unique_identifier': self.unique_identifier,
            'brand': self.brand,
            'colour': self.colour,
            'network': self.network
        }
        # save json
        json.dump(product_list, open('result.json', 'w'))
        
        # read json
        # code from https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/
        with open('result.json', 'r') as myproduct_json:
            data = myproduct_json.read()

        # load json
        converted_list = json.loads(data)
        return converted_list
    
    # print formatted summary of the product
    def product_summary(self):
        return (self.name, self.price, self.quantity, self.unique_identifier, self.brand,
                self.colour, self.network)


# ## self-defined functions

# In[27]:


# if inputted type is not in product_type
# the function will prompt user to enter again
def check_type():
    while True:
        input_product = input('Insert its type (Clothing, Food, Phone): ').capitalize()
        product_type = ['Clothing', 'Food', 'Phone']
        if input_product in product_type:
            return input_product
        else:
            print('Please enter a correct product type.')


# In[28]:


# if inputted price is not a positive float
# the function will prompt user to enter again
def check_price():
    while True:
        try:
            product_price = input('Insert its price (£): ')
            if float(product_price) and float(product_price) > 0:
                return float(product_price)
            else:
                print('Price needs to be a positive number.')
        except:
            print('Price needs to be a positive number.')


# In[29]:


# if inputted quantity is not a positive integer
# the function will prompt user to enter again
def check_quantity():
    while True:
        try:
            product_quantity = input('Insert its quantity: ')
            if int(product_quantity) and int(product_quantity) > 0:
                return int(product_quantity)
            else:
                print('Quantity needs to be a positive integer.')
        except:
            print('Quantity needs to be a positive integer.')


# In[30]:


# if inputted quantity is not in the size_list
# the function will prompt user to enter again
# and shows available size list
def check_size():
    while True:
        size_list = ['XS','S','M','L','XL','XXL']
        product_size = input('Insert its size (e.g., XL): ').upper()
        if product_size in size_list:
            return product_size
        else:
            print('Please enter a correct size.')
            print('Available sizes: ', size_list)


# In[31]:


# only boolean values will be accepted
def check_gluten():
    while True:
        product_gluten = input('Insert if it is gluten free (True/False): ').capitalize()
        if product_gluten == 'True' or product_gluten == 'T':
            return True
        elif product_gluten == 'False' or product_gluten == 'F':
            return False
        else:
            print('Please enter True or False.')


# In[32]:


# only boolean values will be accepted
def check_vegans():
    while True:
        product_vegans = input('Insert if it is suitable for vegans (True/False): ').capitalize()
        if product_vegans == 'True' or product_vegans == 'T':
            return True
        elif product_vegans == 'False' or product_vegans == 'F':
            return False
        else:
            print('Please enter True or False.')


# In[33]:


# if inputted quantity is not in the network_list
# the function will prompt user to enter again
def check_network():
    while True:
        network_list = ['2G','3G','4G','5G']
        product_network = input('Insert its network type (e.g., 4G): ').upper()
        if product_network in network_list:
            return product_network
        else:
            print('Please enter a correct network type')
            print('Available types: ', network_list)


# In[34]:


def change_quantity():
    while True:
        try:
            product_quantity = input('Type the new quantity: ')
            if int(product_quantity) and int(product_quantity) > 0:
                return int(product_quantity)
            elif int(product_quantity) == 0:
                return False
            else:
                print('Quantity needs to be a positive integer.')
        except:
            print('Quantity needs to be a positive integer.')


# ## 1.2 The shopping system

# In[35]:


class ShoppingCart:
    # empty cart list to store products
    cart_list = []
    
    def get_cart(cls):
        return ShoppingCart.cart_list
    
    def addProduct(self, product):
        self.product = product
        ShoppingCart.cart_list.append(self.product)
    
    def removeProduct(self, product):
        self.product = product
        ShoppingCart.cart_list.remove(self.product)
    
    def changeProductQuantity(self, product, quantity):
        self.product = product
        self.quantity = int(quantity)
        self.product.set_quantity(self.quantity)


# ## 1.3 Doing some shopping

# In[ ]:


print('The program has started.')
print('Insert your next command (H for help):')
terminated = False
while not terminated:
    # define ShoppingCart class
    shopping_cart = ShoppingCart()
    c = input('Type your next command:')
    
    # check if the ean+price combination exists. if not, add. else no. 
    # add a product to the cart
    if c == 'A' or c == 'a':
        print('Adding a new product:')
        product_type = check_type()
        product_name = input('Insert its name: ')
        product_price = check_price()
        product_quantity = check_quantity()
        product_brand = input('Insert its brand: ')
        product_identifier = input('Insert its EAN code: ')
        
        # according to the type user input, add the product to the shopping cart list
        # the product type is Clothing
        if product_type == 'Clothing':
            product_size = check_size()
            product_material = input('Insert its material: ')
            
            product = Clothing(name = product_name, price = product_price,
                               quantity = product_quantity, unique_identifier = product_identifier,
                               brand = product_brand, size = product_size,
                               material = product_material)
            
            # check the EAD is unique
            # add product and print the number of product in the shopping cart
            if product.id_check() == True:
                shopping_cart.addProduct(product)
                print('The product', product_name, 'has been added to the cart.')
                print('The cart contains', len(shopping_cart.get_cart()), 'products.')
            
            # if the EAD exists, suggest user to change the quantity of the product
            elif product.id_check() == False:
                print('The product exists. Please enter Q/q to change the product quantity.')
            else:
                print('Invalid EAN code. Please start again!')
        
        # the product type is Food
        if product_type == 'Food':
            product_date = input('Insert its expiry date (e.g., 2021-10-28): ')
            product_gluten = check_gluten()
            product_vegans = check_vegans()
            
            product = Food(name = product_name, price = product_price,
                           quantity = product_quantity, unique_identifier = product_identifier,
                           brand = product_brand, expiry_date = product_date,
                           gluten_free = product_gluten, suitable_for_vegans = product_vegans)
            
            # check the EAD is unique
            # add product and print the number of product in the shopping cart
            if product.id_check() == True:
                shopping_cart.addProduct(product)
                print('The product', product_name, 'has been added to the cart.')
                print('The cart contains', len(shopping_cart.get_cart()), 'products.')
            
            # if the EAD exists, suggest user to change the quantity of the product
            elif product.id_check() == False:
                print('The product exists. Please enter Q/q to change the product quantity.')
            else:
                print('Invalid EAN code. Please start again!')
        
        # the product type is Phone
        if product_type == 'Phone':
            product_colour = input('Insert its colour: ')
            product_network = check_network()
            
            product = Phone(name = product_name, price = product_price,
                           quantity = product_quantity, unique_identifier = product_identifier,
                           brand = product_brand, colour = product_colour,
                           network = product_network)
            
            # check the EAD is unique
            # add product and print the number of product in the shopping cart
            if product.id_check() == True:
                shopping_cart.addProduct(product)
                print('The product', product_name, 'has been added to the cart.')
                print('The cart contains', len(shopping_cart.get_cart()), 'products.')
            
            # if the EAD exists, suggest user to change the quantity of the product
            elif product.id_check() == False:
                print('The product exists. Please enter Q/q to change the product quantity.')
            else:
                print('Invalid EAN code. Please start again!')
            
    # remove an existing product
    elif c == 'R' or c == 'r':
        
        # show the products' EAD of the existing shopping cart
        # allow user to spesify which product to remove
        print('The existing shopping cart: ')
        cart_list = shopping_cart.get_cart()
        cart_id = []
        for i in cart_list:
            cart_id.append(i.get_id())
        print(cart_id)

        # if the shopping cart is not empty, prompt user to input the product EAD number
        if len(cart_list) != 0:
            remove_id = input('Input the product id that you want to remove: ')
            for i in cart_list:
                if i.get_id() == remove_id:
                    shopping_cart.removeProduct(i)
                    i.remove_id(remove_id)
            
            # show the shopping cart again
            print('The updated shopping cart: ')
            cart_id = []
            for i in cart_list:
                cart_id.append(i.get_id())
            print(cart_id)
        
        # if the shopping cart is empty
        else:
            print('Your shopping cart is empty!')
        
    # summary of an ongoing shopping session    
    elif c == 'S' or c == 's':
        cart_list = shopping_cart.get_cart()
        
        # if the shopping cart is not empty, print summary of the shopping cart
        # with product name, quantity and price
        if len(cart_list) != 0:
            print('This is the total of expenses: ')
            
            cart_list = shopping_cart.get_cart()
            total_price = 0
            for i in range(len(cart_list)):
                if cart_list[i].get_quantity() == 1:
                    total_price = total_price + cart_list[i].get_price()
                    print('  ' + str(i+1) + ' - ' + str(cart_list[i].get_name()) + ' = £' + str(cart_list[i].get_price()))
                else:
                    total_price = total_price + cart_list[i].get_price()*cart_list[i].get_quantity()
                    print('  ' + str(i+1) + ' - ' + str(cart_list[i].get_quantity()) + ' * ' + str(cart_list[i].get_name()) + ' = £' + str((cart_list[i].get_quantity())*(cart_list[i].get_price())))
            print(' Total = £' + str(total_price))
        
        # if the shopping cart is empty
        else:
            print('Your shopping cart is empty!')
                          
    # change quantity
    elif c == 'Q' or c == 'q':
        cart_list = shopping_cart.get_cart()
        
        # show the products' EAD of the existing shopping cart
        # allow user to spesify which product to change the quantity
        cart_quantity = {}
        for i in cart_list:
            cart_quantity[i.get_id()] = i.get_quantity()
        
        if len(cart_list) != 0:
            print('Check the existing shopping cart: ')
            print(cart_quantity)
            
            product_id = input('Input the product ID that you want to change quantity from the shopping cart: ')
            product_quantity = change_quantity()
            
            # cannot find the product
            if product_id not in cart_quantity.keys():
                print('Cannot find this product! Please input a new ID!')
            else:
                # if the user input quantity is 0, the remove the product
                if product_quantity == False:
                    for i in cart_list:
                        if i.get_id() == product_id:
                            shopping_cart.removeProduct(i)
                            i.remove_id(product_id)
                    print('Entered quantity is 0 so product has been removed!')
                
                # if the user input quantity is not 0, then change to the new quantity
                else:
                    for i in cart_list:
                        if i.get_id() == product_id:
                            shopping_cart.changeProductQuantity(i, product_quantity)
            
            # print updated shopping cart
            print('The updated shopping cart: ')
            cart_quantity = {}
            for i in cart_list:
                cart_quantity[i.get_id()] = i.get_quantity()
            print(cart_quantity)
            
        # if the shopping cart is empty    
        else:
            print('Your shopping cart is empty!')
        
    # generate a json file
    elif c == 'E' or c == 'e':
        cart_list = shopping_cart.get_cart()
        
        # check if the shopping cart is empty
        if len(cart_list) != 0:
            
            # store all product details to a dictionary with EAD as the keys
            cart_dict = {}
            for i in cart_list:
                key_name = i.get_id()
                cart_dict[key_name] = i.to_json()

            # save json
            json.dump(cart_dict, open('my_shopping_cart.json', 'w'))
            
            # read json
            with open('my_shopping_cart.json', 'r') as mycart_json:
                data = mycart_json.read()
            
            # load json
            cart_json = json.loads(data)
            print(cart_json)    

        else:
            print('Your shopping cart is empty. Please add some products.')
        
    # terminate the loop
    elif c == 'T' or c == 't':
        print('Goodbye')
        break
    
    # help commands
    elif c == 'H' or c == 'h':
        print('The program supports the following commands:')
        print('  [A] - Add a new product to the cart')
        print('  [R] - Remove a product from the cart')
        print('  [S] - Print a summary of the cart')
        print('  [Q] - Change the quantity of a product')
        print('  [E] - Export a JSON version of the cart')
        print('  [T] - Terminate the program')
        print('  [H] - List the supported commands')
    
    # other commands
    else:
        print('Command not recognised. Please try again')









