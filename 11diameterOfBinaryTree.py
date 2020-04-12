class MinStack:
    index = -1
    min = float("inf")
    minIndex = 0
    stack = []

    def push(self, x: int) -> None:
        self.index+=1;
        self.stack.insert(self.index,x)
        if(x<self.min):
            self.minIndex=self.index
            self.min=x

    def finMin(self):
        if self.index==0:
            self.minIndex = 0
            self.min = self.stack[0]
            return
        for i in range(self.index+1):
            if self.stack[i]<self.min:
                self.minIndex = i
                self.min = self.stack[i]

    def pop(self) -> None:
        if(self.index<0):
            return

        if(self.index==self.minIndex):
            self.index -= 1;
            self.min = float("inf")
            self.finMin()
        else:
            self.index-=1;

    def top(self) -> int:
        if (self.index < 0):
            return

        return self.stack[self.index]

    def getMin(self) -> int:
        return self.stack[self.minIndex]
