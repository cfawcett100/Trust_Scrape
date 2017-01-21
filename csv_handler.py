import csv
import datetime

class csv_handler(object):
    def __init__(self, file_name):
        print(datetime.datetime.now())
        self._csv_file = file_name

        print("LOADING FILE...")
        csv_reader = self.open_csv()
        self._trust_list = self.create_list(csv_reader)
        self.to_upper()
        print("FILE LOADED!")

        print(datetime.datetime.now())

    def run_tests(self):
        self.trustee_search()
        location = int(input("Enter location: "))
        self.get_first_cons(location)

    def open_csv(self):
        """Opens the csv file and returns the csv reader"""
        input_file = open(self._csv_file, "r")
        reader = csv.reader(input_file)
        return reader

    def create_list(self, csv_reader):
        """Takes the items in the file and puts them into a list"""
        new_list = []
        count = 1
        first = True

        for row in csv_reader:
            # A horrible piece of code to break if the first row is an int
            # Continues if it's the first line
            if first == True:
                if not isinstance(row[0], str):
                    return []
                first = False
                continue

            new_list.append(row)

        return new_list

    def to_upper(self):
        """Turns all names into upper case"""
        for i in self._trust_list:
            i[1] = i[1].upper() # Changes name to all upper case

    def trustee_search(self):
        """Searches for all appearances of a string"""
        name = input("Enter trustee name: ")
        name = name.upper()
        trustee_list = []

        for i in range(0, len(self._trust_list)):
            try:
                if name in self._trust_list[i][1]:
                    trustee_list.append([i, self._trust_list[i][0], self._trust_list[i][1]])
            except:
                print(self._trust_list[i])

        self.print_search(trustee_list)

    def print_search(self, trustee_list):
        """Prints the search results from trustee_search"""
        if len(trustee_list) > 20:
            choice = input("More than 20 matches found. Do you wish to print?(y/n) ")
            if choice == "y":
                self.printf(trustee_list)
        else:
            self.printf(trustee_list)

    def printf(self, trustee_list):
        """Formatted print function for the trustee list"""
        print("Location, Trust, Trustee")
        for i in trustee_list:
            print(i[0], i[1], i[2])

    def get_trustee(self, location):
        """Given a position in the _trust_list, returns the trustee name"""
        return self._trust_list[location][1]

    def get_trust(self, location):
        """Given a position in the _trust_list, returns the trust number"""
        return self._trust_list[location][0]

    def get_trustees_trusts(self, name):
        """Takes a trustee name and returns a list of associated trusts"""
        trust_list = []
        for i in self._trust_list:
            if name == i[1] and i[0] not in trust_list:
                trust_list.append(i[0])

        return trust_list

    def get_trust_trustees(self, trust):
        """Takes a trust number and returns a list of associated trustees"""
        name_list = []
        for i in self._trust_list:
            if trust == i[0] and i[1] not in name_list:
                name_list.append(i[1])

        return name_list

    def get_first_cons(self, location):
        """Given a location in the list of trustees, it will find that trustees first hand connections"""
        trustee = self.get_trustee(location)
        trustees_trusts = self.get_trustees_trusts(trustee)
        cons = []

        print("Trustee name: ", trustee)
        print("Trustee's trusts: ")
        self.print_list(trustees_trusts)

        for i in trustees_trusts:
            cons = cons + self.get_trust_trustees(i)
            print("\n", i)
            self.print_list(self.get_trust_trustees(i))

        #cons = list(set(cons))       In case of duplicates

    def print_list(self, input_list):
        """Formatted printing for outputting connections"""
        for i in input_list:
            print(i)

    def connections(self, degree, location):
        """Takes a number and a location and finds all connections at the degree entered"""

    def fail(self, n):
        print("TEST ", n, " FAILED!!!")
        exit()

    def eq(self, n, a, b):
        """General function to see if two things are equal"""
        n += 1
        if a == b:
            return n
        else:
            self.fail(n)
            return n

    def list_sub(self, a, b):
        if len(a) < len(b):
            return []
        return [x for x in a if x not in b]

    def list_comp(self, a, b):
        for i in a:
            if i not in b:
                return False

        return True

    def eq1(self, n, inp, exp):
        count = 1
        while count <= len(exp) - 1:
            inpComp = self.list_sub(inp[-count], inp[-count - 1])
            expComp = self.list_sub(exp[-count], exp[-count - 1])
            inpComp = sorted(inpComp)
            expComp = sorted(expComp)
            if inpComp != expComp:
                self.fail(n)
            count += 1

        return n

    def tests(self):
        """Tests some other functions in the class"""
        n = 0
        n = self.eq(n, self.connections(0,0), [["A"]])
        n = self.eq1(n, self.connections(1,0), [["A"], ["A", "B", "C", "D", "E", "F", "G"]])
        n = self.eq1(n, self.connections(2,0), [["A"], ["A", "B", "C", "D", "E", "F", "G"], ["A", "B", "C", "D", "E", "F", "G", "H", "I"]])


# Used for testing
def main():
    file_name = "test_data.csv"
    new_handler = csv_handler(file_name)
    new_handler.eq1(1, [["A"], ["D", "A", "F", "I"]], [["A"], ["I", "F", "D", "A"]])
    # new_handler.tests()

main()
