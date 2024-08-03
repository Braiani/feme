class Export:
    def __init__(self):
        print('Export.__init__')

    @staticmethod
    def export():
        print('Export.export')

    def __del__(self):
        print('Export.__del__')