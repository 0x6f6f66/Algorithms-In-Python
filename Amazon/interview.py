class Package:
    def __init__(self, name: str, dependencies: list):
        self.name = name
        self.depedendencies = dependencies

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Installer:
    def install(self, package: Package):
        pass


if __name__ == '__main__':
    """
    A: B, C
    B: D
    C: E    
    
    A: B C D
    B: C D
    
    A: B
    B: A
    
    """

    D = Package('D', [])
    E = Package('E', [])
    B = Package('B', [D])
    C = Package('C', [E])
    A = Package('A', [B, C])

    print(A.depedendencies)
    print(B.depedendencies)

    installer = Installer()
    installer.install(A)