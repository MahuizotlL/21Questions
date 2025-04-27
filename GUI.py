from tkinter import * #GUI
from tkinter import ttk
from PIL import Image, ImageTk
import pygame #sound handling

root = Tk()
root.title("21 Questions")
root.geometry("1200x700")

my_pic = Image.open("90Retro.png")
new_pic = my_pic.resize((1200,500), Image.Resampling.LANCZOS)
bg = ImageTk.PhotoImage(new_pic) #90RETRO

ques = Image.open("21Questions.png")
pic = ques.resize((500,400), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(pic) #21QUESTION

pygame.mixer.init() #sound initialization

class GUI:
    def __init__(self, master):

        s = ttk.Style()
        s.configure('My.TFrame', background=bg)
        s.theme_use("clam")


        bg_frame = ttk.Frame(master,width = 100,height = 100,style='My.TFrame')
        #bg_frame.config()
        bg_frame.pack()

        self.frame = Frame(master) #BUTTON FRAME
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.pack(pady=30,fill="x")

        lower_bg_frame = ttk.Frame(master,style="My.TFrame")
        lower_bg_frame.pack()

        self.question_display = 0 #0 is start screen, 1-21 questions, 22 - calculation/job
        self.social = 0 #sociability  neg=introvert   pos=extrovert
        self.ethic = 0 #workethic    neg=lofty   pos=endurance
        self.schedule = 0 #major      neg=creativity  pos=scientific
        self.nature = 0 #nature      neg=business   pos=humanitarian

        self.bg = Label(bg_frame, image= bg)
        self.bg.place(x=0 , y=0,relwidth=1, relheight=1)
        self.bg.lower()

        self.bg2 = Canvas(lower_bg_frame, width=1200, height=500,background="pink")
        self.bg2.create_image(0,0,image=bg,anchor=NW)
        self.bg2.create_image(380,0 ,image=logo,anchor=NW)
        #self.bg2 = Label(lower_bg_frame, image= bg)
        self.bg2.pack() #works


        #GOOD FONTS
        #Small Fonts
        #"Bahnschrift Light SemiCondensed"
        #Comic Sans MS
        #Segoe Script
        self.lbl = Label(bg_frame,text = "", font = ("Comic Sans MS", 24),width=100)
        self.lbl.pack(pady=0)

        self.btn1 = Button(self.frame, text="Math", font=("Impact", 18), bg = "light coral", height=2, command=self.one_click)

        self.btn2 = Button(self.frame, text="Art", font=("Impact", 18), bg = "light goldenrod", height=2,command=self.two_click)

        self.btn3 = Button(self.frame, text="English", font=("Impact", 18), bg = "light blue", height=2,command=self.three_click)

        self.btn4 = Button(self.frame, text="Science", font=("Impact", 18), bg = "pale green",height=2,command=self.four_click)

        self.nextBtn = Button(bg_frame, text="Start Quiz", font=("Arial", 18), command= self.next_question)
        self.nextBtn.pack(pady = 10)

        #self.prevBtn = Button(master, text="Previous Question", font=("Arial", 18), command=self.prev_question)

    def one_click(self):
        pygame.mixer.music.load("Button.mp3")
        pygame.mixer.music.play(loops=0)

        match self.question_display:
            case 1: #subject: math
                self.schedule += 1
            case 2: #pizza: pepperoni
                self.social += 1
            case 3: #Friends: Ross
                self.schedule += 2
                self.social -= 1
            case 4: #Strength: Buff
                self.ethic += 2
            case 5: #Social: very social
                self.social += 2
            case 6: #music: nirvana
                self.schedule -=1
                self.nature += 1 #human
            case 7: #Reading
                self.social -= 1
            case 8: #Poke Charmander
                self.social += 2
                self.nature -= 1
            case 9: #group 1
                self.social -= 2
                self.ethic += 2
            case 10: #career firefighter/police
                self.ethic += 2
                self.nature += 1
            case 11: #homemade
                self.schedule -= 2
                self.nature += 1
            case 12: #mall
                self.social += 2
                self.nature += 2
            case 13: #consistancy
                self.ethic += 2
                self.nature += 2
            case 14: #all ears
                self.nature += 2
            case 15: #bart
                self.social += 2
                self.ethic -= 1
            case 16: #Book
                self.social -= 1
                self.schedule -= 1
            case 17: #doing stuff
                self.ethic += 1
            case 18: #gym
                self.ethic += 1
            case 19: #pulp
                self.nature -= 1
            case 20: #Human
                self.nature += 1
            case 21: #Human
                self.nature += 1

        self.btn1.config(bg="firebrick3")
        self.lock_all()

    def two_click(self):
        pygame.mixer.music.load("Button.mp3")
        pygame.mixer.music.play(loops=0)

        match self.question_display:
            case 1: #subject: art
                self.schedule -= 2 #creativity
            case 2: #pizza: cheese
                self.ethic -= 1
            case 3: #Friends: Monica
                self.ethic += 1
                self.nature -= 1
            case 4: #Strength: Average
                self.ethic += 1
            case 5: #social: sorta social
                self.social += 1
            case 6: #music: Michael Jackson
                self.schedule -= 1
                self.social += 2
            case 7: #Hobbies: Jamming to Music
                self.schedule -= 1
            case 8: #Pokemon Pikachu
                self.social += 1
                self.schedule -= 1
            case 9:  # Group 2-3
                self.social -= 1
                self.ethic += 1
            case 10: #Career Doctor
                self.schedule += 2
                self.nature += 1
            case 11: #cookbook
                self.schedule += 1
                self.nature += 1
            case 12: #arcade
                self.schedule += 1
                self.social -= 1
                self.ethic -= 1
            case 13: #flexibility
                self.ethic += 1
            case 14: #chiil pill
                self.nature += 1
            case 15: #homer
                self.ethic -= 2
                self.schedule += 1
            case 16: #walkman
                self.ethic += 1
                self.schedule += 1
            case 17: #world
                self.nature += 1
            case 18: #art
                self.schedule -= 1
            case 19: #Breakfast
                self.schedule -= 1
            case 20: #Die
                self.nature -= 1
            case 21: #stored
                self.social -= 1

        self.btn2.config(bg="goldenrod3")
        self.lock_all()

    def three_click(self):
        pygame.mixer.music.load("Button.mp3")
        pygame.mixer.music.play(loops=0)

        match self.question_display:
            case 1: #subject: english
                self.schedule -= 1
            case 2: #pizza: combo
                self.social += 2
            case 3:  # Friends: Joey
                self.social += 2
                self.schedule -= 1
            case 4: # Strength: Not too Strong
                self.ethic -= 1
            case 5: #Social: not very social
                self.social -= 1
            case 6: #Music: 2Pac
                self.schedule -= 1
                self.nature -= 1
            case 7: #Hobbies: Exercise
                self.ethic += 2
            case 8: #Poke: squirtle
                self.social -= 1
                self.ethic -= 1
            case 9: #group: 4-5
                self.social += 1
                self.nature -= 1
            case 10: #Rockstar
                self.schedule -= 2
                self.nature += 1
            case 11: #buy food
                self.nature -= 2
                self.ethic -= 1
            case 12: #work
                self.nature -= 2
                self.ethic += 1
            case 13: #preffered
                self.ethic -= 1
                self.nature -= 1
            case 14: #call rest of gang
                self.nature -= 1
            case 15: #marge
                self.nature += 2
                self.social -= 1
            case 16: #tamagotchi
                self.social += 1
                self.nature += 1
            case 17: #nothing
                self.ethic -= 1
            case 18: #tech
                self.schedule += 1
            case 19: #jurassic
                self.schedule += 1
            case 20: #science chia
                self.schedule += 1
            case 21: #memorized
                self.schedule += 1

        self.btn3.config(bg="slate blue")
        self.lock_all()

    def four_click(self):
        pygame.mixer.music.load("Button.mp3")
        pygame.mixer.music.play(loops=0)

        match self.question_display:
            case 1: #subject: Science
                self.schedule += 2
            case 2: #pizza: veggie
                self.social -= 2
            case 3:  # Friends: Rachel
                self.schedule += 2
                self.social -= 1
            case 4: # Strength: Weak
                self.ethic -= 2
            case 5: #Social: I avoid sociability
                self.social -= 2
            case 6: #Music: I don't like music
                self.schedule += 2
                self.social -= 1
            case 7: #Hobbies: Skatepark
                self.social += 1
                self.ethic += 1
            case 8: #Poke Bulb
                self.social -= 1
                self.schedule -= 1
                self.nature += 1
            case 9: #group 6+
                self.social += 2
                self.nature -= 1
            case 10: #CEO
                self.nature -= 2
                self.social += 1
            case 11: #not go
                self.ethic -= 2
                self.social -= 1
            case 12: #internet
                self.social -= 2
                self.ethic -= 1
            case 13: #work?
                self.schedule -= 1
                self.ethic -= 2
            case 14: #ride solo
                self.nature -= 2
            case 15: #lisa
                self.schedule -= 2
                self.ethic += 1
            case 16: #comfy bed
                self.ethic -= 1
                self.nature -= 1
            case 17: #money
                self.nature -= 1
            case 18: #mattress
                self.ethic -= 1
            case 19: #ferris
                self.ethic -= 1
            case 20: #box
                self.ethic -= 1
            case 21: #social security?
                self.ethic -= 1

        self.btn4.config(bg="sea green")
        self.lock_all()

    def next_question(self):
        self.question_display += 1
        pygame.mixer.music.load("nextques.mp3")
        pygame.mixer.music.play(loops=0)
        self.unlock_all()

        match self.question_display:
            case 1: #Subject
            # USER INITIALIZATION
                self.btn1.grid(row=0, column=0, sticky="W" + "E")
                self.btn2.grid(row=0, column=1, sticky="W" + "E")
                self.btn3.grid(row=1, column=0, sticky="W" + "E")
                self.btn4.grid(row=1, column=1, sticky="W" + "E")
                #self.bg.destroy()
                self.nextBtn.config(text="Next Question")

                self.lbl.config(text="1. What's your favorite subject?")
                #Math    +1 science
                #Art     +2 creative
                #English +1 creative
                #Science +2 science
            case 2: #PIZZA
                self.lbl.config(text="2. What's your favorite pizza?")
                self.btn1.config(text="Pepperoni")#+1 extrovert
                self.btn2.config(text="Cheese")   #+1 lofty
                self.btn3.config(text="Combo")    #+2 extrovert
                self.btn4.config(text="Veggie")   #+2 introvert
            case 3: #FRIENDS
                self.lbl.config(text="3. What 'Friends' Character do you relate to the most?")
                self.btn1.config(text="Ross")   #+2 science +1 introvert
                self.btn2.config(text="Monica") #+1 endurance +1 extrovert
                self.btn3.config(text="Joey")   #+1 creative +1 extrovert
                self.btn4.config(text="Rachel") #+1 science +1 introvert
            case 4: #ETHIC
                self.lbl.config(text="4. How Strong do you think you are?")
                self.btn1.config(text="Hella strong")          #+2 endurance
                self.btn2.config(text="Average Joe")           #+1 endurance
                self.btn3.config(text="I could use some work") #+1 lofty
                self.btn4.config(text="As strong as a beanie baby")           #+2 lofty
            case 5: #SOCIAL
                self.lbl.config(text="5. How Sociable are you?")
                self.btn1.config(text="Im a Party Animal")      #+2 extrovert
                self.btn2.config(text="A consistent yapper") #+1 extrovert
                self.btn3.config(text="A pretty quiet guy")  #+1 introvert
                self.btn4.config(text="I'm a lone wolf")   #+2 introvert
            case 6: #Musician
                self.lbl.config(text="6. Who's your favorite music act?")
                self.btn1.config(text="Nirvana")
                self.btn2.config(text="Michael Jackson")
                self.btn3.config(text="2Pac")
                self.btn4.config(text="I don't like music")
            case 7: #Hobbies
                self.lbl.config(text="7. How do you prefer to spend your free time?")
                self.btn1.config(text="Chillin' out with a cool Book")
                self.btn2.config(text="Jamming to music like i'm about to drop a mixtape")
                self.btn3.config(text="Getting ripped like i'm training for the X-games")
                self.btn4.config(text="Cruisin' at the Skatepark")
            case 8: #pokemon
                self.lbl.config(text="8. Choose your pokemon!")
                self.btn1.config(text="Charmander")
                self.btn2.config(text="Pikachu")
                self.btn3.config(text="Squirtle")
                self.btn4.config(text="Bulbasaur")
            case 9: #group project
                self.lbl.config(text="9. You have a group project at school, how many people do you include?")
                self.btn1.config(text="I only need me")
                self.btn2.config(text="2-3 people")
                self.btn3.config(text="4-5 people")
                self.btn4.config(text="6+ people")
            case 10:  #career (BIG)
                self.lbl.config(text="10. What was your dream job as a kid?")
                self.btn1.config(text="Firefighter/Police Officer")
                self.btn2.config(text="Doctor")
                self.btn3.config(text="Rockstar")
                self.btn4.config(text="CEO")
            case 11:  #potluck
                self.lbl.config(text="11. You're invited to a potluck, do you...")
                self.btn1.config(text="Cook up a rad homemade dish")
                self.btn2.config(text="Read a cookbook and whip something up")
                self.btn3.config(text="Slide by the store and pick up a meal")
                self.btn4.config(text="Chillax at home and ignore the invitation")
            case 12:  #School's pit
                self.lbl.config(text="12. School's out! What do you do?")
                self.btn1.config(text="Go to the mall with the homies")
                self.btn2.config(text="Play at the arcade")
                self.btn3.config(text="Head off to work")
                self.btn4.config(text="Run home and surf the internet")
            case 13:  #work schedule
                self.lbl.config(text="13. What's your ideal work schedule?")
                self.btn1.config(text="I want something consistent")
                self.btn2.config(text="I need some flexibility")
                self.btn3.config(text="I will only work on my preferred days")
                self.btn4.config(text="Work?")
            case 14:  #NATURE
                self.lbl.config(text="14. Your friend needs emotional support, how do you respond?")
                self.btn1.config(text="I'm all ears, help them in any way I can")
                self.btn2.config(text="Help them find their chill pills")
                self.btn3.config(text="Call up the rest of the gang and have them talk to everybody")
                self.btn4.config(text="Tell them they're riding solo on this one")
            case 15: #Simpson
                self.lbl.config(text="15. Which Simpsons character do you relate to the most")
                self.btn1.config(text="Bart") #+2 business +1 extrovert
                self.btn2.config(text="Homer") #+2 lofty +1 science
                self.btn3.config(text="Marge")#+2 humanitarian +1 introvert
                self.btn4.config(text="Lisa ") #+2 creative +1 endurance
            case 16: #Island
                self.lbl.config(text="16. If you were stranded on a deserted island, what would you bring?")
                self.btn1.config(text="Book")  # +1 introverted +1 science
                self.btn2.config(text="Walkman")  # +1 endurance +1 creative
                self.btn3.config(text="Tamagotchi")  # +1 extroverted +1humanitarian
                self.btn4.config(text="A comfy beanbag chair")  # +1 lofty +1business
            case 17: #get out of bed
                self.lbl.config(text="17. What gets you out of bed in the morning?")
                self.btn1.config(text="I always have lots to do")  # +1 endurance
                self.btn2.config(text="Changing the world")  # +1 humanitarian
                self.btn3.config(text="Nothing, I sleep in as long as I can")  # +1 lofty
                self.btn4.config(text="Money.")  # +1 business
            case 18:
                self.lbl.config(text="18. You're opening a new business, what is it gonna be?")
                self.btn1.config(text="Gym")  # +1 endurance
                self.btn2.config(text="Art Studio")  # +1 creative
                self.btn3.config(text="Tech Repair")  # +1 science
                self.btn4.config(text="Mattress Store")  # +1 lofty
            case 19:
                self.lbl.config(text="19. Favorite Movie?")
                self.btn1.config(text="Pulp Fiction")  # +1 business
                self.btn2.config(text="Breakfast Club")  # +1 creative
                self.btn3.config(text="Jurassic Park")  # +1 science
                self.btn4.config(text="Ferris Bueller's Day Off")  # +1 lofty
            case 20:
                self.lbl.config(text="20. How do you take care of your chia pet?")
                self.btn1.config(text="It always flourishes")  # +1 humanitarian
                self.btn2.config(text="I'd rather let it die")  # +1 business
                self.btn3.config(text="I have my own chia pet ecosystem")  # +1 science
                self.btn4.config(text="It's still in the box")  # +1 lofty
            case 21: #
                self.lbl.config(text="21. Where do you keep your social security number?")
                self.btn1.config(text="I keep it in my wallet")  # +1 humanitarian
                self.btn2.config(text="Stored in a safe place")  # +1 introverted
                self.btn3.config(text="I have it memorized")  # +1 science
                self.btn4.config(text="Social Security?")  # +1 lofty
            case 22: #Calculation

                pygame.mixer.music.load("congrats.mp3")
                pygame.mixer.music.play(loops=0)

                values = [('schedule', abs(self.schedule)), ('social', abs(self.social)), ('ethic', abs(self.ethic)), ('nature', abs(self.nature))]
                top_two = sorted(values, key =lambda x: x[1], reverse = True)[:2]
                names = [item[0] for item in top_two]

                trait_1 = self.names(names,0)
                trait_2 = self.names(names,1)
                #print(trait_1, trait_2) #COMMENT OUT

                self.job_picker(trait_1, trait_2)

                self.frame.destroy() #removes selection buttons
                self.nextBtn.destroy()

                self.lbl2 = Label(text=f"Your two most defining traits are {trait_1} and {trait_2}", font=("Comic Sans MS", 24), fg="yellow",bg="blue", width="1200")
                self.lbl2.pack() #traits


    def names(self, names, i):
        if names[i] == "schedule":
            if self.schedule >= 0:
                return "science"
            else:
                return "creative"
        elif names[i] == "social":
            if self.social >= 0:
                return "extrovert"
            else:
                return "introvert"
        elif names[i] == "ethic":
            if self.ethic >= 0:
                return "endurance"
            else:
                return "lofty"
        elif names[i] == "nature":
            if self.nature >= 0:
                return "humanitarian"
            else:
                return "business"
        return None

    def job_picker(self, trait1, trait2):
        self.lbl.config(fg="yellow",bg="blue")
        match (trait1, trait2):
            #SCHEDULE/MIND
            case "science", "extrovert": #default
                self.lbl.config(text="Your job is a Nurse")
            case "science", "introvert":
                self.lbl.config(text="Your job is a Programmer")
            case "science", "endurance":
                self.lbl.config(text="Your job is a Land Surveyor") #better?
            case "science", "lofty":
                self.lbl.config(text="Your job is a Lab Tech")
            case "science", "humanitarian":
                self.lbl.config(text="Your job is a Doctor")
            case "science", "business":
                self.lbl.config(text="Your job is a Sales Analyst")

            case "creative", "extrovert":
                self.lbl.config(text="Your job is a Film Director")
            case "creative", "introvert":
                self.lbl.config(text="Your job is a Photographer")
            case "creative", "endurance":
                self.lbl.config(text="Your job is a Baker")
            case "creative", "lofty":
                self.lbl.config(text="Your job is a Artist")
            case "creative", "humanitarian":
                self.lbl.config(text="Your job is a Musician")
            case "creative", "business":
                self.lbl.config(text="Your job is a Graphic Designer")

            #SOCIAL
            case "extrovert", "science":
                self.lbl.config(text="Your job is a Teacher")
            case "extrovert", "creative":
                self.lbl.config(text="Your job is a Actor")
            case "extrovert", "endurance":
                self.lbl.config(text="Your job is a Police")
            case "extrovert", "lofty":
                self.lbl.config(text="Your job is a Customer Service Agent")
            case "extrovert", "humanitarian":
                self.lbl.config(text="Your job is a Social Work")
            case "extrovert", "business":
                self.lbl.config(text="Your job is a Advertiser")

            case "introvert", "science":
                self.lbl.config(text="Your job is a Researcher")
            case "introvert", "creative":
                self.lbl.config(text="Your job is a Video Editor")
            case "introvert", "endurance":
                self.lbl.config(text="Your job is a Electrician")
            case "introvert", "lofty":
                self.lbl.config(text="Your job is a Librarian")
            case "introvert", "humanitarian":
                self.lbl.config(text="Your job is a Pharmacist")
            case "introvert", "business":
                self.lbl.config(text="Your job is a Auditor")

            #ETHIC
            case "endurance", "science":
                self.lbl.config(text="Your job is a Engineer")
            case "endurance", "creative":
                self.lbl.config(text="Your job is a Culinary Arts")
            case "endurance", "extrovert":
                self.lbl.config(text="Your job is a Personal Trainer")
            case "endurance", "introvert":
                self.lbl.config(text="Your job is a Truck Driver")
            case "endurance", "humanitarian":
                self.lbl.config(text="Your job is a Fire Fighter")
            case "endurance", "business":
                self.lbl.config(text="Your job is a Stockbroker")

            case "lofty", "science":
                self.lbl.config(text="Your job is a Web Developer")
            case "lofty", "creative":
                self.lbl.config(text="Your job is a Singer")
            case "lofty", "extrovert":
                self.lbl.config(text="Your job is a Secretary")
            case "lofty", "introvert":
                self.lbl.config(text="Your job is being Unemployed, do better")
            case "lofty", "humanitarian":
                self.lbl.config(text="Your job is a Human Resources Worker")
            case "lofty", "business":
                self.lbl.config(text="Your job is a Office Job")

            #NATURE
            case "humanitarian", "science":
                self.lbl.config(text="Your job is a Physical Therapist")
            case "humanitarian", "creative":
                self.lbl.config(text="Your job is a Author")
            case "humanitarian", "extrovert":
                self.lbl.config(text="Your job is a Therapist")
            case "humanitarian", "introvert":
                self.lbl.config(text="Your job is a Journalist")
            case "humanitarian", "endurance":
                self.lbl.config(text="Your job is a Disaster Relief")
            case "humanitarian", "lofty":
                self.lbl.config(text="Your job is a Clergy")

            case "business", "science":
                self.lbl.config(text="Your job is a Economist")
            case "business", "creative":
                self.lbl.config(text="Your job is a Beautician")
            case "business", "extrovert":
                self.lbl.config(text="Your job is a Salesperson")
            case "business", "introvert":
                self.lbl.config(text="Your job is a Journalist")
            case "business", "endurance":
                self.lbl.config(text="Your job is a Construction")
            case "business", "lofty":
                self.lbl.config(text="Your job is a Manager")

    def lock_all(self):
        self.btn1["state"] = "disabled"
        self.btn2["state"] = "disabled"
        self.btn3["state"] = "disabled"
        self.btn4["state"] = "disabled"

    def unlock_all(self):
        self.btn1["state"] = "normal"
        self.btn2["state"] = "normal"
        self.btn3["state"] = "normal"
        self.btn4["state"] = "normal"
        self.btn1.config(bg="light coral")
        self.btn2.config(bg="light goldenrod")
        self.btn3.config(bg="light blue")
        self.btn4.config(bg="pale green")

GUI(root)
root.mainloop()