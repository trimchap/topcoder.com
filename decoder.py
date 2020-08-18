# You have a binary string such as: 011100011
# One way to encrypt it is to add to each digit the sum of it's adjacent
# digits. For example, the above string would become: 123210122
#
# If P is the original string and Q is the encrypted string then
# Q[i] = P [i-1] + P[i] + P[i+1]. Characters off the left and right
# edges of the string are treated as zeroes.
#
# Class:             BinaryCode
# Method:            decode
# Parameters:        string
# Returns:           tuple(string)
# Method signature:  def decode(self, message):

class BinaryCode:
    def __init__(self):
        return

    #loop through the encrypted list, build origional string
    def decode_the_middle(self,P,Q):
        P_str = ""
        for i in range(2,len(Q)):
            P.append( Q[i-1] - P[i-2] - P[i-1] )
            if P[i] > 1 or P[i] < 0 : # not valid, not binary
                return "NONE"
        for x in P:
            P_str += str(x)
        return P_str

    # decode with 2 assumptions about the first digit
    def decode(self, Q):
        P0 = []
        P1 = []
        P0_str = ""
        P1_str = ""
        if len(Q) < 2:
            return("NONE","NONE")
        Q = list(map(int,Q)) # convert the string element to ints

        #assume P[0] = 0
        P0.append(0)
        #decode P[1]
        if Q[0] == 1:
            P0.append(1)
        else:
            P0.append(0)
        # decode the middle
        P0_str = self.decode_the_middle(P0,Q)

        #assume P[0] = 1
        P1.append(1)
        #decode P[1]
        if Q[0] == 1:
            P1.append(0)
        else:
            P1.append(1)
        P1_str = self.decode_the_middle(P1,Q)

        return [P0_str,P1_str]
        
# Test Decoder
Q = "123210122"
print(" Q =",Q)
code = BinaryCode()
print(BinaryCode.decode(code,Q))
print("['011100011', 'NONE'] - expected")
print('-----------------------')
Q = "11"
print(" Q =",Q)
code = BinaryCode()
print(BinaryCode.decode(code,Q))
print("['01', '10']- expected")
print('-----------------------')
Q = "22111"
print(" Q =",Q)
code = BinaryCode()
print(BinaryCode.decode(code,Q))
print("['NONE', '11001'] - expected")
print('-----------------------')
Q = "123210120"
print(" Q =",Q)
code = BinaryCode()
print(BinaryCode.decode(code,Q))
print("['011100011', 'NONE'] - expected")
print('-----------------------')
Q = "3"
print(" Q =",Q)
code = BinaryCode()
print(BinaryCode.decode(code,Q))
print("['NONE', 'NONE'] - expected")
print('-----------------------')


