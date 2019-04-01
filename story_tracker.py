import yaml


class StoryTracker():

    def __init__(self):
    
        self.prompts_dict = yaml.load(open('story_prompts.yaml'))
        
        self.story_blocks = []
        self.start_prompt = None
        self.action_blocks = []
        self.action_phrases = ["You attack", "You tell them", "You use", "You go"]
        
    def select_story(self, story):
        self.start_prompt = self.prompts_dict[story]
        return self.start_prompt
        
    def get_possible_stories(self):
        return list(self.prompts_dict.keys())
        
    def get_story_prompt(self, action):
        self.action_blocks.append(action)
        return self.start_prompt + self.story_blocks[-1] + action
        
        
    def get_action_prompt(self, story_block):
        self.story_blocks.append(story_block)
        return self.start_prompt + self.story_blocks[-1]
        
        
    def get_action_phrases(self):
        return self.action_phrases
    
        
        
    
