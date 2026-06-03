class Teleport:
    def __init__(
        self, initial_position, initial_direction, disk_size, request_queue, logger=None
    ):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue
        self.logger = logger

    def run(self):
        total_steps = len(self.request_queue)
        order_of_service = self.request_queue.copy()

        return order_of_service, total_steps
