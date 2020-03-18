import json
from urllib.parse import parse_qs
import logging

from wrt_agenda_command import handle_agenda_command, post_the_agenda, clear_all_items
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        if type(event) == str:
            params = parse_qs(json.loads(event)['body'])
        else:
            params = parse_qs(event['body'])
    except Exception as e:
        params = f'err: {e}'
    try:
        if type(event) == str:
            params = parse_qs(json.loads(event)['body'])
        else:
            params = parse_qs(event['body'])
    except:
        logger.error('couldn\'t parse event{}'.format(event))
        logger.error('error when parsing event["body"]')
        return respond(None, "couldn't parse input")
    try:
        user = params['user_id'][0]
    except:
        logger.error('couldn\'t parse event{}'.format(event))
        logger.error('error when parsing user_id')
        return respond(None, "couldn't parse input")
    try:
        user_name = params['user_name'][0]
    except:
        logger.error('couldn\'t parse event{}'.format(event))
        logger.error('error when parsing user_name')
        return respond(None, "couldn't parse input")
    try:
        command = params['command'][0]
    except:
        logger.error('couldn\'t parse event{}'.format(event))
        logger.error('error when parsing command')
        return respond(None, "couldn't parse input")
    try:
        team_domain = params['team_domain'][0]
    except:
        logger.error('couldn\'t parse event{}'.format(event))
        logger.error('error when parsing team_domain')
        return respond(None, "couldn't parse input")
    try:
        text = ""
        if "text" in params:
            text = params['text'][0]
        logger.info('%s (id %s) sent command %s to domain %s with text %s' % (user_name, user, command, team_domain, text))
    except:
        logger.error('couldn\'t parse event{}'.format(event))
        logger.error('error when parsing text')
        return respond(None, "couldn't parse input")
    
    logger.info(f'command={command}')
    
    if command == '/agenda':
        return handle_agenda_command(user, user_name, text, team_domain)

    return {
        'statusCode': 200,
        'body': json.dumps(f'command: {command}, text: {text}')
    }
