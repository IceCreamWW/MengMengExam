import sys, os
import csv
sys.path.append(os.path.abspath('../'))
os.environ["DJANGO_SETTINGS_MODULE"] = "MengMeng.settings"
import django
django.setup()
from study.models import *

with open('../data/questions.csv') as fp:
    reader = csv.DictReader(fp)
    for question in reader:
        question_text = question["content"]
        answer = question['answer'].strip()

        if question['type'] == '单选题':
            choices='{c1}\n{c2}\n{c3}\n{c4}'.format(**question)
            answer = ord(answer) - ord('A')
            SingleChoice(question_text=question_text, question_type='SingleChoice', choices=choices, answer=answer).save()

        elif question['type'] == '多选题':
            choices='{c1}\n{c2}\n{c3}\n{c4}'.format(**question)
            answer = ','.join([chr(ord(ans) - ord('A') + ord('0')) for ans in answer])
            MultipleChoice(question_text=question_text, answer=answer).save()

        elif question['type'] == '填空题':
            FillInBlank(question_text=question_text, answer=answer).save()

        elif question['type'] == '判断题':
            answer = True if answer == 'Y' else False
            TrueOrFalse(question_text=question_text, answer=answer).save()

        elif question['type'] == '简答题':
            ShortAnswerQuestion(question_text=question_text, answer=answer).save()

        else:
            raise RuntimeError('question type does not exist: {}'.format(question['type']))

