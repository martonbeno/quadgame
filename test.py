from Board import *


#----------------test case 1-----------------------
b = Board()
assert not b.is_over(), "testcase1"
#--------------------------------------------------


#----------------test case 2-----------------------
b = Board()
b.add_piece(0,0,(0,0,0,0))
b.add_piece(0,1,(0,0,0,1))
b.add_piece(0,2,(0,0,1,1))
b.add_piece(0,3,(0,1,1,1))
assert b.is_over(), "testcase2"
#--------------------------------------------------


#----------------test case 3-----------------------
b = Board()
b.add_piece(0,0,(0,0,0,0))
b.add_piece(0,1,(0,0,0,1))
b.add_piece(0,2,(0,0,1,1))
b.add_piece(0,3,(1,1,1,1))
assert not b.is_over(), "testcase3"
#--------------------------------------------------


#----------------test case 4-----------------------
b = Board()
b.add_piece(0,0,(0,0,0,0))
b.add_piece(1,1,(0,0,0,1))
b.add_piece(2,2,(0,0,1,1))
b.add_piece(3,3,(0,1,1,1))
assert b.is_over(), "testcase4"
#--------------------------------------------------

#----------------test case 5-----------------------
b = Board()
b.add_piece(3,0,(0,0,0,0))
b.add_piece(2,1,(0,0,0,1))
b.add_piece(1,2,(0,0,1,1))
b.add_piece(0,3,(0,1,1,1))
assert b.is_over(), "testcase5"
#--------------------------------------------------

#----------------test case 6-----------------------
b = Board()
b.add_piece(0,0,(0,0,0,0))
b.add_piece(0,1,(0,0,0,1))
b.add_piece(0,2,(0,0,1,1))
b.add_piece(0,3,(1,1,1,1))
assert not b.is_over(), "testcase6"
#--------------------------------------------------

#----------------test case 7-----------------------
b = Board()
# nagy, lyukas, szögletes, sötét
b.add_piece(0,0,(0,1,0,1))
b.add_piece(0,1,(0,1,1,0))
b.add_piece(0,2,(1,0,1,0))
b.add_piece(0,3,(0,1,0,0))

b.add_piece(1,0,(1,1,1,0))
b.add_piece(1,1,(0,0,0,0))
b.add_piece(1,2,(0,0,1,1))
b.add_piece(1,3,(0,0,0,1))

b.add_piece(2,0,(1,0,0,0))
b.add_piece(2,1,(1,1,0,0))
b.add_piece(2,2,(1,1,1,1))
b.add_piece(2,3,(0,1,1,1))

b.add_piece(3,0,(0,0,1,0))
b.add_piece(3,1,(1,0,1,1))
b.add_piece(3,2,(1,1,0,1))
b.add_piece(3,3,(1,0,0,1))
assert b.is_over(), "testcase7"
#--------------------------------------------------


print("all tests passed")