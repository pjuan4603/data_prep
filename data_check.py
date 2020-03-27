# Brian Juan / Feb 2020


def retrieve_data():
    # all_files = ['source_final_trimmed.txt', 'target_final_trimmed.txt']
    all_files = ['test_source.txt', 'test_target.txt']
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


def get_user_count(data):
    user_list = []
    count = 0
    for review in data:
        if review[0] not in user_list:
            user_list.append(review[0])
            count += 1

    return count


def main():

    source, target = retrieve_data()
    print get_user_count(source)
    print get_user_count(target)


main()