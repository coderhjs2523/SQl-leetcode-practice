class Solution(object):

    def myAtoi(self, s):

        n = len(s)

        i=0

        # skip leading zeroes

        while i<n and s[i]==' ':

            i+=1

        # check sign

        sign = 1

        if i<n and s[i]=='-':

            sign = -1

            i+=1

        elif i<n and s[i]=='+':

            i+=1

        # build number

        num =0

        while i<n and s[i].isdigit():

            d = int(s[i])

            num =num*10+d

            i+=1

        num*=sign

        # bring in range

        intMin = -2**31

        intMax = 2**31 - 1

        if num< intMin:

            return intMin

        if num>intMax:

            return intMax

        return num




