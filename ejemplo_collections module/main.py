from namedtuple import ejemplo_namedtuple
from deque import ejemplo_deque
from counter import ejemplo_counter
from defaultdict import ejemplo_defaultdict
from chainmap import ejemplo_chainmap
from userdict import ejemplo_userdict
from userlist import ejemplo_userlist
from userstring import ejemplo_userstring

def main():
    print("=== namedtuple ===")
    ejemplo_namedtuple()

    print("\n=== deque ===")
    ejemplo_deque()

    print("\n=== Counter ===")
    ejemplo_counter()

    print("\n=== defaultdict ===")
    ejemplo_defaultdict()

    print("\n=== ChainMap ===")
    ejemplo_chainmap()

    print("\n=== UserDict ===")
    ejemplo_userdict()

    print("\n=== UserList ===")
    ejemplo_userlist()

    print("\n=== UserString ===")
    ejemplo_userstring()


if __name__ == "__main__":
    main()
