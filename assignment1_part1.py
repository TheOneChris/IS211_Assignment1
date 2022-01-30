def listDivide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    """
    Passing Two Args numbers which is a list of numbers provided, and divide which is a set integer (2) 
    """
    divisiblecount = 0
    for num in numbers:
        if num % divide == 0:
            divisiblecount += 1
    return divisiblecount


class ListDivideException(Exception):
    """Exception Class used to throw an Excpetion if above function doesn't work"""
    pass


def testListDivide():
    
    """
    Test listDivide
    """
    numlist1 = listDivide([1,2,3,4,5])
    numlist2 = listDivide([2,4,6,8,10])
    numlist3 = listDivide([30, 54, 63,98, 100], divide=10)
    numlist4 = listDivide([])
    numlist5 = listDivide([1,2,3,4,5], 1)
    
    if numlist1 != 2:
        raise ListDivideException("numlist1 error")
    if numlist2 != 5:
        raise ListDivideException("numlist2 error")
    if numlist3 != 2:
        raise ListDivideException("numlist3 error")
    if numlist4 != 0:
        raise ListDivideException("numlist4 error")
    if numlist5 != 5:
        raise ListDivideException("numlist5 error")
    
    
    """TEST command is calling the testListDivide via testListDivide()"""