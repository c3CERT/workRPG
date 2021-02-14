import json

import markdown
from flask import Flask
from flask import url_for, redirect, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route('/npc/<path:name>')
def get_npc(name):
    # look for a matching npc and redirect to start dialog
    try:
        name = name.replace('..', '')
        with open('npcs/' + name + '.json') as npcFile:
            npc = json.load(npcFile)

        return redirect(url_for('.get_npc_dialog', name=name, dialog=npc['start_dialog']))
    except:
        abort(404)


@app.route('/npc/<path:name>/<string:dialog>')
def get_npc_dialog(name, dialog):
    # look for a matching npc and dialog
    try:
        name = name.replace('../', '')
        with open('npcs/' + name + '.json') as npcFile:
            npc = json.load(npcFile)
            dialog = npc['dialogs'][dialog]
            dialog['text'] = markdown.markdown(dialog['text'])
            for option in dialog['options']:
                option['text'] = markdown.markdown(option['text'])
                if option['action'] == "dialog":
                    option['url'] = url_for('.get_npc_dialog', name=name, dialog=option['payload'])

        return render_template('dialog.html', npc=npc, dialog=dialog)
    except:
        abort(404)
