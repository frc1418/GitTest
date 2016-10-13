class Robot():
    def __init__(self):
        self.bender()
        self.hal()
        self.wall_e()
    
    def bender(self):
        print('Kill all humans!')
        
    def hal(self):
        print('I\'m sorry, Dave. I\'m afraid I can\'t do that.')
        
    def c3po(self):
        print('R2-D2, it is you, It Is You !')
        
    def wall_e(self):
        print('W--Wall-E!')
    
    def robo_cop(self):
        print('Dead or alive, you\'re coming with me!')
        
if __name__ == '__main__':
    robo = Robot()