from vector import Vector3D

def main():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)

    print(v1 + v2)
    print(v1 * v2)
    print(len(v1))
    print(v1 == v2)

if __name__ == "__main__":
    main()