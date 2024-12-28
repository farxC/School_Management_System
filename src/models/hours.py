class Hours:
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self.value = value
        
    def __repr__(self):
        return f"{self.value}/hrs"
    
    def __int__(self):
        return self.value