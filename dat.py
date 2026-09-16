class dailydatahelper:

    def __init__(self):
        self.data = [10, 20, 30]

    def show_data(self):
        print(self.data)

    def search_data(self):
        for i, x in enumerate(self.data):
            print(i, x)

    def __del__(self):
        print("Object ended")


helper = dailydatahelper()

helper.show_data()
helper.search_data()