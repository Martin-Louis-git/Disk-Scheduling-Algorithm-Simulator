class Scan:
    def __init__(self, initial_position, initial_direction, disk_size, request_queue):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue

    def run(self, look: bool):
        # Implement the SCAN disk scheduling algorithm here.
        # The 'look' parameter indicates whether to use the look variant of SCAN.
        pass
