import utils

if __name__ == '__main__':

    for operation in range(5):

        data = utils.sort_by_date(utils.json_reader('../operations.json'))
        print(utils.output_data(data[operation]))
