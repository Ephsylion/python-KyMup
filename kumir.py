walls = ['|','-','⌜','⌞','⌟','⌝', '\n']

player= 'O'

room_x = 10
room_y = 20

command = ''

alive = False

position_x = 1
position_y = 0        

class Roomer:
    def __init__(self):
        pass
    def makeRoom(self, x, y, spawn_x, spawn_y):
        room = []    
        for i in range(x):
            if len(room) < 1:
                room = room+[walls[2]]
                for a in range(y):
                    room = room+[walls[1]]
                room = room+[walls[5]]
                room = room+[walls[6]]
            elif i == x-1:
                room = room+[walls[3]]
                for b in range(y):
                    room = room+[walls[1]]
                room = room+[walls[4]]
                room = room+[walls[6]]
            else:
                room = room+[walls[0]]
                for c in range(y):
                    if spawn_x == i and spawn_y == c:
                       room = room+[player]
                    else:
                        room = room+['*']
                room = room+[walls[0]]
                room = room+[walls[6]]
        return room
    def prettyMapper(self, map):
        prettyMap = ''
        for i in range(len(map)):
            prettyMap = prettyMap+map[i]
        print(prettyMap)

while command != 'exit':
    line_sep =''
    command = input('>>')
    if 'MAPSIZE_NOW' in command.upper():
        print(f'Map size:\nX: {room_x} blocks\nY: {room_y} blocks\n')
    elif 'RESET' in command.upper():
        if alive == True:
            if input('Are you sure? It remove ALL of your progress (Y/N)>>').upper() == 'Y':
                position_x = 1
                position_y = 0
                print('Posititon was sucsessfully set to X: 1; Y: 1')
        else:
            alive = not alive
            position_x = 1
            position_y = 0
            print('You respawned!')
            pass
    elif alive == True:
        if 'RUNPROG' in command.upper():
                command = command[8::]
                try:
                    file = open(command, 'r')
                    command = file.read()
                    file.close()
                    print('Programm loaded! Please wait while emulation will be ended...')
                except:
                    print('Programm loading failed!')
        for i in range(len(command)):
            line_sep = command[i]
            player = 'O'
            if line_sep.upper() == 'A':
                if position_y < 1:
                    print('YOU CANNOT GO THERE')
                    player = 'X'
                    alive = False
                    break
                #self.position_y = self.position_y+1
                else:
                    position_y = position_y-1                   
            if line_sep.upper() == 'W':
                if position_x-1 == 0 :
                    #self.position_x = self.position_x+1
                    print('YOU CANNOT GO THERE')
                    player = 'X'
                    alive = False
                    break
                else:
                    position_x = position_x-1
            if line_sep.upper() == 'S':
                if position_x+1 == room_x-1:
                    #self.position_x = self.position_x-1 
                    print('YOU CANNOT GO THERE')
                    player = 'X'
                    alive = False
                    break
                else:
                    position_x = position_x+1
            if line_sep.upper() == 'D':
                if position_y+1 > room_y-1:
                    #self.position_y = self.position_y-1
                    print('YOU CANNOT GO THERE')
                    player = 'X'
                    alive = False
                    break
                else:
                    position_y = position_y+1
        Roomer().prettyMapper(Roomer().makeRoom(room_x,room_y,position_x,position_y))
    elif alive == False:
        print('Whoops! Your robot broken! Type "reset" to restart level!')
    #print('INPUT: '+line)