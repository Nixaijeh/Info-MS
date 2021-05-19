import json
import pickle

from 实验一.blockchain import
from 实验一.blockchain import


def on_message(self, message):
    elif message['op'] == 'pool':
    self.write_message(json.dumps({
        'status': 200,
        'error': 'OK',
        'response': {
            'pool': [json.loads(str(i)) for i in list(pickle.loads(db.get('pool')))]
        }
    }))

    elif message
    ['op'] == 'merge'
    :
    if
        'args' in message and 'pool' in message
    [
        'args
        '
    ]
    :
    pool = pickle.loads
    (db.get
     ('pool'))
    for
        i in message
    [
        'args
        ']['pool'
    ]
    :
    pool.add
    (Transaction
        (
        sender
        =
        i
        ['sender'],
        receiver
        =
        i
        ['receiver'],
        amount
        =
        i
        ['amount'
        ]
    ))
    db.set
    ('pool', pickle.dumps(pool))
