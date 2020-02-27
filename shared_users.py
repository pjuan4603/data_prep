# This file is used to get shared users between target and source domains for cross domain experiments and also to map business ids to an integer
# INPUT : target domain and list of source domains
# OUTPUT : output will be stored under /experiments
import pandas as pd
import numpy as np
import statistics as sta
import json

#print data['asin']
# This file is used for reading file
# INPUT : file name
# OUTPUT : list of review ids, set of users and set of businesses
def readCSV(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    result = []
    user = set()
    item = set()
    for line in lines:
        comp = json.loads(line)
        uId = comp['user_id']
        #print uId
        iId = comp['business_id']
        time = comp['stars']
        result.append((uId,iId,time))
        user.add(uId)
        item.add(iId)
    return result,user,item


def takeFirst(elem):
    return elem[0]


def get_all_data(all_s):
    lines = []
    for each_file in all_s:
        f = open(each_file, 'r')
        lines += f.readlines()
        f.close()
    result = []
    user = set()
    item = set()
    for line in lines:
        comp = json.loads(line)
        uId = comp['user_id']
        #print uId
        iId = comp['business_id']
        time = comp['stars']
        result.append((uId,iId,time))
        user.add(uId)
        item.add(iId)
    return result,user,item



# all_sources = [['American.json', 'South American.json',  'African & Middle Eastern Food.json', 'East Asian.json', 'European.json'],
#                ['Food.json'],
#                ['Nightlife.json'],
#                ['Food and Social.json'],
#                ['Shop and Travel.json'],
#                ['Shopping.json'],
#                ['Hotels & Travel.json'],
#                ['Beauty & Spas.json'],
#                ['Pets.json'],
#                ['American.json'],
#                ['South American.json'],
#                ['African & Middle Eastern Food.json'],
#                ['East Asian.json'],
#                ['European.json']
#                ]
#

# all_sources = [['American.json', 'Others.json',  'African & Middle Eastern Food.json', 'East Asian.json', 'European.json'],
#                ['Food.json'],
#                ['Nightlife.json'],
#                ['Food and Social.json'],
#                ['Shop and Travel.json'],
#                ['Shopping.json'],
#                ['Hotels & Travel.json'],
#                ['Beauty & Spas.json'],
#                ['Pets.json'],
#                ['American.json'],
#                ['Others.json'],
#                ['African & Middle Eastern Food.json'],
#                ['East Asian.json'],
#                ['European.json']
#                ]


# all_sources = [['American.json', 'South American.json',  'Others.json', 'East Asian.json', 'European.json'],
#                ['Food.json'],
#                ['Nightlife.json'],
#                ['Food and Social.json'],
#                ['Shop and Travel.json'],
#                ['Shopping.json'],
#                ['Hotels & Travel.json'],
#                ['Beauty & Spas.json'],
#                ['Pets.json'],
#                ['American.json'],
#                ['South American.json'],
#                ['Others.json'],
#                ['East Asian.json'],
#                ['European.json']
#                ]


# all_sources = [['Hobby.json', 'Books, Mags, Music & Video.json',  'Electronics Stores.json', 'Fashion.json', 'Arts & Crafts.json', 'Home & Garden.json'],
#                ['Hotels & Travel.json'],
#                ['Pets.json'],
#                ['Beauty & Spas.json'],
#                ['Shop and Travel.json'],
#                ['Food and Social.json'],
#                ['Nightlife.json'],
#                ['Food.json'],
#                ['Restaurants.json'],
#                ['Hobby.json'],
#                ['Books, Mags, Music & Video.json'],
#                ['Electronics Stores.json'],
#                ['Fashion.json'],
#                ['Arts & Crafts.json'],
#                ['Home & Garden.json']
#                ]


# all_sources = [['Hobby.json', 'Books, Mags, Music & Video.json',  'Electronics Stores.json', 'Meat & Grocery.json', 'Arts & Crafts.json', 'Home & Garden.json'],
#                ['Hotels & Travel.json'],
#                ['Pets.json'],
#                ['Beauty & Spas.json'],
#                ['Shop and Travel.json'],
#                ['Food and Social.json'],
#                ['Nightlife.json'],
#                ['Food.json'],
#                ['Restaurants.json'],
#                ['Hobby.json'],
#                ['Books, Mags, Music & Video.json'],
#                ['Electronics Stores.json'],
#                ['Meat & Grocery.json'],
#                ['Arts & Crafts.json'],
#                ['Home & Garden.json']
#                ]

#
# all_sources = [['Hobby.json', 'Fashion.json',  'Electronics Stores.json', 'Meat & Grocery.json', 'Arts & Crafts.json', 'Home & Garden.json'],
#                ['Hotels & Travel.json'],
#                ['Pets.json'],
#                ['Beauty & Spas.json'],
#                ['Shop and Travel.json'],
#                ['Food and Social.json'],
#                ['Nightlife.json'],
#                ['Food.json'],
#                ['Restaurants.json'],
#                ['Hobby.json'],
#                ['Fashion.json'],
#                ['Electronics Stores.json'],
#                ['Meat & Grocery.json'],
#                ['Arts & Crafts.json'],
#                ['Home & Garden.json']
#                ]

# all_sources = [['Clubs.json'],
#                ['Restaurants.json'],
#                ['Food.json'],
#                ['Food and Social.json'],
#                ['Shop and Travel.json'],
#                ['Shopping.json'],
#                ['Hotels & Travel.json'],
#                ['Pets.json'],
#                ['Beauty & Spas.json'],
#                ]

# all_sources = [['Meat & Grocery.json', 'Candy & Dessert.json',  'Liquors.json', 'Drinks.json'],
#                ['Restaurants.json'],
#                ['Nightlife.json'],
#                ['Food and Social.json'],
#                ['Shop and Travel.json'],
#                ['Hotels & Travel.json'],
#                ['Shopping.json'],
#                ['Pets.json'],
#                ['Beauty & Spas.json'],
#                ['Meat & Grocery.json'],
#                ['Candy & Dessert.json'],
#                ['Liquors.json'],
#                ['Drinks.json']
#                ]


# all_sources = [['Bakery.json', 'Candy & Dessert.json',  'Liquors.json', 'Drinks.json'],
#                ['Restaurants.json'],
#                ['Nightlife.json'],
#                ['Food and Social.json'],
#                ['Shop and Travel.json'],
#                ['Hotels & Travel.json'],
#                ['Shopping.json'],
#                ['Pets.json'],
#                ['Beauty & Spas.json'],
#                ['Bakery.json'],
#                ['Candy & Dessert.json'],
#                ['Liquors.json'],
#                ['Drinks.json']
#                ]

all_sources = [['restaurant.json']]

[book,book_user,book_item] = readCSV('shopping.json')
for case_no in range(1, len(all_sources)+1):
    sources = all_sources[case_no-1]
    print sources
    path = 'experiments/shopping/Case' + str(case_no)
    [movie, movie_user,movie_item] = get_all_data(sources)
    print path

    book = np.array(book)

    #print book
    movie = np.array(movie)

    print book
    #interactionU = [i for i in book_user if i in movie_user]
    interactionU = book_user.intersection(movie_user)
    interactionU = list(sorted(interactionU))

    if len(interactionU) == 0:
        continue

    print 'start cross'
    CrossBooks = [i for i in book if i[0] in interactionU]
    CrossMovies = [i for i in movie if i[0] in interactionU]

    print 'start array'
    CrossBooks = np.array(CrossBooks)
    CrossMovies = np.array(CrossMovies)

    print 'start sort'
    CrossBooks = sorted(CrossBooks, key = takeFirst)
    CrossMovies = sorted(CrossMovies, key = takeFirst)

    print 'start np array'
    CrossBooks = np.array(CrossBooks)
    CrossMovies = np.array(CrossMovies)

    print 'start list'
    Books = list(np.unique(CrossBooks[:, 1]))
    Movies = list(np.unique(CrossMovies[:, 1]))

    print "Case ", case_no, len(interactionU)

    with open("iteruser.txt",'w') as k:
        for i in interactionU:
            k.write("{:s}\n".format(i))


    with open(path + "/target.txt", 'w') as k:
        for i in CrossBooks:
            k.write("{:d}   {:d}    {:d}\n".format(interactionU.index(i[0])+1,Books.index(i[1])+1,int(i[2])))

    with open(path + "/source.txt", 'w') as k:
        for i in CrossMovies:
            k.write("{:d}   {:d}    {:d}\n".format(interactionU.index(i[0])+1,Movies.index(i[1])+1,int(i[2])))


