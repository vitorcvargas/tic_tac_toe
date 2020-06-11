class GameTable:
    
    blocks = {
        '7': "", '8': "", '9': "",
        '4': "", '5': "", '6': "",
        '1': "", '2': "", '3': ""
    }

    def __init__(self):
        pass
        
    def add(self, block, mark):
        if self.blocks[block] == "": 
            self.blocks[block] = mark
        else:
            return False

    def __str__(self):
        return ' {} | {} | {} \n---------\n {} | {} | {} \n---------\n {} | {} | {} '.format(
        self.blocks['7'], self.blocks['9'], 
        self.blocks['8'], self.blocks['4'],
        self.blocks['5'], self.blocks['6'], 
        self.blocks['1'],self.blocks['2'], 
        self.blocks['3']
        )

    def result(self, count):
    
        if count >= 5:
            if self.blocks['7'] == self.blocks['8'] == self.blocks['9']:
                return True
            elif self.blocks['4'] == self.blocks['5'] == self.blocks['6']:
                return True
            elif self.blocks['1'] == self.blocks['2'] == self.blocks['3']:
                return True
            elif self.blocks['1'] == self.blocks['4'] == self.blocks['7']:
                return True
            elif self.blocks['2'] == self.blocks['5'] == self.blocks['8']:
                return True
            elif self.blocks['3'] == self.blocks['6'] == self.blocks['9']:
                return True
            elif self.blocks['3'] == self.blocks['5'] == self.blocks['7']:
                return True
            elif self.blocks['1'] == self.blocks['5'] == self.blocks['9']:
                return True
            elif count == 10:
                return False

