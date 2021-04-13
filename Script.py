from docplex.mp.model import Model

my_model = Model(name='Car_Production')

CarA = my_model.integer_var(name='CarA')
CarB = my_model.integer_var(name='CarB')


# constraint #1: CarA production is greater than 100
my_model.add_constraint(CarA >= 10)

# constraint #2: CarB production is greater than 100
my_model.add_constraint(CarB >= 10)

# constraint #3: Assembly Line has a Maximum Capacity Limitaion
ct_assembly = my_model.add_constraint( 0.5 * CarA + 0.25 * CarB <= 20)

# constraint #4: Painting and Finishing Line has a Maximum Capacity Limitation.
ct_painting = my_model.add_constraint( 0.5 * CarA + 0.1 * CarB <= 10)


my_model.maximize(12000 * CarA + 15000 * CarB)

solution = my_model.solve()
print(solution)
my_model.print_solution()