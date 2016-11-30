for i in range(2,2016):
 p=True
 for x in range(2,i):
  p=p and i%x
 if p and str(i)==str(i)[::-1]:print i
