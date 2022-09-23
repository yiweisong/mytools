from curses.ascii import isdigit
from decorator import (receive_args, handle_application_exception)

READ_LIMIT = 1000
HEX_FORMAT = 16
JOIN_INDICATOR = ','
SPLIT_INDICATOR = ','
NEW_LINE = '\n'


@handle_application_exception
@receive_args
def main(**kwargs):
    options = kwargs['options']
    if not options.input_file:
        raise Exception('Please set -i argument')

    if not options.output_file:
        options.output_file = 'output.txt'

    match_count = 0
    write_line = []

    write_file = open(options.output_file, 'w')

    with open(options.input_file, 'r') as read_file:
        while True:
            lines = read_file.readlines(READ_LIMIT)
            values = [x.split(SPLIT_INDICATOR)[2].replace(
                NEW_LINE, '') for x in lines]
            for value in values:
                try:
                    try_hex = int(value, HEX_FORMAT)
                    if try_hex < 0x8000:
                        match_count += 1
                        write_line.append(value)

                    if len(write_line) == 16:
                        write_file.write('{0}{1}'.format(
                            JOIN_INDICATOR.join(write_line), NEW_LINE))
                        write_line = []
                        pass
                except:
                    continue

            if len(lines) == 0:
                break

    write_file.close()
    print('done')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
