class MapManager(): #клас для керування картою
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))

        self.color = (0.2, 0.2, 0.35, 1)

        def startNew(self):
            self.land = render.attachNewNode('Land')

        def addBlock(self, position)
            pass