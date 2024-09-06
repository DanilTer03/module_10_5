import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start_time = datetime.datetime.now()
# for file_name in filenames:
#     data = read_info(file_name)
# end_time = datetime.datetime.now()
# print(f" {end_time - start_time} (линейный)")
#
# Многопроцессный
if __name__ == "__main__":
    start_time = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    print(f"{end_time - start_time} (многопроцессный)")
