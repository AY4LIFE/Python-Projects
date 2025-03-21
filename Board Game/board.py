#  Hi My name is Ayomide Akinsanya and welcome to my code. Let me walk you through
class Board:
    def __init__(self):  # In my init method, I made all these random instances 0. You will find out why?
        self.game_grid = None
        self.L = 0
        self.W = 0
        self.board = None
        self.steps = 0
        self.players = 0
    #  Also, note that these try/excepts are done to prevents crashing of the game
    def get_board(self):
        try:
            if self.game_grid == None: # If my self.board has not been created originally
                with open("map.txt") as self.mapFile:  # with my map.txt file opened, here is what will happen
                    self.game_grid = []  # self.game_grid will be a list
                    lines = self.mapFile.readlines()  # the lines variables contain all the lines in the map.txt file
                    for line in lines:
                        v = []  # v is my sub-list
                        for column in line:  # for each character in the line
                            if column != "\n":  # As long as the character is not "\n"
                                v.append(column)  # Add these columns to the sub-list
                            else:
                                pass
                        self.game_grid.append(v)  # Then append the sub-list to the main list
                with open("players.txt") as self.playerFile:  # With my players.txt file opened,
                    i = 0
                    for line2 in self.playerFile:  # For every line in the players file
                        i += 1
                        if 4 >= i >= 1:  # I had this increased and validated so that only 4 players can be in the game
                            parts = line2.strip().split()  # The line will be divided in two parts seperated by a space
                            if len(parts) == 2:  # If the total parts broken is 2
                                row_idx, col_idx = int(parts[0]), int(parts[1])  # The first is row and second column
                                if 0 <= row_idx < len(self.game_grid) and 0 <= col_idx < len(self.game_grid[0]):
                                    self.game_grid[row_idx][col_idx] = "P"  # The positions will be called "P"

                with open("exit.txt") as self.exitFile:  # With my exit file opened
                    for line3 in self.exitFile:  # for every line in the file
                        parts2 = line3.strip().split()  # Like earlier, broken into two parts
                        if len(parts2) == 2:
                            row2, column2 = int(parts2[0]), int(parts2[1])
                            if 0 <= row2 < len(self.game_grid) and 0 <= column2 < len(self.game_grid[0]):
                                self.game_grid[row2][column2] = "E"  # But this time, position is called "E"
            return self.game_grid  # The overall game_grid will be returned
        except Exception:
            print(Exception)
            exit()

    def update(self, direction):
        grid = self.game_grid.copy()  # I made the variable grid a copy of the game_grid for editing
        try:
            if direction == "L":  # If the direction is L
                for row in grid:  # For every row in the grid
                    for i in range(1, len(row)):  # For every position in the row
                        if row[i] == "P":  # If P is found:
                            if row[i - 1] == "#":  # If the row before it is a wall
                                row[i] = " "  # Then "P" should turn into a space
                                self.L += 1  # And there will be a counter for dead players
                            elif row[i - 1] == "E":  # Else if it's E
                                row[i] = " "
                                self.W += 1  # Same but counter for escaped players
                            elif row[i - 1] == "P":  # But if it's a fellow "P"
                                continue  # Just skip
                            elif i == 0:  # Also if the player is on the edge of the board
                                continue  # Just skip
                            else:  # If it passes all the validations,
                                row[i-1], row[i] = row[i], row[i - 1]  # Move what's in front of the back.

                self.steps += 1  # Steps keep increasing by 1
            elif direction == "R":  # If direction is right, similar approach is applied
                for row in grid:
                    for i in range(len(row)-1, -1, -1):  # However, I want it to iterate backward
                        if row[i] == "P" and i < len(row) - 1:
                            if row[i+1] == "#":
                                row[i] = " "
                                self.L += 1
                            elif row[i+1] == "E":
                                row[i] = " "
                                self.W += 1
                            elif row[i+1] == "P":
                                continue
                            elif i == 15:
                                continue
                            else:
                                row[i], row[i+1] = row[i+1], row[i]  # This time, what's at the back, move in-front

                self.steps += 1
            elif direction == "U":  # Now, if the direction is up
                for column in range(len(grid[0])):  # For each column in the grid
                    for row in range(len(grid)):  # For each row in the grid,
                        if grid[row][column] == "P":  # If "P" is found:
                            if row == 0:  # If the position they found it is at the edge
                                continue  # Just skip
                            elif grid[row - 1][column] == "#":  # If what is in front of it is a wall
                                grid[row][column] = " "  # The "P" turns into a space
                                self.L += 1  # Our dead counter is still here
                            elif grid[row - 1][column] == "E":  # If what is in front of it is an exit
                                grid[row][column] = " "  # Same but now escape counter
                                self.W += 1
                            elif grid[row - 1][column] == "P":  # If what's in front of it is a fellow player
                                continue  # Just skip
                            else:  # If all the validations have been met,
                                grid[row][column], grid[row - 1][column] = \
                                            grid[row - 1][
                                                column], grid[row][column]
    # The position directly in front of the player and the player will exchange
                self.steps += 1
            elif direction == "D":  # Now for direction "D"
                for column in range(len(grid[0])):
                    for row in range(len(grid) - 1, -1, -1):  # Same thing but now we iterate backward
                        if grid[row][column] == "P":
                            if row == 11:
                                continue
                            if grid[row + 1][column] == "#":
                                grid[row][column] = " "
                                self.L += 1
                            elif grid[row + 1][column] == "E":
                                grid[row][column] = " "
                                self.W += 1
                            elif grid[row + 1][column] == "P":
                                continue
                            else:
                                grid[row][column], grid[row + 1][column] = \
                                    grid[row + 1][
                                        column], grid[row][column]
    # The position directly behind the player and the player will exchange
                self.steps += 1
                self.game_grid = grid  # The game_grid will now be updated to what the grid look like.
        except Exception:
            print(Exception)
            exit()


    def get_state(self):
        try:
            with open("players.txt") as player:  # For get_state, we will open the players file again
                self.players = len(player.readlines())  # self.players will be now many players by line
                if self.players > 4:  # To align with previous validation, if greater than 4
                    self.players = 4  # self.players is 4
                if (self.W > 0 and self.L == 0) and self.players - (self.W + self.L) == 0:
                    return 1  # If every player reach the exit, return 1
                elif (self.W == 0 and self.L > 0) and self.players - (self.W + self.L) == 0:
                    return 2  # If every player died on the wall, return 2
                elif (self.W > 0 and self.L > 0) and self.players - (self.W + self.L) == 0:
                    return 3  # If some players died and escaped, return 3
                else:
                    return 0  # Else, game is still going on
        except Exception:
            print(Exception)
            exit()

    def save_map(self):
        try:
            with open("save.txt", "w") as saveFile:  # I created a file and called it save.txt as SaveFile.
                v = []
                for row in self.game_grid:  # For each row in the game_grid
                    v.append(row)  # It should be appended to v
                reincarnated = v  # I then renamed it as reincarnated
                for row in reincarnated:  # For each row in reincarnated
                    output = ""
                    for column in row:  # For each column in row
                        if len(column) == 0:  # If the length of the column is 0
                            output += " " + ""  # It should add a space
                        else:  # Else, add the string of the column
                            output += str(column) + ""
                    output += "\n"
                    saveFile.write(output)  # The saveFile will write these output
                saveFile.write("Dead: " + str(self.L) + "\n")
                saveFile.write("Escaped: " + str(self.W) + "\n")
                saveFile.write("Players: " + str(self.players) + "\n")
                saveFile.write("Steps: " + str(self.steps) + "\n")
        #  I also wrote the number of dead players, escaped players, overall players and number of steps
        except Exception:
            print(Exception)
            exit()



    def load_map(self):
        try:
            with open("save.txt", "r") as save_File:  # With save.txt now opened for reading
                self.game_grid = []  # self.game_grid now has an empty list
                lines = save_File.readlines()
                for line in lines:  # For each line in the lines
                    if line.startswith("#") or line.startswith(" "):  # If the line with "#" or a space
                        v = []  # v is a sublist
                        for column in line:  # For each column in the line
                            if column != "\n":
                                v.append(column)  # the columns should be appended to v
                        self.game_grid.append(v)  # Then the sublist is appended to the game_grid
                    elif line.startswith("Steps: "):  # If the line starts with steps
                        self.steps = int(line.split(":")[1])  # self.steps will then be the outcome of this

                    elif line.startswith("Dead: "):  # If the line starts with dead
                        self.L = int(line.split(":")[1])  # self.L will the outcome of this

                    elif line.startswith("Players: "):  # If the line starts with players
                        self.players = int(line.split(":")[1])  # self.players will be the outcome of this

                    elif line.startswith("Escaped: "):  # If the line starts with escaped
                        self.W = int(line.split(":")[1])  # self.W will be the outcome of this
        except:
            print(Exception)
            exit()

    def get_steps(self):
        try:
            return self.steps  # This method will return the number of steps
        except Exception:
            print(Exception)
            exit()