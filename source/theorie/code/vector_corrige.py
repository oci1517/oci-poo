class Vector(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __mul__(self, other):
        return sum([
            self.x * other.x,
            self.y * other.y,
            self.z * other.z,
        ])

    def __eq__(self, other):
        # la fonction intégrée all() retourne True si tous les éléments de la
        # liste sont True
        return all([
            self.x == other.x,
            self.y == other.y,
            self.z == other.z,
        ])

    
def test_Vector():
    v1 = Vector(1,1,1)
    v2 = Vector(2,2,2)
    assert (Vector(3,3,3) == Vector(3,4,3)) == False
    assert (v1 + v2) == Vector(3,3,3)
    assert (v1 * v2) == 6


# uniquement exécuter la fonction de test si on exécute directement ce fichier
if __name__ == '__main__':
    test_Vector()
