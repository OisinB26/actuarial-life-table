class LifeTable:
        
    def __init__(self, qx):
        """
        qx = list of annual mortality rates
        Example: [0.01, 0.012, 0.013]
        """
        self.qx = qx

        # px is the probability of surviving each year
        self.px = [1 - q for q in qx]
            
