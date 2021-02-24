import json
import re
import markdown
from flask import Flask
from flask import url_for, redirect, render_template
from flask import session, request
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = b'Ahdeekeiphahthoh2ohBie8Tee5lijai'

def recursive_lookup(k, d: dict) -> list:
    if k in d: return d[k]
    for v in d.values():
        if isinstance(v, dict):
            a = recursive_lookup(k, v)
            if a is not None: return a
    return []

def replace_placeholders(text: str) -> str:
    print("replace vars")
    p = re.compile('\[(\w+)\]')
    for var in p.findall(text):
        try:
            print("try replacing %s" % var)
            text = text.replace('[%s]' % var, session[var])
        except TypeError:
            pass
    return text

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


@app.route('/npc/<path:name>/prompt/<string:var>', methods=['POST',])
def post_prompt(name, var):
    # check if var may be prompted by npc
    try:
        name = name.replace('..', '')
        with open('npcs/' + name + '.json') as npcFile:
            npc = json.load(npcFile)

            for option in recursive_lookup('options', npc):
                if option['action'] == "prompt" and option['payload']['var'] == var:
                    prompt_option = option
                    print("found option")
                    break
                else:
                    prompt_option = False
            if not prompt_option:
                abort(404)
    except:
        abort(404)

    #save value to session
    session[var] = request.form[var]
    return redirect(url_for('.get_npc_dialog', name=name, dialog=prompt_option['payload']['next']))



@app.route('/npc/<path:name>/<string:dialog>')
def get_npc_dialog(name, dialog):
    # look for a matching npc and dialog
    try:
        name = name.replace('../', '')
        with open('npcs/' + name + '.json') as npcFile:
            npc = json.load(npcFile)
            npc['base_url'] = url_for('.get_npc', name=name)
            dialog = npc['dialogs'][dialog]
            dialog['text'] = replace_placeholders(markdown.markdown(dialog['text']))
            for option in dialog['options']:
                option['text'] = replace_placeholders(markdown.markdown(option['text']))
                if option['action'] == "dialog":
                    option['url'] = url_for('.get_npc_dialog', name=name, dialog=option['payload'])

        return render_template('dialog.html', npc=npc, dialog=dialog)
    except:
        abort(404)