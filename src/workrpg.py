import json

from flask import Flask
from flask import url_for, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route('/npc/<name>')
def get_npc(name):
    # look for a matching npc and redirect to start dialog
    try:
        name = name.replace('../', '')
        with open('npcs/' + name + '.json') as npcFile:
            npc = json.load(npcFile)

        return redirect(url_for('.get_npc_dialog', name=name, dialog=npc['start_dialog']))
    except:
        abort(404)


@app.route('/npc/<name>/<dialog>')
def get_npc_dialog(name, dialog):
    # look for a matching npc and dialog
    try:
        name = name.replace('../', '')
        with open('npcs/' + name + '.json') as npcFile:
            npc = json.load(npcFile)

        return 'NPC %s said: %s' % (npc['name'], npc['dialogs'][dialog]['text'])
    except:
        abort(404)
