def retrieve_data():
    all_files = ['source_final_trimmed.txt', 'target_final_trimmed.txt']
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


def rename(data):

    user_dict = {}
    bus_dict = {}
    user_index = 1
    business_index = 1

    for review in data:
        if review[0] in user_dict:
            review[0] = user_dict.get(review[0])
        else:
            user_dict[review[0]] = user_index
            review[0] = user_index
            user_index += 1

        if review[1] in bus_dict:
            review[1] = bus_dict.get(review[1])
        else:
            bus_dict[review[1]] = business_index
            review[1] = business_index
            business_index += 1

    print 'User: \t' + str(user_index-1) + '\tBus:\t' + str(business_index-1)
    return data


def generate_output(reviews, file_name):

    with open(file_name + '.txt', 'w') as f:
        for review in reviews:
            #print 'writing' + str(review[0]) + ',' + str(review[1]) + ',' + str(review[2])
            f.write(str(review[0]) + ',' + str(review[1]) + ',' + str(review[2]) + '\n')


def main():
    source, target = retrieve_data()
    target = rename(target)
    source = rename(source)

    generate_output(target, 'test_target')
    generate_output(source, 'test_source')


main()