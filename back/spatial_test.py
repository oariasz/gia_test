import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os
import time
from icecream import ic
# import gia_test as gia

class ImageApp:
    def __init__(self, master, questions, starting_question=1):
        self.master = master
        self.master.title("GIA Spatial Aptitude Test")
        
        self.starting_question = starting_question
        self.question_number   = starting_question
        self.local_questions   = self.question_number - self.starting_question
                       
        self.total_questions   = questions
       
        self.total_time = 0.0
        self.correct_answers = 0
        
        self.letters_subset = ['B', 'F', 'P', 'R']
        self.transformations = ['original', 'rotated', 'rotated', 'flipped']

        # Label: Question Number title
        self.qn_label = ttk.Label(master, text="Question No. " + str(self.question_number), font=("Helvetica", 24))
        self.qn_label.pack(pady=(30,0))

        # Label: head question
        self.question_label = ttk.Label(master, text="How many bottom images are only rotated?", font=("Helvetica", 18))
        self.question_label.pack(pady=(20,0))

        # Images frame        
        self.images_frame = ttk.Frame(master)
        self.images_frame.pack()


        self.top_left_image_label = tk.Label(self.images_frame)
        self.bottom_left_image_label = tk.Label(self.images_frame)
        self.top_right_image_label = tk.Label(self.images_frame)
        self.bottom_right_image_label = tk.Label(self.images_frame)
        
        self.generate_images()
        self.display_images()
        
        # Buttons
        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.pack()
        
        # Create a custom style for the buttons
        # button_style = ttk.Style()
        # button_style.configure("TButton", padding=10, background="navy", foreground="white")
        # button_style.configure("TButton", padding=(10, 5), background="navy", foreground="white", pressedbackground="navy")
        
        self.button_0 = ttk.Button(self.buttons_frame, text="0", command=lambda: self.check_answer(0))
        self.button_0.grid(row=0, column=0)
        self.button_1 = ttk.Button(self.buttons_frame, text="1", command=lambda: self.check_answer(1))
        self.button_1.grid(row=0, column=1)
        self.button_2 = ttk.Button(self.buttons_frame, text="2", command=lambda: self.check_answer(2))
        self.button_2.grid(row=0, column=2)
        
        # Add extra padding to the top of the choice buttons
        self.button_0.grid_configure(pady=(40, 0))
        self.button_1.grid_configure(pady=(40, 0))
        self.button_2.grid_configure(pady=(40, 0))
        
        # button_style.configure("Close.TButton", background="dark red", foreground="white")

        self.close_button = ttk.Button(master, text="Close", command=self.finish_test)
        # Add extra padding to the top of the close button
        self.close_button.pack(pady=(40, 40))

        # Make buttons taller by increasing padding
        self.button_0.config(padding=(10, 10))
        self.button_1.config(padding=(10, 10))
        self.button_2.config(padding=(10, 10))
        self.close_button.config(padding=(10, 10))

        self.start_time = time.time()

    def generate_images(self):
        # First column
        self.top_left_letter = random.choice(self.letters_subset)
        self.bottom_left_letter = self.top_left_letter
        
        # Second column
        self.top_right_letter = random.choice(self.letters_subset)
        self.bottom_right_letter = self.top_right_letter
        
        # while self.bottom_left_letter == self.top_left_letter:
        #    self.bottom_left_letter = random.choice(self.letters_subset)
            
        # while self.bottom_right_letter == self.top_right_letter or self.bottom_right_letter == self.bottom_left_letter:
        #     self.bottom_right_letter = random.choice(self.letters_subset)
        
        self.top_left_transformation = random.choice(self.transformations)
        self.bottom_left_transformation = random.choice(self.transformations[1:])
        self.top_right_transformation = random.choice(self.transformations)
        self.bottom_right_transformation = random.choice(self.transformations[1:])
        
        self.top_left_image = Image.open(os.path.join('letters', f'{self.top_left_letter}.png'))

        self.top_right_image = Image.open(os.path.join('letters', f'{self.top_right_letter}.png'))

        # First, we apply the transformation on the top images
        if self.top_left_transformation == 'rotated':
            times = random.randint(1, 2)
            self.top_left_image = self.rotate(self.top_left_image, times)
        elif self.top_left_transformation == 'flipped':
            self.top_left_image = self.flip(self.top_left_image)

        if self.top_right_transformation == 'rotated':
            times = random.randint(1, 2)
            self.top_right_image = self.rotate(self.top_right_image, times)
        elif self.top_right_transformation == 'flipped':
            self.top_right_image = self.flip(self.top_right_image)

        # Second, we assing the transformed image to the corresponding bottom images
        self.bottom_left_image = self.top_left_image    # Image.open(os.path.join('letters', f'{self.bottom_left_letter}.png'))
        self.bottom_right_image = self.top_right_image  #  Image.open(os.path.join('letters', f'{self.bottom_right_letter}.png'))
        
        # Now, we apply the transformations to the bottom images
        if self.bottom_left_transformation == 'rotated':
            times = random.randint(1, 2)
            self.bottom_left_image = self.rotate(self.bottom_left_image, times)
        elif self.bottom_left_transformation == 'flipped':
            self.bottom_left_image = self.flip(self.bottom_left_image)



        if self.bottom_right_transformation == 'rotated':
            times = random.randint(1, 2)
            self.bottom_right_image = self.rotate(self.bottom_right_image, times)
        elif self.bottom_right_transformation == 'flipped':
            self.bottom_right_image = self.flip(self.bottom_right_image)

    def display_images(self):
        self.top_left_photo = ImageTk.PhotoImage(self.top_left_image)
        self.bottom_left_photo = ImageTk.PhotoImage(self.bottom_left_image)
        self.top_right_photo = ImageTk.PhotoImage(self.top_right_image)
        self.bottom_right_photo = ImageTk.PhotoImage(self.bottom_right_image)
        
        self.top_left_image_label.config(image=self.top_left_photo)
        self.bottom_left_image_label.config(image=self.bottom_left_photo)
        self.top_right_image_label.config(image=self.top_right_photo)
        self.bottom_right_image_label.config(image=self.bottom_right_photo)
        '''
        self.top_left_image_label.grid(row=0, column=0)
        self.bottom_left_image_label.grid(row=1, column=0)
        self.top_right_image_label.grid(row=0, column=1)
        self.bottom_right_image_label.grid(row=1, column=1)
        '''
        self.top_left_image_label.grid(row=0, column=0, padx=(50, 50), pady=(50,30))     # Add padding to the sides and to the bottom of the top image
        self.bottom_left_image_label.grid(row=1, column=0, padx=(50, 50))               # Add padding to the sides
        self.top_right_image_label.grid(row=0, column=1, padx=(0, 50), pady=(50,30))
        self.bottom_right_image_label.grid(row=1, column=1, padx=(0, 50))

    def rotate(self, img, times):
        return img.rotate(-90 * times)
    
    def flip(self, img):
        return img.transpose(Image.FLIP_LEFT_RIGHT)

    def check_answer(self, answer):
        correct_answer = 0
        if self.bottom_left_transformation == 'rotated' or self.bottom_left_transformation == 'original':
            correct_answer += 1
        if self.bottom_right_transformation == 'rotated' or self.bottom_right_transformation == 'original':
            correct_answer += 1        
        
        self.the_right_answer = correct_answer
        if answer == correct_answer:
            # messagebox.showinfo("Result", "Correct!")
            self.correct_answers += 1
        else:
            # messagebox.showerror("Result", "Incorrect!")
            pass

        self.master.after(300, self.next_question)

    def next_question(self):
        self.question_number += 1
        self.local_questions += 1
        elapsed_time = time.time() - self.start_time
        self.total_time += elapsed_time 
        
        if self.local_questions < self.total_questions:
            # Construct message
            # message = "Elapsed time: {:.2f} seconds\n\n".format(elapsed_time)
            # message += "Top left image: {}\n".format(transformations[self.top_left_transformation])
            # message += "Bottom left image: {}\n".format(transformations[self.bottom_left_transformation])
            # message += "Top right image: {}\n".format(transformations[self.top_right_transformation])
            # message += "Bottom right image: {}\n".format(transformations[self.bottom_right_transformation])

            # Show message
            # messagebox.showinfo("Transformations and Elapsed Time", message)

            # Generate new images
            self.qn_label.config(text="Question No. " + str(self.question_number), font=("Helvetica", 24))
            self.question_label.config(text="How many bottom images are only rotated?", font=("Helvetica", 18))
            self.generate_images()
            self.display_images()
            self.start_time = time.time()
        else:
            self.finish_test()
        
    def finish_test(self):
        elapsed_time = time.time() - self.start_time
        self.total_time = elapsed_time
        ic('Task 5: Spatial total elapsed time: ', elapsed_time)
        # messagebox.showinfo("Time", f"Total time taken: {elapsed_time:.2f} seconds")
        self.master.quit()

def main():
    QUESTIONS = 8
    root = tk.Tk()
    root.geometry("500x640")  
    app = ImageApp(root, QUESTIONS)
    root.mainloop()
    root.quit()

if __name__ == "__main__":
    main()
