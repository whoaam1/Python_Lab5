import re

patterns = {
    r'\[22\/Mar\/2009:2[2-3]:[0-5][0-9]:\d{2} [+-]\d{4}] "GET .*" 4\d\d ',
    r'\[23\/Mar\/2009:\d{2}:\d{2}:\d{2} [+-]\d{4}] "GET .*" 4\d\d ',
    r'\[24\/Mar\/2009:0[0-3]:[0-5][0-9]:\d{2} [+-]\d{4}] "GET .*" 4\d\d '
}


def count_logs():
    results = {}
    with open('logs.txt') as log_file:

        for row in log_file:
            row = row.replace('\n', '')

            for pattern in patterns:
                match = re.search(pattern, row)
                if not match:
                    continue
                status = match.group()
                if status is None:
                    continue
                if status not in results:
                    results[status] = 0
                results[status] += 1
                break
    return results


def main():
    found_lines = count_logs()

    for elements in found_lines:
        print(elements)
    print('The total number of unsuccessful requests: ', len(found_lines))


if __name__ == '__main__':
    main()
