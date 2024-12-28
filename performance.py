import gsheetsExample as gs
from datetime import datetime as dt

from gsheetsExample import gSheetsRead

vocabular = {'Первое практическое занятие по Python': 'Первая методичка',
            'Нулевое практическое занятие по Python': 'Нулевая методичка',
            'Второе практическое занятие по Python': 'Вторая методичка',
            'Третье практическое занятие по Python': 'Третья методичка',
            'Четвёртое практическое занятие по Python': 'Четвёртая методичка',
            'Упражнение 1': 'Упражнение 1',
            'Упражнение 2': 'Упражнение 2',
            'Упражнение 3': 'Упражнение 3',
            'Упражнение 4': 'Упражнение 4',
            'Упражнение 5': 'Упражнение 5',
            'Упражнение 6': 'Упражнение 6',
            'Упражнение 7': 'Упражнение 7',
            'Упражнение 8': 'Упражнение 8',
            'Упражнение 9': 'Упражнение 9',
            'Упражнение 10': 'Упражнение 10'}

def agregateData(tries, row):
    tries['question'] = row['question']
    tries['step'] = str(abs(int(row['step'])))
    tries['status'] = row['status']
    tries['time'] = row['time']
    tries['attempt_id'] = row['attempt_id']
    tries['question_usage_id'] = row['question_usage_id']

def main():
    data = gs.gSheetsRead(gs.table, 'Data', start_row=1)
    performance = gs.gSheetsRead(gs.table, 'PerformanceSaturday')
    # for row in performance:
    #     print(row)
    # for row in data:
    #     print(row)
    #     break
    for st in performance:
        tries = {}
        for row in data:
            if row['FIO'] == st['FIO']:
                test_name_Q = row['test_name']+';;'+row['question']
                if not test_name_Q in tries:
                    tries[test_name_Q] = {'question' : '0',
                                            'step' : '0',
                                            'status' : '',
                                            'time' : '0',
                                            'attempt_id' : '0',
                                            'question_usage_id' : '0'}
                    agregateData(tries[test_name_Q], row)
                if tries[test_name_Q]['status'] != 'complete':
                    agregateData(tries[test_name_Q], row)
        res = {}
        for key, val in tries.items():
            test_name = key.split(';;')[0]
            if not test_name in res:
                res[test_name] = { 'res' : [],
                                    'question' : '0',
                                    'step' : '0',
                                    'status' : '',
                                    'time' : '0',
                                    'attempt_id' : '0',
                                    'question_usage_id' : '0'}
            if val['status'] != 'complete':
                agregateData(res[test_name], val)
                res[test_name]['res'] += [val['question']+'.'+val['step']]
        for test_name, val in res.items():
            if len(val['res'])>0:
                st[vocabular[test_name]] = f'=ГИПЕРССЫЛКА("https://moodle.surgu.ru/mod/quiz/review.php?attempt={val['attempt_id']}#question-{val['question_usage_id']}-{val['question']}"; "{', '.join(val['res'])}")'
            else:
                st[vocabular[test_name]] = "'+"
    gs.gSheetsUpdate(gs.table, 'PerformanceSaturday', performance, start_row = 3)


if __name__ == '__main__':
    main()