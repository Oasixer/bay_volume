import json
from urlparse import parse_qs

def lambda_handler(event, context):
    # TODO implement
    try:
        if type(event) == str:
            params = parse_qs(json.loads(event)['body'])
        else:
            params = parse_qs(event['body'])
    except:
        params = 'heck'
    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from Lambda!{params}')
    }
