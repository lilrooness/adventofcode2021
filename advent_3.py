from abc import abstractproperty
from collections import defaultdict

def get_int_column(data, col_n):
    column = []

    for row in data:
        column.append(int(row[col_n]))
    
    return column

def get_significant_value(values, most_common=True, tie_breaker=1):
    counts = defaultdict(lambda : 0)

    for v in values:
        counts[v] += 1
    
    if len(set(counts.values())) == 1 and len(counts.values()) > 1:
        return tie_breaker

    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=most_common)
    return sorted_items[0][0]

def get_power_consumption(data):

    most_common_values = []
    least_common_values = []

    for x in range(len(data[0])):
        column = get_int_column(data, x)
        most_common_values.append(get_significant_value(column, most_common=True))
        least_common_values.append(get_significant_value(column, most_common=False))

    gamma = int("".join([str(x) for x in most_common_values]), 2)
    sigma = int("".join([str(x) for x in least_common_values]), 2)

    return gamma * sigma

def get_life_support_rating(data):
    oxygen_rating = get_rating(data, most_common_wins=True, tie_breaker=1)
    co2_rating = get_rating(data, most_common_wins=False, tie_breaker=0)

    return int(oxygen_rating, 2) * int(co2_rating, 2)

def get_rating(data, column_position=0, most_common_wins=True, tie_breaker=1):
    column = get_int_column(data, column_position)

    most_significant_value = get_significant_value(column, most_common=most_common_wins, tie_breaker=tie_breaker)

    matching_rows = select_matching_rows_by_column(data, column_position, most_significant_value)
    if len(matching_rows) == 1:
        return_value = matching_rows[0]
        return return_value
    else:
        return get_rating(matching_rows, column_position+1, most_common_wins=most_common_wins, tie_breaker=tie_breaker)
    
def select_matching_rows_by_column(data, column_position, filter_value):
    matching = []
    for row in data:
        if row[column_position] == str(filter_value):
            matching.append(row)
    
    return matching


def test_1():
    data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    power_consumption = get_power_consumption(data)
    assert 198 == power_consumption

    oxygen_rating = get_rating(data, most_common_wins=True, tie_breaker=1)
    print("oxygen_rating: {}".format(oxygen_rating))
    assert '10111' == oxygen_rating

    co2_rating = get_rating(data, most_common_wins=False, tie_breaker=0)
    print("co2_rating: {}".format(co2_rating))
    assert '01010' == co2_rating

    life_support_rating = get_life_support_rating(data)
    assert 230 == life_support_rating

if __name__ == "__main__":
    test_1()
    print("tests passed")
    data = []
    with open("input_3") as file:
        for line in file.readlines():
            data.append(line.strip())

    # power_consumption = get_power_consumption(data)
    life_support_rating = get_life_support_rating(data)
    print(life_support_rating)

