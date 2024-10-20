def moveTower(height,start,aux,end):
    if height>=1:
        moveTower(height-1,start,end,aux)
        print("moving disk",height,start,"to",end)
        moveTower(height-1,aux,start,end)
moveTower(3,"A","B","C")
