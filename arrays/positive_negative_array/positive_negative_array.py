def segregateElements(self, arr):
        pos=[]
        neg=[]
        for i in arr:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        arr[:]=pos+neg
