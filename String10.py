def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    answer=(x+y)*2
    ans='"('+str(x)+'+'+str(y)+')*2='+str(answer)+'"'
    return ans
print(main(4,6))    
