import os
import time
import pandas as pd
from   icecream import ic
import random
import string
import shutil
import getch
import tkinter as tk
from tkinter import ttk, messagebox
import spatial_test as spatial
from gia_data_es import Tasks, Line2, Line3, reasoning_pairs, perceptual_top, synonym_pairs, antonym_pairs, unrelated_words, word_pairs

random.seed()


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
        
        self.num_questions    = 30      # QUESTIONS PER TASK    <<<<<<<<<<<<
        
        self.candidate_name   = 'Omar Arias'
        self.question_counter = 0
               
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
    start_time = time.time()
    spatial_test = spatial.ImageApp(root, exam.num_questions, exam.question_counter-1)
    root.mainloop()
    end_time = time.time()
    elapsed_time = end_time - start_time
    root.quit() 
    
    # Updates the metrics gathered from the Spatial Visualization Task
    exam.results[4]['Total Questions'] += spatial_test.local_questions
    exam.results[4]['Correct Answers'] += spatial_test.correct_answers                
    exam.results[4]['Elapsed Time'] += elapsed_time
    exam.register_metrics(5, spatial_test.local_questions, spatial_test.correct_answers, elapsed_time)
    
    # Sum all the elapsed times from the different tasks    
    exam.new_record.at[0, 'Total Questions'] = sum(item['Total Questions']  for item in exam.results)
    exam.new_record.at[0, 'Correct Answers'] = sum(item['Correct Answers']  for item in exam.results)
    exam.new_record.at[0, 'Elapsed Time']    = sum(item['Elapsed Time']     for item in exam.results)
    exam.save_results()
    
    
    # exam.print_results()
    

if __name__ == '__main__':
      main()
      
