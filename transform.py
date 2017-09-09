import sqlite3
import json


def fetch_data(file):
    with open(file) as json_data:
        return json.load(json_data)


def process_data(data):
    try:
        conn = sqlite3.connect('efl.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS assessmentResponse ('
                  'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                  'questionCode VARCHAR(104), '
                  'questionResponse VARCHAR(104), '
                  'section VARCHAR(104), '
                  'timeElapsed SMALLINT, '
                  'viewsCount SMALLINT, '
                  'responseSequence VARCHAR(104))')

        query_str = 'INSERT INTO assessmentResponse (' \
                    'questionCode, ' \
                    'questionResponse, ' \
                    'section, ' \
                    'timeElapsed, ' \
                    'viewsCount, ' \
                    'responseSequence) VALUES (?,?,?,?,?,?)'

        for item in data:
            question_response = time_elapsed = views_count = response_sequence = None
            section = item['step']
            observations = item['observations']
            for key in observations.keys():
                question_code = key
                if 'responseSequence' in observations[key]:
                    response_sequence = str(observations[key]['responseSequence'])
                if 'responseValue' in observations[key]:
                    question_response = observations[key]['responseValue']
                if 'timeElapsed' in observations[key]:
                    time_elapsed = int(observations[key]['timeElapsed'])
                if 'viewCount' in observations[key]:
                    views_count = int(observations[key]['viewCount'])

                c.execute(query_str, (question_code, question_response, section, time_elapsed,
                                      views_count, response_sequence))
                conn.commit()

            question_response = time_elapsed = response_sequence = None
            for meta in item['metas'].items():
                if 'timeElapsed' in meta:
                    time_elapsed = meta[1]
                if 'viewCount' in meta:
                    views_count = meta[1]
                    c.execute(query_str, ('_' + section, question_response, section, time_elapsed,
                                          views_count, response_sequence))
                    conn.commit()
    finally:
        conn.close()


def get_rows():
    conn = sqlite3.connect('efl.db')
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assessmentResponse")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    finally:
        conn.close()


if __name__ == '__main__':
    data = fetch_data('payload.json')
    process_data(data)
    get_rows()  # Optional
