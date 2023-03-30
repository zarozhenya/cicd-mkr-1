def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            string_data = line.strip().split(', ')
            string_data[1] = int(string_data[1])
            string_data[2] = int(string_data[2])
            data.append(string_data)
    return data


def sort_by_population(data, descending_order=False):
    return sorted(data, key=lambda x: x[2], reverse=descending_order)


def sort_by_area(data, descending_order=False):
    return sorted(data, key=lambda x: x[1], reverse=descending_order)


def pretty_print_the_data(data):
    counter = 1
    for item in data:
        print(f'\nCountry {counter}')
        print(f'Name: {item[0]}\nArea: {item[1]}\nPopulation: {item[2]}\n')
        counter += 1


if __name__ == '__main__':
    data_from_file = read_data_from_file('data.txt')
    print('Read data from file\n==========')
    pretty_print_the_data(data_from_file)
    sorted_data_by_population = sort_by_population(data_from_file, True)
    print('Sorted data from file by population\n==========')
    pretty_print_the_data(sorted_data_by_population)
    sorted_data_by_area = sort_by_area(data_from_file, True)
    print('Sorted data from file by area\n==========')
    pretty_print_the_data(sorted_data_by_area)
