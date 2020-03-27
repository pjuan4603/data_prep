# Brian Juan / Feb 2020


def retrieve_data():
    all_files = ['source.txt', 'target.txt']
    source = []
    target = []
    for each_file in all_files:

        file_name = each_file.split('.')[0]
        f = open(each_file, 'r')
        all_lines = f.readlines()

        for line in all_lines:

            tokens = line.split('   ')
            tokens[2] = tokens[2].splitlines()[0].split(' ')[1]
            # tokens = line.split(',')
            # tokens[2] = tokens[2].splitlines()[0]
            print 'user:' + tokens[0] + '\tbusiness:' + tokens[1] + '\tratings:' + tokens[2]

            if file_name.__contains__('source'):
                source.append(tokens)
            else:
                target.append(tokens)

    return source, target


def bus_more_3(data):

    bus_list = []
    aggre = {}
    for review in data:

        if review[1] in aggre:
            aggre[review[1]] += 1
        else:
            aggre[review[1]] = 1

    for key in aggre.keys():
        if aggre.get(key) > 3:
            bus_list.append(key)

    return bus_list


def generate_output(data, shared_business, file_name):

    reviews = []
    for review in data:
        if review[1] in shared_business:
            reviews.append([int(review[0]), int(review[1]), int(review[2])])

    print reviews
    with open(file_name + '.txt', 'w') as f:
        for review in reviews:
            print 'writing' + str(review[0]) + ',' + str(review[1]) + ',' + str(review[2])
            f.write(str(review[0]) + ',' + str(review[1]) + ',' + str(review[2]) + '\n')


def main():
    source, target = retrieve_data()
    source_bus_list = bus_more_3(source)
    target_bus_list = bus_more_3(target)
    generate_output(source, source_bus_list, 'source_business_trimmed')
    generate_output(target, target_bus_list, 'target_business_trimmed')


main()