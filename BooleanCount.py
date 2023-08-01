def count_boolean(b1, b2, b3):
        if( b1==True,b2==True, b3==True):
            return True
        elif( b1==True,b2==True, b3==False):
            return True
        elif( b1==True,b2==False, b3==True):
            return True
        elif( b1==False,b2==True, b3==True):
            return True
        else:
            return False
            
        '''if( b1==True,b2==False, b3==False):
            return False
        if( b1==False,b2==True, b3==False):      
            return False
        if( b1==False,b2==False, b3==True):
            return False
        if( b1==False,b2==False, b3==False):
            return False
            '''

print (count_boolean(False,False,True))
