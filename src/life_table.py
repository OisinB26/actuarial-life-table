class LifeTable:
        
    def __init__(self, qx):
        """
        qx = list of annual mortality rates
        Example: [0.01, 0.012, 0.013]
        """
        self.qx = qx
