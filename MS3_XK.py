#-------------------------------------------------------------------------------
#                                 Xavier Kidston
#                                  MileStone 3
#-------------------------------------------------------------------------------
'''
The purpose of this code is to make the game towers of hanoi with all rules and
fun stuff
'''


#This imports graphics all, and time functions
from graphics import *
import time


#these establish constant variables
WIN_W, WIN_H = 500, 400
BASE = 350
POST_SP = 125
POST_W = 13
POST_H = 200


#these establish global variables
win = None
posts = []
disks = []
msg_main = ''
msg_secondary = ''
clicks = 0
moves_list = []
N_entry = [3, None, None]
btn_quit = None
btn_reset = None
btn_auto = None
btn_playback = None




'''
I couldn't read my code easily, because of my commenting style. 
All of my comments were green, which made it hard to see where new functions
started, so I changed all my prior to function comments to this style,
as to fix that issue I was having. 
'''




'''
Function: Creates the disks
Parameters: None
Returns: Num_of_disks - the amount of disks
'''
def create_disks():
    global disks
    
    #Establish variables for later use
    disk_list = []
    text = ''
    Num_of_disks = N_entry[0]
    height = 20
    Ulx = 62
    Uly = 330
    width = 125
    colour = 'purple'
    
    
    #Makes a for loop for each disk, and times it to look good
    for i in range(1, Num_of_disks + 1):
        text = str(N_entry[0] - i + 1)
        disk, label = create_button(win, Ulx, Uly, width, height, text, colour)
        Uly += -20
        Ulx += 5
        width += -10
        time.sleep(1 / 6)
        disk_list.append(N_entry[0] - i + 1)
        disk_list.append(disk)
        disk_list.append(label)
        disk_list.append('A')
        disks.append(disk_list)
        disk_list = []
    
    #Gets rid of posts[0].pop(3)
    posts[0].pop(3)
    
    #runs through each disk in disks, and then appends them onto post A
    for disk in disks:
        disk_list.append(disk[0])
    posts[0].append(disk_list)
    
    return Num_of_disks




'''
Function: To check if the disk is the top of the stack, and if it's then make it
          green, if it isn'tmake it red
Parameters: Disk - a single disk from the list of disks(the one that was clicked)
Returns: None
'''
def proc_disk(disk):
    
    #Establishes a counter
    counter = 0
    
    for post in posts:   #Checks through each post in posts
        counter += 1
        
        #Checks if the disk is on the post
        if post[0] == disk[-1]:
            
            #Checks if the disk clicked is the top of the stack
            if post[3][-1] == disk[0]:
                counter += -1
                msg_main.setText("DISK: " + str(disk[0]))
                disk[1].setFill("green")
                time.sleep(1 / 2)
                disk[1].setFill("purple")
                point = win.getMouse()
                wait_move(point, disk, counter)
                break
            
            #Informs the user it's a bad move
            else:
                msg_main.setText("NO MOVE")
                disk[1].setFill("red")
                time.sleep(1/2)
                disk[1].setFill("purple")




'''
Function: To change the color and display when a post is clicked on
Parameters: Post - the post that was clicked on
Returns: None
'''
def proc_post(post):
    
    #changes the color of the post, and then back to the original color
    #as well as saying which post was clicked
    msg_main.setText("POST: " + post[0])
    post[1].setFill("yellow")
    time.sleep(1 / 2)
    post[1].setFill("brown")
    
    #Checks if the post clicked has a disk_id_list longer than zero, and then
    #uses the top of the stack disk to run through the code
    if len(post[-1]) > 0:
        popped = post[-1].pop()
        post[-1].append(popped)
        the_disk = disks[3 - popped]
        proc_disk(the_disk)




'''
Function: Checks if the disk you're moving will be the largest number/smallest
          disk
Parameters: num - the number of the post you want to move the disk too
            disk - the disk you want to move
Returns: True or False dependant on if the move follows the rules or doesn't
'''
def Hanoi_rules(num, disk):  
    
    #Checks if the end number of the wanted posts ID is lower, then moves it if
    #it is. If the disk is a smaller number, it tell you it's an impossible move
    if len(posts[num][-1]) > 0:
        if disk[0] < posts[num][-1][-1]:
            return True
        
        #If the move isn't allowed says NO MOVE! as the move isn't allowed, and
        #returns false
        else:
            msg_main.setText("NO MOVE!")
            time.sleep(1 / 2)
            return False
    
    #If the length of the disk_id_list at the end of posts is 0, returns true
    elif len(posts[num][-1]) == 0:
        return True




'''
Function: to wait for the person to make another click on a post, and then move 
          the disk, the label, and append the label onto the new list
Parameters: point - the point the user clicks the second time
            disk - a single disk from the disks list that was clicked
            num - the source post's number in the list
Returns: None
'''
def wait_move(point, disk, num):
    
    movement = []
    
    # If you click a post after clicking a disk, it says true
    if post_check(point) == True:
        numb = posts.pop()
        
        # checks if the post clicked is the same as the post the disk is on
        if numb == num:
            msg_main.setText("NOT A VALID MOVE")
        
        #If the post clicked is not the same as the post the disk is on, movesit
        elif numb != num:
            if Hanoi_rules(numb, disk) == True:
                movement = [(disk[0] - 1), numb, num]
                da_move(disk, numb, num)       
                string = ("DISK: " + str(disk[0]) + ", MOVED TO " + str(posts[numb][0])) 
                msg_main.setText(string)
                time.sleep(1)
                moves_list.append(movement)
                
            
    #If the thing clicked after the disk click is not a post, returns coords
    #of the click
    else:
        x = point.getX()
        y = point.getY()
        string = ("(" + str(x) + ",", str(y) + ")")
        msg_main.setText(string)
        time.sleep(1 / 2) 




'''
Function: To move the disk and label to another post 
Parameters: Disk - the disk you want to move 
            numb - the number of the target post that they want
                   to move the disk to
            num - the number of the post that you're moving the disk from
Returns: None
'''
def da_move(disk, numb, num):
    
    #A valid click gets added
    global clicks
    clicks += 1
    msg_secondary.setText(clicks)
    
    #Establishes the two variables, numB being destination - current,
    #dest_length being the len of the destinations list
    numB = numb - num
    dest_length = len(posts[numb][-1])
    
    #Gets the bottom left coord of the rectangle of the disk
    Bly = disk[1].getP2()
    Bly = Bly.getY()
    diff = BASE - Bly
    dy = -(20 * dest_length) + diff
    dx = numB * POST_SP
    
    #Moves the label and the disk itself
    disk[1].move(dx, dy)
    disk[2].move(dx, dy)
    
    #Changes what post the disk is associated with, and updates all the showings
    #beneath the posts
    disk.pop()
    disk.append(posts[numb][0])
    
    posts[numb][-1].append(posts[num][-1].pop())
    show_post_info()    

    
    
    
'''
Function: To apply the list changes and undraw the old lists, then write 
          the new ones
Parameters: None - but uses a global variables
Returns: None
'''
def show_post_info():
    
    #unwrites and rewrites every single posts info
    for post in posts:
        post[2].undraw()        
        post[2] = Text(Point(((posts.index(post)+1) * 125), BASE + 25),\
                       post[0] + "\n" + str(post[3]))
        post[2].setSize(12)
        post[2].draw(win)
    
    
    

'''
Function: Runs a helper function for create_posts to make it shorter, also
          creates a post on a window and in list, and appends it to posts
Parameters: the post_name - The name of the post
            color - The color you want the post
            height -the height of the post
            x - The the x for start
            x1 - the end
            x2 - text location
Returns: None
'''
def posts_helper(post_name, color, height, x, x1, x2):
    
    #Establishes variables to be appended and used by other functions
    #also draws the rectangle as well as setting it's color
    disk_id = []
    post = []
    rect = Rectangle(Point(x, height), Point(x1, BASE))
    rect.setFill(color)
    rect.draw(win)
    post.append(post_name)
    post.append(rect)
    text = post[0] + "\n" + str(disk_id)
    Text = info_create(win, x2, 375, text)    
    post.append(Text)
    post.append(disk_id)
    posts.append(post)
    
        
        
        
'''        
Function: Creates 3 posts named A, B, C, and appends them each to a list,
                 and then appends those lists to another lists
Parameters: None
Returns: None
'''
def create_posts():
    
    #these set up lists and variables, and calls a helper function to make
    #the posts
    height = BASE - POST_H
    color = "brown"
    posts_helper("A", color, height, 118, 132, 125)
    posts_helper("B", color, height, 243, 257, 250)
    posts_helper("C", color, height, 368, 382, 375)
    
    
    
    
'''    
Function: Creates the pillars, base, quit & reset buttons, and the entry point 
          for how many disks
Parameters: None
Returns: btn_quit - the quit button
         btn_reset - the reset button
         entry - the entry point
         btn_auto - the auto button
'''
def Hanoi_create():
    
    #Imports N_entry just for safety
    global N_entry
    
    #Creates the quit button & reset button by calling create_button, and also 
    #the entry point appending it to N_entry for global use
    btn_quit = create_button(win, 25, 25, 55, 35, "QUIT", None)
    btn_reset = create_button(win, 420, 25, 55, 35, "RESET", None) 
    btn_auto = create_button(win, 420, 90, 55, 35, "AUTO", None)
    btn_playback = create_button(win, 25, 90, 55, 35, "", None)
    btn_playback[0].setOutline("white")
    enter = Entry(Point(447, 75), 2)
    enter.draw(win)        
    Text = info_create(win, 425, 75, "N:")
    
    #Creates the base, and makes it all black, and then draws it
    base = Rectangle(Point(25, BASE), Point(475, (BASE + 1)))
    base.setFill("black")
    base.setOutline("black")
    base.draw(win)
    
    #Calls create_posts() and create_disks() to make all the posts and disks
    create_posts() 
    Hanoi_reset()
    
    #creates the entry object and text for Hanoi_reset to later use
    N_entry.pop(1)
    N_entry.insert(1, Text)
    N_entry.pop(2)
    N_entry.insert(2, enter)        
    
    return btn_quit, btn_reset, enter, btn_auto, btn_playback




'''
Function: Calls the entry box from hanoi create, to get the writing in that box,
          and then creates text using that writing, and inserts both things into
          the N_entry list, and displays "RESET\nN:()#"
Parameters: None
Returns: Num_of_disks - the amount of disks there is, which is also 
                        available in N_entry[0], but to heck with it. I'm wild.
'''
def Hanoi_reset():   
    
    #Clears each disk_id list for each post
    for post in posts:
        post[-1].clear()
    
    #If the text is not empty, which is all the time except when you first
    #start the code
    if N_entry[2] != None:
        
        ent = N_entry[0]
        
        #This tries to get the number in the box, if it doesn't exist it just
        #gives the number used prior to hitting RESET or AUTO
        try:
            #This calls the enter box that we made in Hanoi_create()
            enter = N_entry[2]
            
            #Gets the text object from the box
            entry = enter.getText()
            entry = int(entry)  
            
        except ValueError:
            entry = ent
        
    #if the text is empty, entry = 3, because it's only ever empty when you
    #start the program
    elif N_entry[2] == None:
        entry = 3
    
    
    #This uses a while loop to check if enter is greater than 9, if it is, 
    #it remainders it from 10
    while entry > 9:
        entry = entry % 10
    if entry == 0:
        entry = 1
    
    #This pops that first thing in the list, and then inserts the new entry 
    #into its place
    N_entry.pop(0)
    N_entry.insert(0, entry)
    
    #This establishes the text, then pops the second thing in the list, 
    #and inserts the text into its place
    num_of_disks = create_disks()
    
    #show_post_info() to update all the information in the window
    show_post_info()
    
    return num_of_disks
    
    
    
    
'''    
Function: Creates a text in a space
Parameters: Win - The window
            x - the x coord
            y - the y coord
            text - the text you want to usue
Returns: info - the text object
'''
def info_create(win, x, y, text):
    
    #Creates the text with coords in the window
    info= Text(Point(x, y), "")
    info.setText(text)
    info.draw(win)
    
    return info




'''
Function: Creates a button
Parameters: Win - the window
            Ulx - upper left x
            Uly - upper left y
            width - how wide you want the button
            height - how tall you want the button
            text - the text you want for the button
            colour - the colour of the button you want
Returns: [rectangle, label] - a tuple containing both rectangle and label
'''
def create_button(win, Ulx, Uly, width, height, text, colour):
    
    #Creates a rectangle for the button
    rectangle = Rectangle(Point(Ulx, Uly), Point(Ulx+width, Uly+height))
    rectangle.setFill(colour)
    rectangle.draw(win)
    
    #Creates a text label on the rectangle
    label= Text(Point(Ulx + width//2, Uly + height//2), text)
    label.setSize(12)
    label.draw(win)
    
    return [rectangle, label]




'''
Function: Checks if it's in a rectangle
Parameters: Point - x, y coords of a click
            Button - the button itself
Returns: A comparison checking if clicks within points
'''
def in_rectangle(point, button):
    
    #Gets the top left and bottom right positions
    top_left=button.getP1()
    bottom_right= button.getP2()
    
    #Returns if the click is within the rectangle
    return(top_left.getX() <= point.getX() <= bottom_right.getX() and \
            top_left.getY() <= point.getY() <= bottom_right.getY())
    
    
    
    
'''           
Function: Runs a for loop to check if a click was within the amount of disks
Parameters: Point - The point the user clicked
Returns: True or False dependant if the user clicked a disk
'''
def disk_check(Point):
    
    #Checks through each disk if it was clicked and appends which disk was
    #clicked, then returns true
    for i in range(len(disks)):
        if in_rectangle(Point, disks[i][1]):
            disks.append(i)
            return True
    
    #Returns false if no disk was clicked
    return False




'''
Function: To check if a click is in the posts
Parameters: Point - the location the user clicked
Returns: True or False, dependant on if the user clicked a post
'''
def post_check(Point):
    
    #Checks through each post if it was clicked and appends which post was
    #clicked, then returns true
    for i in range (len(posts)):
        if in_rectangle(Point, posts[i][1]):
            posts.append(i)
            return True
        
    #returns false if no post was clicked
    return False




'''
Function: Uses a global list to run through each item in that list to redo moves
          the user entered
Parameters: None
Returns: None
'''
def playback():
    
    #Runs hanoi_reset() and sleeps it for half a second
    entry = Hanoi_reset()       
    
    #for each move in the move_list, it makes the disk, the destination(numb),
    #and the source(num), then runs da_move and only makes 1 move per second
    for i in range(len(moves_list)):
        move = moves_list[i][0]
        disk = disks[move]
        numb = moves_list[i][1]
        num = moves_list[i][2]
        
        da_move(disk, numb, num)
        time.sleep(1)
    
    #Clears the moves_list, and undraws the button and word on the button
    moves_list.clear()
        



'''
Function: To run through Hanoi auto, with 1 disk moved a 1 / 6 of a second
          using a recursion method.
Parameters: pegs - the disk id lists of each post
            start - the peg all the disks start on (A)
            target - where you want all the pegs to end up at (C)
            n - the number of posts
Returns: None
'''
def AUTO(pegs, start, target, n):
    
    global clicks
    
    
    #Checks if a click happened
    point = win.checkMouse()
    
    #if a click did happen, pauses the program
    if point != None:        
        if in_rectangle(point, btn_auto[0]):
            btn_auto[1].setText('PLAY')
            
            try:
                win.getMouse()
                btn_auto[1].setText('PAUSE')
            except GraphicsError:
                None
    

    
    #At the base of the recursion, makes a move, tells you the move, 
    #and adds to the globa variable clicks so it can say how many clicks
    #it would take in perfect conditions        
    if n == 1:
        clicks += 1
        msg_secondary.setText(clicks)        
        iteration = pegs[start][-1]
        disk = disks[N_entry[0] - iteration]
        da_move(disk, target, start)
        string = ("disk", str(pegs[target][-1]), 'from', \
                  str(posts[start][0]), "to", str(posts[target][0]))
        msg_main.setText(string)        
        show_post_info()     
        time.sleep(1 / 10)    
        
    #If it's not at the base of the recursion runs move from 
    #(A -> C(kind of)) then from A -> B,
    #then from C -> B, again, just kind of
    else:
        aux = 3 - start - target # start + target + aux = 3
        AUTO(pegs, start, aux, n - 1)
        AUTO(pegs, start, target, 1)
        AUTO(pegs, aux, target, n - 1)       
            
            
            

'''
Function: Combines all other functions and runs a GUI loop
Parameters: None
Returns: None 
'''
def main():
    
    #These allow me to bring in global variables and edit them
    global moves_list, win, posts, disks, clicks, msg_main, msg_secondary, N_entry, btn_quit, btn_reset, btn_auto, color
    
    #these make the window, house, resetbutton, quit button, auto button,
    #color the house, and name the window
    win = GraphWin("Hanoi Towers (5) (C) 2018 by Xavier Kidston", WIN_W, WIN_H)
    msg_main = info_create(win, 250, 50, "GREETINGS!")
    msg_secondary = info_create(win, 250, 75, 0)
    btn_quit, btn_reset, enter, btn_auto, btn_playback = Hanoi_create()
    clicks = 0
    
    
    #Runs the GUI loop
    while True:
        
        #Establishes a list of colors for flashing upon a win
        colors = ["red", "black"] 
        minimum_number_of_clicks = ((2 ** N_entry[0]) - 1)
        
        
        #Checks post C's ID list is as many numbers as the user wanted to see if
        #the user won, and then checks if they did it within the minimum number
        #of clicks, and flashes CONGRATULATIONS!! and PERFECT!! (in red)
        #as well as creates a playback button to be used
        if len(posts[2][-1]) == N_entry[0]:      
            btn_playback[1].setText("PLAYBACK")
            btn_playback[0].setOutline("black")
            msg_main.setText("CONGRATULATIONS !!")
            msg_main.setFill(colors[0])
            msg_main.setOutline(colors[0])            
            if clicks == minimum_number_of_clicks:
                for i in range(5):
                    msg_main.setText("CONGRATULATIONS !!")
                    msg_main.setFill(colors[0])
                    msg_main.setOutline(colors[0])
                    time.sleep(1 / 10 * 3)
                    msg_main.setText("PERFECT!!")
                    msg_main.setFill(colors[1])
                    msg_main.setOutline(colors[1])
                    time.sleep(1 / 10 * 3)    
        
        
        #Tries getting a mouse click, if there isn't one, it just keeps 
        #trying really. 
        try:
            point = win.getMouse()
            
        except GraphicsError:
            return 
        
        
        #Checks if the click is in a disk, by running a function that checks 
        #if the click is any of the disks
        if disk_check(point) == True:
            num = disks.pop()
            disk = disks[num]
            msg_secondary.setText(clicks)            
            proc_disk(disk)   
            
        
        elif in_rectangle(point, btn_playback[0]):
            
            #Undraws all the disks and labels, and then clears the disks lists
            for i in range(len(disks)):
                disk = disks[i][1]
                disk.undraw()
                label = disks[i][2]
                label.undraw()  
            
            #for i in range(len(disks)):
             #   disk = disks[i]
              #  da_move(disk, 0, 2)
                
            
            disks.clear()
            clicks = 0
            time.sleep(1 / 2)
            
            #runs playback
            playback()
        
        
        #Checks if the click is in the auto button, and then 
        #runs the approapriate code
        elif in_rectangle(point, btn_auto[0]):
            btn_auto[1].setText("PAUSE")
            pegs = []
            
            #Removes all the disks and their labels
            for i in range(len(disks)):
                disk = disks[i][1]
                disk.undraw()
                label = disks[i][2]
                label.undraw()  
            disks.clear()
            
            #Runs hanoi_reset() and sleeps it for half a second
            entry = Hanoi_reset()             
            time.sleep(1 / 2)
            
            #Sets clicks to 0 for the loop so you can see how many moves it 
            #takes to complete the auto loop
            clicks = 0
            
            #Uses the posts I_D lists to create a new list of all of them 
            pegs.append(posts[0][-1])
            pegs.append(posts[1][-1])
            pegs.append(posts[2][-1])
            
            #Runs auto and shows clicks at the end
            AUTO(pegs, 0, 2, N_entry[0])
            msg_secondary.setText(clicks)            
            

        #Checks if the mouse click is in the quit button, and then says BYE BYE!
        #Then needs another click to close the window
        elif in_rectangle(point, btn_quit[0]):
            msg_main.setText("BYE BYE!")
            time.sleep(1 / 2)
            clicks = 0
            
            #Gets another click, and then closes the window
            try:
                point = win.getMouse()
                win.close()     
                
            #returns if there is a graphics error
            except GraphicsError:
                return
            
            #Resets these global variables so if you open it up again without
            #running it, it still starts fresh
            N_entry = [3, None, None]
            disks = []          
        
        
        #Checks if the btn click is in reset, if it is, calls on the 
        #function Hanoi_reset
        elif in_rectangle(point, btn_reset[0]):
            for i in range(len(disks)):
                disk = disks[i][1]
                disk.undraw()
                label = disks[i][2]
                label.undraw()  
                
            #makes sure the btn_auto label is AUTO, clears the disks, and runs
            #hanoi_reset(), and makes the text object
            btn_auto[1].setText("AUTO")
            disks.clear()
            entry = Hanoi_reset()
            text = "RESET\nN: " + str(entry)
            
            #this makes the main message "RESET\n N: (Entered Number)", and
            #resets the number of clicks to zero, and displays the zero clicks
            msg_main.setText(text)             
            time.sleep(1 / 2)
            clicks = 0
            msg_secondary.setText(clicks)
                
                
        #Post_check is a function I made to cut down on elifs that works 
        #like disk_check
        elif post_check(point) == True:
            
            num = posts.pop()
            proc_post(posts[num])
            msg_secondary.setText(clicks)
            
            
        #Tells you the x and y coords of where clicked if you didn't click 
        #in a rectangle
        else:
            x = point.getX()
            y = point.getY()
            string = ("(" + str(x) + ",", str(y) + ")")
            msg_main.setText(string)
            time.sleep(1 / 2)            