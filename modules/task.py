class Task:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "I'm a Task Class"
    
    def jsonify(self):
        raise NotImplementedError("TODO")
    
    def dejsonify(self):
        raise NotImplementedError("TODO")