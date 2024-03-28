import os
import time
import pandas as pd
from icecream import ic
import random
import string
import shutil
import getch
import tkinter as tk
from tkinter import ttk, messagebox
import spatial_test as spatial

random.seed()

Tasks = [
    {
        'Task': 'Task 1', 
        'Section': 'Reasoning',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you3 have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },
    {
        'Task': 'Task 2', 
        'Section': 'Perceptual Speed',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
    {
        'Task': 'Task 3', 
        'Section': 'Number Speed and Accuracy',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },
    {
        'Task': 'Task 43', 
        'Section': 'Word Meaning',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
    {
        'Task': 'Task 5', 
        'Section': 'Spatial Visualization',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
]

Line2 = 'Work as quickly and accurately ass possible.'
Line3 = 'Good luck!'

# TASK 1
reasoning_pairs = [
    {'Statement': 'Jack is taller than James', 'Question': 'Who is shorter?','Choices': ['Jack', 'James'], 'Answer': 'James'},
    {'Statement': 'Ruth is not as old as Lily', 'Question': 'Who is older?', 'Choices': ['Ruth', 'Lily'], 'Answer': 'Lily'},
    {'Statement': 'Mark is heavier than David', 'Question': 'Who is heavier?', 'Choices': ['David', 'Mark'], 'Answer': 'Mark'},
    {'Statement': 'Emma is poorer than Bruce', 'Question': 'Who is richer?','Choices': ['Bruce', 'Emma'], 'Answer': 'Bruce'},
    {'Statement': 'Lee is stronger than Josh', 'Question': 'Who is weaker?','Choices': ['Josh', 'Lee'], 'Answer': 'Josh'},
    {'Statement': 'Todd is not as funny as Matt', 'Question': 'Who is funnier?', 'Choices': ['Todd', 'Matt'], 'Answer': 'Matt'},
    {'Statement': 'Mike is not as sad as Stacy', 'Question': 'Who is happier?', 'Choices': ['Stacy', 'Mike'], 'Answer': 'Mike'},
    {'Statement': 'Ron is smarter than Joe', 'Question': 'Who is less smart?', 'Choices': ['Joe', 'Ron'], 'Answer': 'Joe'},
    {'Statement': 'Alice is taller than Bob', 'Question': 'Who is shorter?', 'Choices': ['Alice', 'Bob'], 'Answer': 'Bob'},
    {'Statement': 'Sara is older than Emily', 'Question': 'Who is younger?', 'Choices': ['Emily', 'Sara'], 'Answer': 'Emily'},
    {'Statement': 'John is heavier than Michael', 'Question': 'Who is lighter?', 'Choices': ['Michael', 'John'], 'Answer': 'Michael'},
    {'Statement': 'Anna is richer than Kate', 'Question': 'Who is poorer?', 'Choices': ['Kate', 'Anna'], 'Answer': 'Kate'},
    {'Statement': 'Chris is stronger than Peter', 'Question': 'Who is weaker?', 'Choices': ['Peter', 'Chris'], 'Answer': 'Peter'},
    {'Statement': 'Linda is funnier than Carol', 'Question': 'Who is less funny?', 'Choices': ['Carol', 'Linda'], 'Answer': 'Carol'},
    {'Statement': 'Greg is happier than Paul', 'Question': 'Who is sadder?', 'Choices': ['Paul', 'Greg'], 'Answer': 'Paul'},
    {'Statement': 'Mary is smarter than Lisa', 'Question': 'Who is less smart?', 'Choices': ['Lisa', 'Mary'], 'Answer': 'Lisa'},
    {'Statement': 'Tom is taller than Tim', 'Question': 'Who is shorter?', 'Choices': ['Tom', 'Tim'], 'Answer': 'Tim'},
    {'Statement': 'Hannah is older than Emma', 'Question': 'Who is younger?', 'Choices': ['Emma', 'Hannah'], 'Answer': 'Emma'},
    {'Statement': 'Richard is heavier than Daniel', 'Question': 'Who is lighter?', 'Choices': ['Daniel', 'Richard'], 'Answer': 'Daniel'},
    {'Statement': 'Sophia is richer than Olivia', 'Question': 'Who is poorer?', 'Choices': ['Olivia', 'Sophia'], 'Answer': 'Olivia'},
    {'Statement': 'Lucas is stronger than Ethan', 'Question': 'Who is weaker?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Rachel is funnier than Jessica', 'Question': 'Who is less funny?', 'Choices': ['Jessica', 'Rachel'], 'Answer': 'Jessica'},
    {'Statement': 'Ben is happier than Andrew', 'Question': 'Who is sadder?', 'Choices': ['Andrew', 'Ben'], 'Answer': 'Andrew'},
    {'Statement': 'Grace is smarter than Emily', 'Question': 'Who is less smart?', 'Choices': ['Emily', 'Grace'], 'Answer': 'Emily'},
    {'Statement': 'Dylan is taller than Logan', 'Question': 'Who is shorter?', 'Choices': ['Logan', 'Dylan'], 'Answer': 'Logan'},
    {'Statement': 'Madison is older than Chloe', 'Question': 'Who is younger?', 'Choices': ['Chloe', 'Madison'], 'Answer': 'Chloe'},
    {'Statement': 'Nathan is heavier than Ethan', 'Question': 'Who is lighter?', 'Choices': ['Ethan', 'Nathan'], 'Answer': 'Ethan'},
    {'Statement': 'Ava is richer than Mia', 'Question': 'Who is poorer?', 'Choices': ['Mia', 'Ava'], 'Answer': 'Mia'},
    {'Statement': 'Peter is not as big as John', 'Question': 'Who is smaller?', 'Choices': ['Peter', 'John'], 'Answer': 'Peter'},
    {'Statement': 'Alice is not as tall as Bob', 'Question': 'Who is shorter?', 'Choices': ['Alice', 'Bob'], 'Answer': 'Alice'},
    {'Statement': 'Sara is not as fast as Emily', 'Question': 'Who is slower?', 'Choices': ['Sara', 'Emily'], 'Answer': 'Sara'},
    {'Statement': 'Michael is not as strong as David', 'Question': 'Who is weaker?', 'Choices': ['Michael', 'David'], 'Answer': 'Michael'},
    {'Statement': 'Sophia is not as smart as Olivia', 'Question': 'Who is less smart?', 'Choices': ['Sophia', 'Olivia'], 'Answer': 'Sophia'},
    {'Statement': 'Ethan is not as good at singing as Lucas', 'Question': 'Who is worse at singing?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Lily is not as good at drawing as Emma', 'Question': 'Who is worse at drawing?', 'Choices': ['Lily', 'Emma'], 'Answer': 'Lily'},
    {'Statement': 'Chloe is not as talented as Madison', 'Question': 'Who is the more skillful?', 'Choices': ['Madison', 'Chloe'], 'Answer': 'Madison'},
    {'Statement': 'Juan is running faster than Tim', 'Question': 'Who will probably win the race?', 'Choices': ['Juan', 'Tim'], 'Answer': 'Juan'},
    {'Statement': 'Lucia does not play piano as well as Emma', 'Question': 'Who is the piano teacher?', 'Choices': ['Emma', 'Lucia'], 'Answer': 'Emma'},
    {'Statement': 'Peter is wiser than Daniel', 'Question': 'Who is the dumbest oen?', 'Choices': ['Daniel', 'Peter'], 'Answer': 'Daniel'},
    {'Statement': 'Ernesto is more talktative than Olivia', 'Question': 'Who is more reserved?', 'Choices': ['Olivia', 'Ernesto'], 'Answer': 'Olivia'},
    {'Statement': 'Melania dances better than Silvia', 'Question': 'Who is a bad dancer?', 'Choices': ['Silvia', 'Melania'], 'Answer': 'Silvia'},
    {'Statement': 'Ethan is not as good at singing as Lucas', 'Question': 'Who is worse at singing?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Lily is not as good at drawing as Emma', 'Question': 'Who is worse at drawing?', 'Choices': ['Lily', 'Emma'], 'Answer': 'Lily'},
    {'Statement': 'Chloe is not as talented as Madison', 'Question': 'Who is the more skillful?', 'Choices': ['Madison', 'Chloe'], 'Answer': 'Madison'},    
]

# TASK 2
perceptual_top = ['E', 'Q', 'D', 'K', 'R', 'P']


synonym_pairs = [
    ['happy', 'joyful'], ['sad', 'gloomy'], ['big', 'large'], ['small', 'tiny'], ['hot', 'burning'], ['cold', 'freezing'], ['teach', 'educate'], ['learn', 'study'], 
    ['break', 'shatter'], ['fix', 'repair'], ['day', 'morning'], ['night', 'evening'], ['give', 'donate'], ['take', 'receive'], ['sharp', 'keen'], ['dull', 'blunt'], 
    ['high', 'tall'], ['low', 'short'], ['red', 'crimson'], ['blue', 'azure'], ['green', 'emerald'], ['yellow', 'golden'], ['black', 'dark'], ['white', 'pale'], 
    ['walk', 'run'], ['talk', 'shout'], ['write', 'draw'], ['read', 'watch'], ['eat', 'drink'], ['think', 'ponder'], ['dog', 'puppy'], ['bird', 'fly'], 
    ['horse', 'mare'], ['snake', 'serpent'], ['elephant', 'giant'], ['monkey', 'ape'], ['house', 'building'], ['car', 'vehicle'], ['book', 'magazine'], 
    ['table', 'desk'], ['computer', 'laptop'], ['door', 'gateway'], ['bread', 'loaf'], ['cheese', 'dairy'], ['meat', 'flesh'], ['vegetables', 'greens'], 
    ['pasta', 'noodles'], ['candy', 'sweets'], ['angry', 'furious'], ['scared', 'terrified'], ['tired', 'weary'], ['bored', 'monotonous'], ['proud', 'elated'], 
    ['jealous', 'envious'], ['speak', 'converse'], ['whisper', 'murmur'], ['bright', 'luminous'], ['dull', 'lifeless'], ['loud', 'boisterous'], ['quiet', 'silent'], 
    ['fragrant', 'aromatic'], ['foul', 'putrid'], ['heavy', 'weighty'], ['light', 'airy'], ['abundant', 'plentiful'], ['scarce', 'rare'], ['victory', 'triumph'], 
    ['defeat', 'loss'], ['hope', 'optimism'], ['despair', 'despondency'], ['love', 'affection'], ['hate', 'loathing'], ['trust', 'reliance'], ['betrayal', 'treachery']
 ]

antonym_pairs = [
    ['happy', 'sad'], ['big', 'small'], ['hot', 'cold'], ['long', 'short'], ['wide', 'narrow'], ['bright', 'dark'], ['rough', 'smooth'], ['wet', 'dry'],
    ['loud', 'quiet'], ['fast', 'slow'], ['deep', 'shallow'],['thick', 'thin'], ['heavy', 'light'], ['full', 'empty'], ['open', 'closed'], ['clean', 'dirty'],
    ['strong', 'weak'], ['beautiful', 'ugly'], ['rich', 'poor'], ['young', 'old'], ['active', 'passive'], ['kind', 'cruel'], ['honest', 'dishonest'], ['brave', 'cowardly'],
    ['careful', 'careless'], ['optimistic', 'pessimistic'], ['generous', 'selfish'], ['polite', 'rude'], ['calm', 'angry'], ['peaceful', 'chaotic'], ['healthy', 'sick'], ['fresh', 'stale'],
    ['sweet', 'sour'], ['bitter', 'sweet'], ['soft', 'hard'], ['smooth', 'rough'], ['flexible', 'rigid'], ['dull', 'sharp'], ['loud', 'quiet'], ['noisy', 'silent'], ['fragrant', 'smelly'],
    ['attractive', 'unattractive'], ['successful', 'unsuccessful'], ['winner', 'loser'], ['gain', 'lose'], ['beginning', 'end'], ['top', 'bottom'], ['front', 'back'],  ['inside', 'outside'],
    ['above', 'below'], ['speak', 'listen'], ['give', 'take'], ['buy', 'sell'], ['show', 'hide'], ['open', 'close'], ['build', 'destroy'], ['create', 'destroy'],
    ['start', 'finish'], ['arrive', 'leave'], ['come', 'go'], ['day', 'night'], ['summer', 'winter'], ['hot', 'cold'], ['dry', 'wet'], ['light', 'dark'],
    ['love', 'hate'], ['trust', 'doubt'], ['friend', 'enemy'], ['truth', 'lie'], ['justice', 'injustice'],['freedom', 'imprisonment'], ['peace', 'war'], ['order', 'chaos'], 
    ['success', 'failure'], ['victory', 'defeat'], ['knowledge', 'ignorance'], ['wisdom', 'foolishness'], ['logic', 'emotion'], ['science', 'faith'], ['reality', 'fantasy'],  ['simple', 'complex'],
    ['easy', 'difficult'], ['familiar', 'strange'], ['famous', 'unknown'], ['public', 'private'], ['open', 'secret'], ['honest', 'deceitful'], ['clear', 'unclear'], ['confident', 'unsure'], 
    ['brave', 'cowardly'], ['generous', 'selfish'], ['active', 'lazy'], ['calm', 'excited'], ['patient', 'impatient'], ['organized', 'messy'], ['hopeful', 'despairing'], ['confident', 'doubtful'], 
    ['realistic', 'idealistic'], ['outgoing', 'shy'], ['talkative', 'quiet'],
]

analog_pairs = [
    ['happy', 'joyful'], ['big', 'large'], ['hot', 'burning'], ['long', 'extensive'], ['wide', 'broad'], ['bright', 'brilliant'], ['rough', 'uneven'], ['wet', 'damp'],
    ['loud', 'boisterous'], ['fast', 'rapid'], ['deep', 'profound'], ['thick', 'dense'], ['heavy', 'weighty'], ['full', 'brimming'], ['open', 'uncovered'], ['clean', 'spotless'],
    ['strong', 'powerful'], ['beautiful', 'gorgeous'], ['rich', 'wealthy'], ['young', 'youthful'], ['active', 'energetic'], ['kind', 'benevolent'], ['honest', 'truthful'], ['brave', 'courageous'],
    ['careful', 'cautious'], ['optimistic', 'hopeful'], ['generous', 'unselfish'], ['polite', 'courteous'], ['calm', 'serene'], ['peaceful', 'tranquil'], ['healthy', 'fit'], ['fresh', 'new'],
    ['sweet', 'luscious'], ['bitter', 'acrid'], ['soft', 'gentle'], ['smooth', 'sleek'], ['flexible', 'pliable'], ['dull', 'blunt'], ['noisy', 'raucous'], ['fragrant', 'aromatic'], 
    ['attractive', 'appealing'], ['successful', 'victorious'], ['winner', 'champion'], ['gain', 'acquire'], ['beginning', 'commencement'], ['top', 'summit'], ['front', 'forefront'], ['inside', 'interior'],
    ['above', 'superior'], ['speak', 'converse'], ['give', 'bestow'], ['buy', 'purchase'], ['show', 'display'], ['open', 'unfold'], ['build', 'construct'], ['create', 'fashion'],
    ['start', 'initiate'], ['arrive', 'reach'], ['come', 'approach'], ['day', 'dawn'], ['summer', 'estivation'],  ['love', 'adoration'], ['trust', 'faith'], ['friend', 'companion'],
    ['truth', 'veracity'], ['justice', 'equity'], ['freedom', 'liberty'], ['peace', 'harmony'], ['order', 'method'], ['success', 'achievement'], ['victory', 'triumph'], ['knowledge', 'erudition'],
    ['wisdom', 'sagacity'], ['logic', 'reason'], ['science', 'inquiry'], ['reality', 'actuality'], ['simple', 'basic'], ['easy', 'effortless'], ['familiar', 'well-known'], ['famous', 'renowned'],
    ['public', 'open'], ['open', 'frank'], ['honest', 'sincere'], ['clear', 'unambiguous'], ['confident', 'assured'], ['brave', 'valorous'], ['generous', 'charitable'], ['active', 'dynamic'],
    ['calm', 'composed'], ['patient', 'forbearing'], ['organized', 'systematic'], ['hopeful', 'optimistic'],  ['confident', 'self-assured'], ['realistic', 'pragmatic'], ['outgoing', 'extroverted'],
    ['talkative', 'loquacious'],
]

unrelated_words = [
    'apple', 'chair', 'ocean', 'mountain', 'umbrella', 'piano', 'cloud', 'camera', 'guitar', 'bicycle', 
    'flower', 'river', 'hat', 'moon', 'star', 'candle', 'island', 'mirror', 'sun', 'train',
    'shoe', 'key', 'window', 'ship', 'butterfly', 'wallet', 'globe', 'clock', 'map', 'cake',
    'painting', 'telephone', 'coin', 'hammer', 'chair', 'bag', 'glasses', 'guitar', 'scissors', 'towel',
    'basket', 'pillow', 'mirror', 'cushion', 'bottle', 'gloves', 'book', 'umbrella', 'basketball', 'guitar',
    'brush', 'remote', 'pen', 'lamp', 'fan', 'toothbrush', 'flag', 'mug', 'chair', 'eraser',
    'calculator', 'stapler', 'magnet', 'fridge', 'calendar', 'clock', 'tape', 'wallet', 'sponge', 'microscope', 
    'soul', 'CAT-scan', 'chill', 'vodka'
]

word_pairs = synonym_pairs + antonym_pairs + analog_pairs

# Screen and Text helper functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen


def press_any_key(message='Press any key...'):
    print(message)
    getch.getch()  # Wait for any key press

def center_text(text, width=None):
    terminal_width, _ = shutil.get_terminal_size((80, 20))  # default terminal width
    if width is None:
        width = terminal_width
    left_padding = (terminal_width - width) // 2
    return ' ' * left_padding + str(text)

def pad_text(text, num_chars, side='left', padding_char=' '):
    if side == 'left':
        return padding_char * num_chars + text
    elif side == 'right':
        return text + padding_char * num_chars
    else:
        raise ValueError('Invalid "side" argument. Use "left" or "right".')
    
def add_listcol(mylist: list, newcol: list):
    for elem, item in mylist, newcol:
        elem.append(item)


class Perceptual:
  '''
  A class for performing perceptual tasks with characters.
  '''

  def __init__(self, characters=string.ascii_letters):
    '''
    Initializes the Perceptual class with a character list.

    Args:
        characters: A list of characters to use (default: string.ascii_letters).
    '''
    self.characters = characters

  def shuffle_chars(self, char_list, num_chars, hit_prob = 0.5):
    '''
    Shuffles a list of characters, considers case changes, and returns a desired length.

    Args:
        char_list: A list of characters.
        num_chars: The desired length of the returned list.

    Returns:
        A new list of shuffled characters with case modifications (up to num_chars length).
    '''
    top_list = list(char_list).copy()  # Create a copy to avoid modifying the original
    bottom_list = top_list.copy()
     
    random.shuffle(top_list)  # Shuffle the characters
     

    # Modify case for a random subset of characters
    for i in range(min(num_chars, len(top_list))):
        if random.random() < 0.5:  # 50% chance of modification
            top_list[i] = top_list[i].swapcase()
        if random.random() <= hit_prob:
            bottom_list[i] = top_list[i].swapcase()
        else:
            bottom_list[i] = top_list[random.randint(0,len(top_list) - 1)].swapcase()
    return top_list[:num_chars], bottom_list[:num_chars]  # Return the desired number of characters

  def count_matching_chars(self, top_chars, bottom_chars):
    '''
    Counts the number of matching characters (case-insensitive) between two lists.

    Args:
        top_chars   : The first list of characters.
        bottom_chars: The second list of characters.

    Returns:
        The number of matching characters (case-insensitive).
    '''
    matches = 0
    for i in range(len(top_chars)):
      if top_chars[i].lower() == bottom_chars[i].lower():
        matches += 1
    return matches

class NumberSpeedAccuracy:
    @staticmethod
    @staticmethod
    def furthest_from_median(numbers):
        median = sum(numbers) / len(numbers)
        furthest = max(numbers, key=lambda x: abs(x - median))
        return furthest    
    
    @staticmethod    
    def choicify(triplet):
        choices = ';    '.join(f'{i+1}) {value}' for i, value in enumerate(triplet))
        return choices
      
class GIAtest:
    def __init__(self):
        self.candidate_name = 'Omar Arias'
        self.question_counter = 0
        self.num_questions = 30      # Questions per task    <<<<<<<<<<<<
        
        self.tasks = {
            1: {'name': 'Reasoning', 'options': 2, 'time': 30},
            2: {'name': 'Perceptual Speed', 'options': 5, 'time': 45},
            3: {'name': 'Number Speed & Accuracy', 'options': 5, 'time': 40},
            4: {'name': 'Word Meaning', 'options': 4, 'time': 35},
            5: {'name': 'Spatial Visualization', 'options': 4, 'time': 35}
        }
        self.exam_data_file = 'exam_results.xlsx'

        self.results = [
            {'Task': 1, 'Name': self.candidate_name, 'Total Questions': 0, 'Correct Answers': 0, 'Elapsed Time': 0},
            {'Task': 2, 'Name': self.candidate_name, 'Total Questions': 0, 'Correct Answers': 0, 'Elapsed Time': 0},
            {'Task': 3, 'Name': self.candidate_name, 'Total Questions': 0, 'Correct Answers': 0, 'Elapsed Time': 0},
            {'Task': 4, 'Name': self.candidate_name, 'Total Questions': 0, 'Correct Answers': 0, 'Elapsed Time': 0},
            {'Task': 5, 'Name': self.candidate_name, 'Total Questions': 0, 'Correct Answers': 0, 'Elapsed Time': 0},
        ]
        self.exam_data = pd.DataFrame(columns=['Name', 'Task', 'Total Questions', 'Correct Answers', 'Elapsed Time'])
        self.scorelevel = ['Low',              #  4-15
                           'Below Average',    # 16-34
                           'Average',          # 35-65
                           'Above Average',    # 66-85
                           'High']             # 86-96
        self.correct_answers = 0
        self.total_questions = 0
        self.correct_answers = 0     
        self.new_record = pd.DataFrame({
            'Name': self.candidate_name,
            'T1 Questions': 0,
            'T1 Correct':   0,
            'T1 Time':      None,
            'T2 Questions': 0,
            'T2 Correct':   0,
            'T2 Time':      None,
            'T3 Questions': 0,
            'T3 Correct':   0,
            'T3 Time':      None,
            'T4 Questions': 0,
            'T4 Correct':   0,
            'T4 Time':      None,
            'T5 Questions': 0,
            'T5 Correct':   0,
            'T5 Time':      None,
            'Total Questions': 0,
            'Correct Answers': 0,
            'Elapsed Time': None
        }, index=[0])  # Create a DataFrame with single row


        
    def __task_header(self, task_num):
        if task_num >= len(Tasks):
            return None
        print(Tasks[task_num-1]['Task'] ,': ' , Tasks[task_num-1]['Section'] + '.')
        print('\n\n')
        print(Tasks[task_num-1]['Header1'])
        print(Tasks[task_num-1]['Header2'])
        print('\n\n')
        print(Line2)
        print(Line3)        
        print('\n\n')

    def __display_question(self, task_num, i):
        if task_num == 1:     # TASK1: Reasoning
            stmt = reasoning_pairs[i]['Statement']
            question = reasoning_pairs[i]['Question']
            choices = reasoning_pairs[i]['Choices']
            
            # Displays the question
            print('\n\n')
            print(f'Question {self.question_counter}/{self.num_questions*5}: ')
            print((len(f'Question {self.question_counter}/{self.num_questions*5}: ') - 1) * '=')    # Underline
            print('\n\n')
            print(center_text(stmt))
            print('\n')
            print(center_text(question))
            print('\n\n')
            print(center_text(choices))
            print('\n\n')
            return None        
                    
        if task_num == 2:     # TASK2: Perceptual Speed
            stmt = 'Each question in this section consists of 4 pairs of letters arranged vertically.'
            print(center_text(stmt))
            print('\n')
            question = 'Your task is to determine how many VERTICAL pairs contain the same letter.'.upper()
            print(center_text(question))
            question = 'Work as quickly and accurately as possible.'
            print(center_text(question))
            print('\n')
            question = 'The section contains 8 questions.'
            print(center_text(question))
            print('\n\n')
            # Displays the question
            print('\n\n')
            print(f'Question {self.question_counter}/{self.num_questions*5}: ')
            print((len(f'Question {self.question_counter}/{self.num_questions*5}: ') - 1) * '=')    # Underline
            print('\n\n')            
            return None
        
        if task_num == 3:
            stmt = 'Each question in this section includes 3 numbers.'
            print(center_text(stmt))
            print('\n')
            question = 'Your task is to find the number that is furthest from the median.'.upper()
            print(center_text(question))
            question = 'Work as quickly and accurately as possible.'
            print(center_text(question))
            print('\n')
            question = 'The section contains 8 questions.'
            print(center_text(question))
            print('\n\n')
            # Displays the question            
            print('\n\n')          
            print(f'Question {self.question_counter}/{self.num_questions*5}: ')
            print((len(f'Question {self.question_counter}/{self.num_questions*5}: ') - 1) * '=')    # Underline
            print('\n\n')            
            return None

        if task_num == 4:
            stmt = 'Each question in this section includes 3 words.'
            print(center_text(stmt))
            print('\n')
            question = 'Your task is to find the odd word out.'
            print(center_text(question))
            question = 'Work as quickly and accurately as possible.'
            print(center_text(question))
            print('\n')
            question = 'The section contains 8 questions.'
            print(center_text(question))
            print('\n\n')
            # Displays the question            
            print('\n\n')     
            print(f'Question {self.question_counter}/{self.num_questions*5}: ')
            print((len(f'Question {self.question_counter}/{self.num_questions*5}: ') - 1) * '=')    # Underline
            print('\n\n')              
            return None   
                 
        if task_num == 5:
            stmt = 'Each question in this section consists of 2 pairs of letters.'
            print(center_text(stmt))
            print('\n')
            question = 'Your task is determine how many pairs contain rotated version of the same letter. Mirror images are not considered as a rotated version.'.upper()
            print(center_text(question))
            question = 'Work as quickly and accurately as possible.'
            print(center_text(question))
            print('\n')
            question = 'The section contains 8 questions.'
            print(center_text(question))
            print('\n\n')
            # Displays the question            
            print('\n\n')           
            print(f'Question {self.question_counter}/{self.num_questions*5}: ')
            print((len(f'Question {self.question_counter}/{self.num_questions*5}: ') - 1) * '=')    # Underline
            print('\n\n')              
            return None      
        
    def __get_answer(self, prompt, choices):
        while True:
            ans = (input(prompt))
            if ans.lower() == 'q':
                print('The exam was cancelled')
                quit()
            try:
                ans = int(ans)
            except:
                print('\n*** A number was expected. Try again ***\n')
                continue
            if ans <= len(choices):
                break
            else:
                print('\n*** Invalid answer ***\n')            
        return ans
        
    def __make_question(self, task_num, i=0):
        self.question_counter += 1
        if task_num == 1:     # TASK 1: Reasoning
            random.shuffle(reasoning_pairs)
            choices = reasoning_pairs[i]['Choices']
            correct_answer = reasoning_pairs[i]['Answer']
            
            # Displays the question
            self.__display_question(task_num, i)
            
            ans = self.__get_answer(f'Select the best option: (1-{len(choices)}): ', choices)
                    
            # Updating the counters
            self.total_questions += 1
            self.task_questions  += 1

            # Checks if the answer is correct
            if choices[ans-1] == correct_answer:
                self.correct_answers      += 1                
                self.task_correct_answers += 1                
            return ans
        
        if task_num == 2:    # TASK 2: Perceptual
            # Displays the question
            self.__display_question(task_num, i)
            
            perceptual      = Perceptual()
            available_chars = 4
            num_chars       = 4
            hit_prob        = 0.2
            # Generate two random lists with modified cases
            top_chars, bottom_chars = perceptual.shuffle_chars(perceptual.characters[:available_chars], num_chars, hit_prob)
            
            # Count matching characters (case-insensitive)
            matching_count = perceptual.count_matching_chars(top_chars, bottom_chars)
            
            print('\n\n')
            print(pad_text(f'Top:      {top_chars}', 10))
            print('')
            print(pad_text(f'Bottom:   {bottom_chars}', 10))
            print('\n\n')
            
            # ic(matching_count)
            correct_answer = matching_count
            choices = range(5)      # 0, 1, 2, 3, 4
            
            print('\n')
            ans = self.__get_answer(f'Number of matching characters (case-insensitive): ', choices)   
                     
            # Updating the counter
            self.total_questions += 1
            self.task_questions  += 1

            # Checks if the answer is correct
            if ans == correct_answer:
                self.correct_answers      += 1            
                self.task_correct_answers += 1    
            return ans
        
        if task_num == 3:   # TASK 3: Number Speed & Accuracy
            # return -1
            # Displays the question
            self.__display_question(task_num, i)
            max_sample = 40
            triplet = random.sample(range(1, max_sample + 1), 3)
            # Calculate the correct number
            correct_answer = NumberSpeedAccuracy.furthest_from_median(triplet)
            # ic(triplet)
            # ic(type(triplet))
            # ic(correct_answer)
            
            choices = range(3)      # 0, 1, 2
            print(pad_text(NumberSpeedAccuracy.choicify(triplet), 10))
            print('\n')
            ans = self.__get_answer(f'Select the number of the right answer: ', choices)   
            # Updating the counter
            self.total_questions += 1
            self.task_questions  += 1
            if (triplet[ans-1] == correct_answer):
                self.correct_answers      += 1     
                self.task_correct_answers += 1     
            return ans
            
        if task_num == 4:    # TASK 4: Word Meaning
            # Displays the question
            self.__display_question(task_num, i)            
            full_unrelated_words = unrelated_words * 4
            full_unrelated_words = full_unrelated_words[:len(word_pairs)]   # limits the list size to the sum of the list sizes of word pairs

            choices = range(3)     # only 3 options to choose from in this Task            
            # puts everything together: related and unrelated words into a triplet list
            word_triplets = [[word1, word2, full_unrelated_words[i]] for i, (word1, word2) in enumerate(word_pairs)]
            random.shuffle(word_triplets)      # shuffles the entire triplets list
            
            choices = word_triplets.pop()
            odd_word = choices[2]
            # ic(odd_word)
            random.shuffle(choices)           # shuffles the three words (2 related and one unrelated)

            # self.__display_question(task_num, i)
            print('\n')
            print(pad_text(NumberSpeedAccuracy.choicify(choices), 10))
            print('')
            ans = self.__get_answer(f"Select the number of the word that doesn't belong: ", choices)   
            self.total_questions += 1    
            self.task_questions  += 1   
            if choices[ans-1] == odd_word:
                self.correct_answers      += 1    
                self.task_correct_answers += 1    
            return ans
        
        if task_num == 5:   # TASK 5 - Spatial    
            self.__display_question(task_num, i)   

            return 0
   
    def register_metrics(self, task_num, num_questions, num_correct, elapsed_time):
        # Updates the specified task metrics
        self.new_record.at[0, 'T' + str(task_num) + ' Questions'] = num_questions
        self.new_record.at[0, 'T' + str(task_num) + ' Correct']   = num_correct
        self.new_record.at[0, 'T' + str(task_num) + ' Time']      = f'{elapsed_time:.1f}' 
            
    def display_task(self, task_num):
        clear_screen()

        self.__task_header(task_num)
        self.task_questions       = 0
        self.task_correct_answers = 0

        start_time = time.time()
        
        for i in range(self.num_questions):
            ans = self.__make_question(task_num, i)
            clear_screen()
                
        # Updates the dataframe to write to stats to Excel            
        end_time = time.time()
        elapsed_time = end_time - start_time

        self.results[task_num-1]['Total Questions'] += self.task_questions
        self.results[task_num-1]['Correct Answers'] += self.task_correct_answers                
        self.results[task_num-1]['Elapsed Time'] += elapsed_time
           
        # Add task results to DataFrame
        self.register_metrics(task_num, self.task_questions, self.task_correct_answers, elapsed_time)

    def take_exam(self):
        clear_screen()
        print ('\n')        
        print (center_text('--- Welcome to the GIA Test Practice --- '))
        print ('\n\n\n\n')
        press_any_key(center_text('Please, press any key when you are ready...'))

        for task_num in self.tasks:
            self.display_task(task_num)
            



    def print_results(self):

        if self.total_questions == 0:
            print('No questions answered!')
            return -1
        
        clear_screen()
        
        total_score = self.results[0]['Correct Answers'] / self.results[0]['Total Questions']
        total_time = self.results[0]['Elapsed Time']
        print('\nRESULTS ---------------------------------\n')
        print('')
        print(f'Total Questions:       {self.total_questions}')
        print(f'Total Correct Answers: {self.correct_answers}')
        print('')
        print(f'Total Score:        {total_score:.1%}')
        print(f'Total Elapsed Time: {total_time:.1f} seconds')     
        print('')   
        print(f'Seconds per question:         {total_time/self.total_questions:.1f} seconds')        
        print(f'Seconds per correct question: {total_time/self.correct_answers:.1f} seconds')   
        print('')
        print('Task details:\n')  
        for item in self.results:
            print(item)   
        print('\n')
                
    def save_results(self):
        print('Saving Results...')
        
        # Adds the new record
        self.exam_data = pd.concat([self.exam_data, self.new_record], ignore_index=True)

        if os.path.exists(self.exam_data_file):
            # If file exists, read existing data
            existing_data = pd.read_excel(self.exam_data_file)
            # Concatenate existing data with new data
            updated_data = pd.concat([existing_data, self.exam_data], ignore_index=True)
            # Write updated data to Excel file           
            updated_data.to_excel(self.exam_data_file, index=False)
        else:
            # If file does not exist, write exam data directly to Excel file
            self.exam_data.to_excel(self.exam_data_file, index=False)
        
        print('Results saved successfully!')

    



#           M A I N 
def main():
    # ic.disable()
    exam = GIAtest()
    exam.take_exam()
    
    # Spatial
    root = tk.Tk()
    root.geometry("500x640")  
    spatial_test = spatial.ImageApp(root, exam.num_questions, exam.question_counter-1)
    
    root.mainloop()
    root.quit() 
    exam.register_metrics(5, spatial_test.local_questions, spatial_test.correct_answers, spatial_test.total_time)

    ic(spatial_test.question_number)
    ic(spatial_test.correct_answers)
    ic(spatial_test.total_time)

    
    # Sum all the elapsed times from the different tasks    
    exam.new_record.at[0, 'Total Questions'] = sum(item['Total Questions']  for item in exam.results)
    exam.new_record.at[0, 'Correct Answers'] = sum(item['Correct Answers']  for item in exam.results)
    exam.new_record.at[0, 'Elapsed Time']    = sum(item['Elapsed Time']     for item in exam.results)
    exam.save_results()
    
    
    # exam.print_results()
    

if __name__ == '__main__':
      main()
      
