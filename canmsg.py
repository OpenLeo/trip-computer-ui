from datetime import datetime

from events import events
evt = events()

def handler_0F6(data):
    temperature = (int.from_bytes(data[5:6], 'big')/2)-40
    evt.addEvent({'type': 'temperature', 'value': '{}º'.format(temperature)})

def handler_1A1(data):
    from messages import messages
    command = int.from_bytes(data[0:1], 'big')
    msg_id = int.from_bytes(data[1:2], 'big')
    if command == 0x80 and msg_id in messages:
        value = {'show': True, 'msg_id': msg_id, 'text': messages[msg_id]}
    elif command == 0x80:
        value = {'show': True, 'msg_id': msg_id, 'text': '(message not found)'}
    elif command == 0x7F:
        value = {'show': False, 'msg_id': msg_id, 'text': messages[msg_id]}
    else:
        return
    evt.addEvent({'type': 'messages', 'value': value})

def handler_1A5(data):
    show = not (int.from_bytes(data[0:1], 'big') & 0b11100000)
    volume = int.from_bytes(data[0:1], 'big') & 0b00011111
    value = {'show': show, 'volume': volume}
    evt.addEvent({'type': 'volume', 'value': value})
    evt.addEvent({'type': 'time', 'value': datetime.now().strftime("%a %d %B - %H:%M")})

def handler_221(data):
    if data[2:4] == 0xFF:
        consumption = 0
    else:
        consumption = int.from_bytes(data[1:3], 'big')/10

    if data[6:8] == 0xFF:
        autonomy = 0
    else:
        autonomy = int.from_bytes(data[3:5], 'big')
    evt.addEvent({'type': 'conso', 'value': '{0:.1f}l/100'.format(consumption)})
    evt.addEvent({'type': 'autonomy', 'value': '{} km'.format(autonomy)})

frames = {
    0x0F6: handler_0F6,
    0x1A1: handler_1A1,
    0x1A5: handler_1A5,
    0x221: handler_221
}
