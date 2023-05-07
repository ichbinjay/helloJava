"""
    array valuation example walkthrough 
    for the first problem, we are given 
    [1, 1, 1, 1, 1]
    and 
    [1, 0, 1]

    If we evaluate the converted form of these, the first is 11 and the second is 5 
    This gives a form of 16 in base of -2 
    in base of -2, 16 is -2^4 
    Remembering that we start at power 0, this as an array is then 
    [1, 0, 0, 0, 0]

    Where we can notice that even powers of -2 will be the same as the regular powers of positive 2 
    This should come as no surprise if you have studied 2's complement which the problem is based on
    Learn more here : https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html 

"""

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # converts from negative binary form array to a valuation
        def convert_from_negative_form(array_to_convert) : 
            place_value = 1
            return_valuation = 0
            array_to_convert.reverse()
            for bit in array_to_convert : 
                return_valuation +=  bit * place_value 
                place_value *= -2
            return return_valuation

        # get array valuations 
        array_1_valuation = convert_from_negative_form(arr1)
        array_2_valuation = convert_from_negative_form(arr2)
        # sum them 
        sum_of_arrays = array_1_valuation + array_2_valuation
        
        # converts from value to convert to array form in 2s complement form 
        def convert_to_negative_form(value_to_convert) : 
            # base case 
            if value_to_convert == 0 : 
                return [0]
            # set up for return 
            negative_form_array = collections.deque()
            # build negative_form_array while not 0 
            while value_to_convert != 0 : 
                # update value to convert 
                value_to_convert, remainder = divmod(value_to_convert, -2)
                # remainder is either -1 or 0 
                # if it is 0 we're good, 
                # but if not we need to account for overflow 
                if remainder < 0 : 
                    # shift value to convert forward on remainder -1 
                    value_to_convert += 1 
                    # cannot place -1 in binary array, but can place 1
                    remainder = 1
                # append remainder as this is the 2s complement left over 
                negative_form_array.appendleft(remainder)
            # return when done 
            return negative_form_array 

        # get valuation 
        negative_array = convert_to_negative_form(sum_of_arrays)
        # return negative array 
        return negative_array 