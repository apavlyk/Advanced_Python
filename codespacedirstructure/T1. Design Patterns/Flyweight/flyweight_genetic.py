"""
Flyweight Design Pattern
   Desc: Sharing the shareable data between the common classes and thus  reducing the memory usage
   Code: Believing that every person in a family will have same genetic
         structure, we will create a code to learn about
         genetics of each family. If a same member of a family is given, no new
         object is created. (You can also create new
         objects unlike here but keep a reference of the heavy weighted one in
         the new |||r object).
"""


class ComplexGenetics:
    """Returns a huge genetic pattern"""

    def __init__(self):
        pass

    def genes(self, gene_code):
        self.gene = gene_code
        return "ComplexPatter[{}]TooHugeinSize".format(gene_code)


class Families:
    """To learn about Family Genetic Pattern."""
    family = dict()

    def __new__(cls, name, family_id):
        """I have to capture the details before the class is created, __init__
        is pseudo constructor. Data ex. (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG')) """
        return cls.family.get(family_id, super().__new__(cls))
        try:
            id = cls.family[family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.family[family_id] = id
        return id

    def __init__(self, *args, **kwargs):
        self.chromosome_count = 46

    def set_genetic_info(self, genetic_info):
        cg = ComplexGenetics()
        self.genetic_info = cg.genes(genetic_info)

    def get_genetic_info(self):
        return (self.genetic_info)


def test():
    data = (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG'))
    family_objects = []
    for d in data:
        obj = Families(d[0], d[1])
        obj.set_genetic_info(d[2])
        family_objects.append(obj)

    for f in family_objects:
        print("id = {}".format(id(f)))
        print(f.get_genetic_info())
    print("similar id's says that they are same objects ")


if __name__ == '__main__':
    test()
