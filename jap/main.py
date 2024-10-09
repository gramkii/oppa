from math import *
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence

from panda3d.core import Point3

class SuperGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)


        self.scene.setScale(0.25, 0.25, 0.25)
        
        self.kokojambo = Actor('models/panda-model',
                               {'walk': 'models/panda-walk4'})
        self.kokojambo.setScale(0.005, 0.005, 0.005)
        self.kokojambo.reparentTo(self.render)
        self.kokojambo.loop('walk')

        posInterval1 = self.kokojambo.posInterval(13, Point3(0, -10, 0), startPos = Point3(0,10,0))

        posInterval2 = self.kokojambo.posInterval(13, Point3(0, 10, 0), startPos = Point3(0,-10,0))

        oborot1 = self.kokojambo.hprInterval(4,Point3(180, 0, 0), startHpr = Point3(0,0,0))

        oborot2 = self.kokojambo.hprInterval(4,Point3(0, 0, 0), startHpr = Point3(180,0,0))
  
  

game = SuperGame()
game.run()