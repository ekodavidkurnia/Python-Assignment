
def even_num(a,b):
    """
    this function will return even number between 
    first input to second input, and expected 
    numerical value
    """
    import logging as lg
    lg.basicConfig(filename='even.log', level = lg.INFO, format = "%(asctime)s %(message)s")
    try :
        return [x for x in range(a,b+1) if x%2 == 0]
    except Exception as e:
        lg.error(e)
        return e