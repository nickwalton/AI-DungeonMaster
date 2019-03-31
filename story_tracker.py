import yaml


class StoryTracker():

    def __init__(self, story="bees"):
    
        prompts_dict = yaml.load(open('story_prompts.yaml'))
        self.start_prompt = prompts_dict[story]
        
        self.story_blocks = []
        self.action_blocks = []
        self.action_phrases = ["You attack", "You tell them", "You use", "You go"]
        
    def get_story_prompt(self, action):
        self.action_blocks.append(action)
        return self.start_prompt + self.story_blocks[-1] + action
        
        
    def get_action_prompt(self, story_block):
        self.story_blocks.append(story_block)
        return self.start_prompt + self.story_blocks[-1]
        
        
    def get_action_phrases(self):
        return self.action_phrases
    
        
        
    
