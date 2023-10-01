import csv
import os.path


def read_csv(name: str = 'Corp_Summary.csv') -> list[list[str, str, str, str, float, int]]:
    """
    Reads csv file and return list of workers with 
    name(str), department(str), team(str), 
    position(str), rating(flaot), salary(int)
    """
    result = []
    with open(name, 'r', encoding='utf-8') as file:
        csv_iter = csv.reader(file, delimiter=';', )
        next(csv_iter)
        for line in csv_iter:
            result.append([line[i] for i in range(4)] +
                          [float(line[4]), int(line[5])])
    return result


def create_report(workers: list[list[str, str, str, str, float, int]]) -> None:
    """
    Creates report of departments:
    name, amount of workers, salary fork, average salary
    """
    global report
    departments: dict[str, list[int, int, int, float]] = dict()
    # departments: dict[name, list[amount of workers, min salary, max salary, sum of salaries]]
    for worker in workers:
        department, team, position, salary = *worker[1:4], worker[-1]
        if department not in departments:
            departments[department] = [1] + [salary] * 3
        else:
            departments[department][0] += 1
            departments[department][1] = min(
                departments[department][1], salary)
            departments[department][2] = max(
                departments[department][2], salary)
            departments[department][3] += salary

    for department in departments:
        report.append([department, departments[department][0],
                       f'{departments[department][1]}-'
                       f'{departments[department][2]}',
                       str(round(departments[department][3] / departments[department][0], 2))])


def print_hierarchy(workers: list[list[str, str, str, str, float, int]]) -> None:
    """Prints hierarchy of teams using list of workers"""
    departments: dict[str, list[str]] = dict()
    for worker in workers:
        department, team = worker[1], worker[2]
        if department in departments:
            if team not in departments[department]:
                departments[department].append(team)
        else:
            departments[department] = [team]

    for department in departments:
        print(department + ':', *departments[department], sep='\n   ')
        print()


def print_report() -> None:
    """
    Prints report of departments:
    name, amount of workers, salary fork, average salary
    """
    global data, report
    if report == []:
        create_report(data)
    for line in report:
        print(line[0] + ':',
              f'amount of workers: {line[1]}',
              f'salary fork: {line[2]}',
              f'average salary: {line[3]}',
              sep='\n   ')
        print()


def save_report(name: str = 'report.csv') -> None:
    """Saves report in csv file"""
    global report, data
    if report == []:
        create_report(data)
    with open(name, 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerow(['Name', 'amount of workers',
                           'salary fork', 'average salary', ])
        for line in report:
            csvwriter.writerow(line)


def ask_path() -> str:
    print('Do you want to use file "Corp_Summary.csv" or '
          'you want to use other file?')
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Choose: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return 'Corp_Summary.csv'
    else:
        path = ''
        while True:
            path = input('Write path to a file: ')
            if os.path.exists(path):
                break
            else:
                print('This path doesn\'t exists')
        return path


if __name__ == '__main__':

    data = read_csv(ask_path())
    report = []

    print('Available commands:')
    print('1: Print hierarchy')
    print('2: Print report')
    print('3: Save report to csv file')
    print('4: Exit')
    while True:
        try:
            command = int(input('Type the number of a command: '))
            match command:
                case 1:
                    print_hierarchy(data)
                case 2:
                    print_report()
                case 3:
                    save_report()
                case 4:
                    print('Goodbye!')
                    break
                case _:
                    print('Unknow command. Try again, please.')

        except ValueError as e:
            print('Unknow command. Try again, please.')
