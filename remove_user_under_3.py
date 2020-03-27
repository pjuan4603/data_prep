# Brian Juan / Feb 2020


def retrieve_data():
    all_files = ['source_business_trimmed.txt', 'target_business_trimmed.txt']
    source = []
    target = []
    for each_file in all_files:

        file_name = each_file.split('.')[0]
        f = open(each_file, 'r')
        all_lines = f.readlines()

        for line in all_lines:

            tokens = line.split(',')
            tokens[2] = tokens[2].splitlines()[0]
            # tokens = line.split('   ')
            # tokens[2] = tokens[2].splitlines()[0].split(' ')[1]
            # print 'user:' + tokens[0] + '\tbusiness:' + tokens[1] + '\tratings:' + tokens[2]

            if file_name.__contains__('source'):
                source.append(tokens)
            else:
                target.append(tokens)

    return source, target


def user_more_3(data):

    user_list = []
    aggre = {}
    for review in data:

        if review[0] in aggre:
            aggre[review[0]] += 1
        else:
            aggre[review[0]] = 1

    for key in aggre.keys():
        if aggre.get(key) > 3:
            user_list.append(key)

    return user_list


def shared(source, target):
    user_list = []

    for user in source:
        if user in target:
            user_list.append(user)

    return user_list


def generate_output(data, shared_user, file_name):

    reviews = []
    for review in data:
        if review[0] in shared_user:
            reviews.append([int(review[0]), int(review[1]), int(review[2])])

    print reviews
    with open(file_name + '.txt', 'w') as f:
        for review in reviews:
            print 'writing' + str(review[0]) + ',' + str(review[1]) + ',' + str(review[2])
            f.write(str(review[0]) + ',' + str(review[1]) + ',' + str(review[2]) + '\n')


def main():
    source, target = retrieve_data()
    source_user_list = user_more_3(source)
    target_user_list = user_more_3(target)
    shared_users = shared(source_user_list, target_user_list)
    generate_output(source, shared_users, 'source_final_trimmed')
    generate_output(target, shared_users, 'target_final_trimmed')


main()