"""
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
  list1=[]
  for i in l:
    if type(i) != str:
        list1.append(i)
  
  return list1
