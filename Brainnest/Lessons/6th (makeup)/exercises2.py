'''
1. Write a Python program 
that reads in a JSON file containing data on a set of customers,
and outputs a list of all the unique countries that the customers are from.
'''

import json

with open('customers.json', 'r') as me:
    data = json.load(me)
    for customer in data:
        print(customer['country'])
        

'''
2. Write a Python program that takes a JSON file containing data on a set of products,
and outputs the name and price of the most expensive product.
'''

with open('products.json', 'r') as me:
    products = json.load(me)
    x = 0
    this_p = ''
    for product in products:
        if product['price'] > x:
            x = product['price']
            this_p = product['name']
    
    print(this_p, x)
    
    '''
    3. Write a Python program that takes a JSON file containing data on a set of users,
    and creates a dictionary where each key is a user ID and each value is a list of the user's followers.
    (( output = {1: [2, 3], 2: [1], 3: [1]} ))
    '''
    
with open('users.json', 'r') as me:
    users = json.load(me)
    result_dict = {}
    for user in users:
        followers = []
        for each in user['followers']:
            followers.append(each['id'])
        result_dict.update({user['id'] : followers})
         
          
    print(result_dict)
    
    '''
4. Write a Python program that takes a JSON file containing data on a set of tweets,
and outputs the number of times each hashtag is used.
'''

with open('tweets.json', 'r') as me:
    tweets = json.load(me)
    totallist = []
    for tweet in tweets:
        for hashtag in tweet['hashtags']:
            totallist.append(hashtag)
    number_used = {}
    for all in totallist:
        if all not in number_used:
            number_used.update({all : 1})
        else:
            number_used[all] += 1     
          
    print(number_used)

'''
5.
Write a Python program that takes a JSON file containing data on a set of movies,
and creates a bar chart showing the number of movies released in each year from 2000 to the current year.
    '''
    
with open('movies.json', 'r') as me:
    movies = json.load(me)
    barchart = {}
    for movie in movies:
        if movie['year'] not in barchart:
            barchart.update({movie['year'] : [movie['title']]})
        else:
            barchart[movie['year']].append(movie['title'])
            
    print(barchart)
        
        
    

    
        