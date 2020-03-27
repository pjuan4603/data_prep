# This file is used for 5-core process to remove users who are rated less than 5 businesses.
# INPUT : file that are under data/categories which is review data separated based on the categories they belong to
# OUTPUT : all the files will be updated under data/categories
import json
from os import listdir
from os.path import isfile, join


# to check the user count is less than 5 of not
# INPUT : user's review count set
# OUTPUT : boolean
def check_user(user_cnt):
    if len(user_cnt) == 0:
        return True
    for key,value in user_cnt.iteritems():
        if value < 5:
            return True
    return False


# to check the user count is less than 1 of not
# INPUT : business's review count set
# OUTPUT : boolean
def check_business(business_cnt):
    if len(business_cnt) == 0:
        return True
    for key,value in business_cnt.iteritems():
        if value < 1:
            return True
    return False


# logic of 5-core process
# OUTPUT : data will be updated in all the file of data/categories
def remove_reviews():
    all_files = [f for f in listdir('data/categories') if isfile(join('data/categories', f))]

    for each_file in all_files:
        user_cnt = {}
        business_cnt = {}
        while check_user(user_cnt) or check_business(business_cnt):
            print each_file
            user_cnt = {}
            business_cnt = {}
            file = open('data/categories/' + each_file, 'r')
            all_lines = file.readlines()
            for node in all_lines:
                data = json.loads(node)
                if data['user_id'] not in user_cnt:
                    user_cnt[data['user_id']] = 1
                else:
                    user_cnt[data['user_id']] += 1
            file.close()
            # print "Number of Total number users", len(user_cnt)
            cnt = {}
            for item in user_cnt:
                if user_cnt[item] not in cnt:
                    cnt[user_cnt[item]] = 1
                else:
                    cnt[user_cnt[item]] += 1
            # print cnt


            file = open('data/categories/' + each_file, 'w')
            cnt = 0
            for node in all_lines:
                data = json.loads(node)
                if user_cnt[data['user_id']] > 5:
                    file.write(json.dumps(data) + '\n')
                else:
                    cnt += 1
            # print cnt
            file.close()

            file = open('data/categories/' + each_file, 'r')
            all_lines = file.readlines()
            for node in all_lines:
                data = json.loads(node)

                if data['business_id'] not in business_cnt:
                    business_cnt[data['business_id']] = 1
                else:
                    business_cnt[data['business_id']] += 1

            file.close()

            file = open('data/categories/' + each_file, 'w')
            cnt = 0
            for node in all_lines:
                data = json.loads(node)
                if business_cnt[data['business_id']] > 1:
                    file.write(json.dumps(data)+'\n')
                else:
                    cnt += 1
            # print cnt
            file.close()

            file = open('data/categories/' + each_file, 'r')
            all_lines = file.readlines()
            user_cnt = {}
            business_cnt = {}
            for node in all_lines:
                data = json.loads(node)
                if data['user_id'] not in user_cnt:
                    user_cnt[data['user_id']] = 1
                else:
                    user_cnt[data['user_id']] += 1
                if data['business_id'] not in business_cnt:
                    business_cnt[data['business_id']] = 1
                else:
                    business_cnt[data['business_id']] += 1

            if check_user(user_cnt) and check_business(business_cnt):
                print "HERE", each_file
                break
            # print user_cnt
            # print business_cnt
            file.close()
        print len(user_cnt), len(business_cnt)
    # print user_cnt, business_cnt
    # cnt = {}
    # for item in user_cnt:
    #     if user_cnt[item] not in cnt:
    #         cnt[user_cnt[item]] = 1
    #     else:
    #         cnt[user_cnt[item]] += 1
    # print cnt


remove_reviews()


