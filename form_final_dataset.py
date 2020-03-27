# Brian Juan / Feb 2020
# Functionality: Reindex the users and businesses
# Input Files:
# Output Files:
import json


# Retrieve data from the given file name
# Input: A list of two file names
# Returns: Two list that contains source/target domain data
def retrieve_data(all_files):

    source = []
    target = []
    for each_file in all_files:

        file_name = each_file.split('.')[0]
        # print file_name

        f = open(each_file, 'r')
        all_lines = f.readlines()

        for line in all_lines:

            tokens = line.split(',')
            tokens[2] = tokens[2].splitlines()[0]
            print 'user:' + tokens[0] + '\tbusiness:' + tokens[1] + '\tratings:' + tokens[2]

            review = []
            review.append(int(tokens[0]))
            review.append(int(tokens[1]))
            review.append(int(tokens[2]))

            if file_name.__contains__('source'):
                source.append(review)
            else:
                target.append(review)

    return source, target


# Count the number of users in the desired data set
# Input: The list that needs to be counted
# Returns: Amount of users
def get_user_count(data):
    user_list = []
    count = 0
    for review in data:
        if review[0] not in user_list:
            user_list.append(review[0])
            count += 1

    return count


# Count the number of businesses in the desired data set
# Input: The list that needs to be counted
# Returns: Amount of business
def get_business_count(data):
    business_list = []
    count = 0
    for review in data:
        if review[1] not in business_list:
            business_list.append(review[1])
            count += 1

    return count


# Count the number of reviews in the desired data set
# Input: The list that needs to be counted
# Returns: Amount of business
def get_review_count(data):
    return len(data)


# Separate the data 4/5 used for training and the rest for testing from a single user.
# Input: A review list for a single user
# Returns: Two lists - one for training and one for testing
def form_train_test(review_list):
    train = []
    test = []

    count = len(review_list)
    if count == 0:
        return train, test
    elif count < 5:
        test_amount = 1
        train_amount = count - test_amount
    else:
        test_amount = count/5
        train_amount = count - test_amount

    # print 'Count = ' + str(count) + '\tCount/5 = ' + str((count/5)) + '\tTrAmount= ' + str(train_amount) + '\tTeAmount = ' + str(test_amount)

    for i in range(0, train_amount):
        train.append(review_list[i])
    for i in range(train_amount, train_amount + test_amount):
        test.append(review_list[i])

    # print 'Count: ' + str(count) + '\tTrain: ' + str(len(train)) + '\tTest: ' + str(len(test))
    return train, test


# Form the complete training and testing data sets
# Input: Data from both domains
# Returns: Two data set - one for training anf one for testing
def divide_train_test(source, target):
    train = []
    test = []

    last_user = ''
    review_list = []
    for review in source:
        current_user = review[0]

        if current_user == last_user:
            review_list.append(review)
        else:
            train_temp, test_temp = form_train_test(review_list)
            review_list = []

            if len(train_temp) is not 0:
                for train_example in train_temp:
                    train.append([train_example[0], train_example[1], train_example[2], 0, 0])
                for test_example in test_temp:
                    test.append([test_example[0], test_example[1], test_example[2], 0, 0])

            last_user = current_user
            review_list.append(review)

    last_user = ''
    review_list = []
    for review in target:
        current_user = review[0]

        if current_user == last_user:
            review_list.append(review)
        else:
            train_temp, test_temp = form_train_test(review_list)
            review_list = []

            if len(train_temp) is not 0:
                for train_example in train_temp:
                    train.append([train_example[0], train_example[1], train_example[2], 0, 1])
                for test_example in test_temp:
                    test.append([test_example[0], test_example[1], test_example[2], 0, 1])

            last_user = current_user
            review_list.append(review)

    return train, test


# Generate a JSON output that matches the format of converting JSON to the MAT files
def generate_json_output(user_count, source_count, target_count, train, test):
    print 'generate output'

    data = {}
    data['num_users'] = int(user_count)
    data['num_attempts'] = int(20)
    data['num_quizs'] = int(source_count)
    data['num_disicussions'] = int(target_count)
    print 'User: ' + str(user_count) + '\tSBusCount: ' + str(source_count) + '\tTBusCount: ' + str(target_count)
    data['train'] = train
    data['test'] = test
    data['cross_train'] = []
    data['cross_test'] = []

    with open('data.json', 'w') as f:
        json.dump(data, f)


def main():

    """ YOU CAN CHANGE THE INPUT FILE NAME HERE IN all_files """
    all_files = ['renamed_source.txt', 'renamed_target.txt']
    source, target = retrieve_data(all_files)
    user_count = get_user_count(target)
    source_count = get_business_count(source)
    target_count = get_business_count(target)
    print 'User count: ' + str(user_count) + '\tSourceD review count: ' + str(source_count) + '\tTargetD review count: ' + str(target_count)

    train, test = divide_train_test(source, target)
    print 'Train: ' + str(len(train)) + '\tTest: ' + str(len(test))

    generate_json_output(user_count, source_count, target_count, train, test)
    print 'Done.'


main()