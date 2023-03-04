def check_line_length(line, line_number):
    if len(line) > 79:
        print(f'Line {line_number}: S001 Too Long')


class StaticCodeAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        with open(self.filename, 'r') as file:
            for number, line in enumerate(file, 1):
                check_line_length(line, number)


scan = StaticCodeAnalyzer(input())
scan.run()
