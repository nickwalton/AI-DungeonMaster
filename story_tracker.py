import yaml


class StoryTracker():

    def __init__(self, use_entire_story = False):
    
        self.prompts_dict = yaml.load(open('story_prompts.yaml'))
        self.use_entire_story = use_entire_story
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
        
        if self.use_entire_story:
            return self.get_whole_story()
        else:

            return self.start_prompt + self.story_blocks[-1] + action
        
    def get_action_prompt(self, story_block):
        self.story_blocks.append(story_block)
        
        if self.use_entire_story:
            return self.get_whole_story()
        else:
            return self.start_prompt + self.story_blocks[-1]
        
    def get_action_phrases(self):
        return self.action_phrases
        
    def get_whole_story(self):
    
        story = self.start_prompt
        for i in range(len(self.action_blocks)):
            story += self.story_blocks[i]
            story += self.action_blocks[i]
            story += "\n"
            
        if len(self.story_blocks) > len(self.action_blocks):
            story += self.story_blocks[-1]
  
        return story
        
        
    
