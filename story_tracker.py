
class StoryTracker():

    def __init__(self):
        self.start_prompt = "You enter a dungeon with your trusty sword and shield. You are searching for your true desire which you know is at the lowest level of this dungeon. You know you will encounter goblins and ogres. You enter the first door and see "
        
        self.story_blocks = []
        self.action_blocks = []
        self.action_phrases = ["You attack", "You tell them", "You use", "You go"]
        
    def get_story_prompt(self, action):
        self.action_blocks.append(action)
        return self.story_blocks[-1] + action
        
        
    def get_action_prompt(self, story_block):
        self.story_blocks.append(story_block)
        return self.story_blocks[-1]
        
        
    def get_action_phrases(self):
        return self.action_phrases
    
        
        
    
