from utils import sort_by_date, json_reader, output_data

if __name__ == '__main__':

    for operation in range(5):

        data = sort_by_date(json_reader('../operations.json'))
        print(output_data(data[operation]))
