def keymax(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     print k[v.index(max(v))], max(v)
keymax(d)
