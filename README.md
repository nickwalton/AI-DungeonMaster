# AI-DungeonMaster

### AI Dungeon Master is an automatically generated text adventure. It generates results and actions based on action prompts fed to the GPT-2 Model. 


## Installation
```
git clone http://github.com/nickwalton/AI-DungeonMaster
pip install regex
pip install numpy
pip install tensorflow
```

## (Optional) tensorflow-gpu
For faster performance you can instead install tensorflow-gpu, but you'll also need up to date nvidia graphics drivers and cuda. 
```
pip install tensorflow-gpu==1.12
```

## Download the GPT-2 Model
```
cd AI-DungeonMaster
python download_model.py 117M
```

## Run the Game
```
python dungeon_master.py
```
