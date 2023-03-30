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


if __name__ == '__main__':
    data_from_file = read_data_from_file('data.txt')
    print(data_from_file)
    sorted_data_by_population = sort_by_population(data_from_file, True)
    print(sorted_data_by_population)

