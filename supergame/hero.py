key_switch_camera = 'c' # камера прив'язана до героя чи ні
key_switch_mode = 'z' # можна проходити крізь перешкоди чи ні


key_forward = 'w'   # крок вперед (куди дивиться камера)
key_back = 's'      # крок назад
key_left = 'a'      # крок вліво (вбік від камери)
key_right = 'd'     # крок вправо
key_up = 'e'      # крок вгору
key_down = 'q'     #крок вниз


key_turn_left = 'n'     # поворот камери праворуч (а світу - ліворуч)
key_turn_right = 'm'    # поворот камери ліворуч (а світу – праворуч)

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1,0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        
        self.cameraBind()
        self.setEvents()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUntie(self):
        pos = self.hero.getPos()
        base.mouseInteFaceMode.setPose(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUntie()
        else:
            self.cameraBind()

    def turnLeft(self):
        self.hero.setH( (self.hero.getH() + 5) % 360)
        
    def turnRight(self):
        self.hero.setH( (self.hero.getH() - 5) % 360)

    def check_direction(self, angle):
        '''
        кут 0 (від 0 до 20)      ->        Y - 1
           кут 45 (від 25 до 65)    -> X + 1, Y - 1
           кут 90 (від 70 до 110)   -> X + 1
           від 115 до 155            -> X + 1, Y + 1
           від 160 до 200            ->        Y + 1
           від 205 до 245            -> X - 1, Y + 1
           від 250 до 290            -> X - 1
           від 290 до 335            -> X - 1, Y - 1
           від 340                   ->        Y - 1  '''
        
        if angle >= 0 and angle <= 20:
            return (0, -1)
        if angle <= 65:
            return (1, -1)
        if angle <= 110:
            return(1, 0)
        if angle <= 155:
            return (1, 1)
        if angle <= 200:
            return (0, 1)
        if angle <= 245:
            return (-1, 1)
        if angle <= 290:
            return (-1, 0)
        if angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)
    
    def look_at(self, angle):
        x_from = round( self.hero.getX() )
        y_from = round( self.hero.getY() )
        z_from = round( self.hero.getZ() )

        dx, dy = self.check_direction(angle)

        x_to = x_from + dx
        y_to = y_from + dy
        z_to = z_from 

        return x_to, y_to, z_to
    
    def turn_hero(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def moveTo(self,angle):
        if self.mode: 
            self.turn_hero(angle)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.moveTo(angle)

    def backward(self):
        angle = (self.hero.getH() + 180) % 360
        self.moveTo(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.moveTo(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.moveTo(angle)

    def setEvents(self):
        base.accept(key_turn_left, self.turnLeft)
        base.accept(key_turn_left, self.turnLeft)

        base.accept(key_turn_right, self.turnRight)
        base.accept(key_turn_right + '-repeat', self.turnRight)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)

        base.accept(key_back, self.backward)
        base.accept(key_back + '-repeat', self.backward)

        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)