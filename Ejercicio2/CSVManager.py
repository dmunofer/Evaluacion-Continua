# CSV Manager
class CSVManager:
    @staticmethod
    def save_to_csv(pizza: Pizza):
        with open('pizzas.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            details = [(category, choice) for category, choice in pizza.details.items()]
            csv_writer.writerows(details)

    @staticmethod
    def read_from_csv():
        pizzas = []
        with open('pizzas.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                pizza = Pizza()
                for i in range(0, len(row), 2):
                    pizza.add_detail(row[i], row[i + 1])
                pizzas.append(pizza)
        return pizzas