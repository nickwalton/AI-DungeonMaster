# AI-DungeonMaster

### AI Dungeon Master is an automatically generated text adventure. It generates results and actions based on action prompts fed to the GPT-2 Model. 


## How to Install
```
git clone http://github.com/nickwalton/AI-DungeonMaster
pip install regex
pip install numpy
```
### Either Install CPU Tensorflow
```
pip install tensorflow
```

### Or install GPU Tensorflow (faster) but requires CUDA
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
