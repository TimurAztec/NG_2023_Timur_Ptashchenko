def is_int_convertable(val: str):
    try: 
        int(val)
    except ValueError:
        return False
    else:
        return True
    
    if __name__ == "__main__":
        