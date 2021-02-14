# Example Structure of a npc.
import json

npc = {
    'version': 1,
    'name': 'Mr. Ex Ample',
    'image': 'imgs/npcs/ex_ample.png',
    'start_dialog': 'start',
    'dialogs':
        {
            'start': {
                'text': 'lorem ipsum',
                'img': 'imgs/npcs/ex_ample_speaking.png',
                'audio': 'audio/npcs/ex_ample_start.mp3',
                'comment': 'This is for internal documentation only.',
                'options': [
                    {'text': 'Tell me more...', 'action': 'dialog', 'payload': 'more'},
                    {'text': 'The website?', 'action': 'url', 'payload': 'https://cert.ccc.de/'}
                ]
            },
            'more': {
                'text': 'lorem ipsum einhorn',
                'img': 'imgs/npcs/ex_ample_speaking1.png',
                'audio': None,
                'options': [
                ]
            }
        }
}

with open('npc.json', 'w') as f:
    json.dump(npc, f, indent=4)
