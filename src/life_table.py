class LifeTable:

    def __init__(self, qx, radix=100000):
        """
        qx = list of annual mortality rates
        radix = number of lives at start (default 100000)
        """
        self.qx = qx
        self.radix = radix

        # px is the probability of surviving each year
        self.px = [1 - q for q in qx]

        # lx = number of people alive at start of each year
        self.lx = [radix]
        for p in self.px:
            next_l = self.lx[-1] * p
            self.lx.append(next_l)
            
        # dx = number of deaths during each year
        self.dx = []
        for i in range(len(self.qx)):
            deaths = self.lx[i] * self.qx[i]
            self.dx.append(deaths)
