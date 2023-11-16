# Director
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self, dough, sauce, toppings, technique, presentation, pairing, extras):
        self.builder.build_dough(dough)
        self.builder.build_sauce(sauce)
        self.builder.build_toppings(toppings)
        self.builder.build_cooking_technique(technique)
        self.builder.build_presentation(presentation)
        self.builder.build_pairing(pairing)
        self.builder.build_extras(extras)