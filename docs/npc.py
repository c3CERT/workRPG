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
                'comment': 'This is for internal documentation only. Session variables are globally available for all NPCs. You may want to prefix them for indiviual NPCs',
                'options': [
                    {'text': 'Tell me more...', 'action': 'dialog', 'payload': 'more'},
                    {'text': 'The website?', 'action': 'url', 'payload': 'https://cert.ccc.de/'},
                    {'text': 'Prompting for name', 'action': 'prompt', 'payload': {'var':'name', 'next': 'more'}},
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
