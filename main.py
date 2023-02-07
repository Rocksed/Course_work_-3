from function import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    OPERATION_JSON = "https://www.jsonkeeper.com/b/EAVG"
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5
    data, info = get_data(OPERATION_JSON)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filtered_data(data, filtered_empty_from=FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    print("INFO: Вывод данных:")
    for row in data:
        print(row, end='\n\n')


if __name__ == '__main__':
    main()
