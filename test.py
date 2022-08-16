"""---------------------------------------------------------
    name: test.py
    editor: shenchunqian
    created: 2022-08-16
---------------------------------------------------------"""

from tinylog import tinylog as log

class Tiny():
    def __init__(self, name: str, number: int, keys: list):
        self.name = name
        self.number = number
        self.keys = keys

if __name__ == '__main__':

    t = Tiny("tiny", 100, [1, 2, 3, 4, 5, 6])
    log.info("Tiny __dict__: {}", t.__dict__)

    log.debug("Say: {}, {}", "Hello", "Py!")
    log.warn("Say: {}, {}", "Hello", "Py!")
    log.info("Say: {}, {}", "Hello", "Py!")
    log.error("Say: {}, {}", "Hello", "Py!")
    log.fatal("Say: {}, {}", "Hello", "Py!")
