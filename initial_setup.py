from datetime import datetime, timedelta

content = """---
title: Week {week}: {week_topic}
ref: 'week-{week}'
---

{tues_date}
: **Lecture**{{: .label .label-lecture }} {tues_topic}

{thurs_date}
: **Lecture**{{: .label .label-lecture }} {thurs_topic}
"""


def do_stuff():
    week_topics = [
        'Introductions', 'Decisions I', 'Decisions II',
        'Bayesian Modeling I', 'Bayesian Modeling II',
        'GLMs I', 'GLMs II', 'Nonparametric Methods',
        'Causal Inference I', 'Causal Inference II',
        'Bandits', 'Reinforcement Learning I',
        'Reinforcement Learning II', 'Privacy', 'Wrapup'
    ]
    with open('lecture_names.txt') as f:
        lecture_topics = [line.strip() for line in f.readlines()]
    current = datetime(2024, 8, 27)
    midterms = [datetime(2024, 10, 8), datetime(2024, 11, 14)]
    holidays = [datetime(2024, 11, 28)]
    midterm_number = 1
    for week, week_topic in enumerate(week_topics, 1):

        tues = current
        thurs = current + timedelta(2)

        week_params = {
            'week': week,
            'week_topic': week_topic,
            'tues_date': tues.strftime('%b %-d'),
            'thurs_date': thurs.strftime('%b %-d'),
        }
        for lec_date, day in [
            (tues, 'tues'), (thurs, 'thurs')
        ]:
            if lec_date in holidays:
                topic = 'Holiday'
            elif lec_date in midterms:
                topic = f'Midterm {midterm_number}'
                midterm_number += 1
            else:
                topic = lecture_topics.pop(0)
            week_params[f'{day}_topic'] = topic
        write_week(week, week_params)
        current += timedelta(days=7)


def write_week(week, week_params):
    with open(f'_modules/week-{week:02d}.md', 'w') as f:
        f.write(content.format(**week_params))


if __name__ == '__main__':
    do_stuff()
