import sys
for p in sys.path:
    print(p)
sys.path.append('../')
from src.controller.controller import Controller


if __name__ == "__main__":
    controller = Controller()
