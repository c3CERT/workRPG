# What is it?
A bit of python (flask) and json definitions for npcs.

## How to test it?

1. install a virtualenv (e.g. `python3 -m venv /path/to/new/virtual/environment`)
2. `pip install -r requirements.txt`
3. 
```
  export FLASK_APP=workrpg.py 
  cd src
  flask run
```

## Endpoints
There are currently 2 endpoints

| path | Description |
| ---- | ----------- |
| `/npc/<filename>` | redirect to start dialog or 404 |
| `/npc/<filename>/<dialog>` | display given dialog of a npc or 404 |

Example NPC: http://127.0.0.1:5000/npc/example


## Current state
* Very basic template showing the npc name, his dialog text and the dialog options
* dialog text and option texts are markdown enabled.

### TODO
* Render npc images if given (dialog image > npc image > No image/Placeholder)
* Play audio if any.
* Beefed out template
* ~~Option/way to prompt for a variable (most importantly username)~~
* ~~Replacement of variable|username placeholders in dialogs.~~
