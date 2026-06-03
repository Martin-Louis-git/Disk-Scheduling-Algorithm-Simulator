class Lstf:
    def __init__(
        self,
        initial_position,
        initial_direction,
        disk_size,
        request_queue,
        logger=None,
    ):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue
        self.logger = logger

    def run(self):
        self.logger.info("Running LSTF algorithm...")

        current = self.initial_position
        queue = self.request_queue.copy()
        output_array = []
        total = 0

        while queue:
            i = 0
            farthest = queue[0]
            while i < len(queue):
                if abs(current - queue[i]) > abs(current - farthest):
                    farthest = queue[i]
                i += 1

            seek = abs(current - farthest)
            total += seek
            current = farthest
            output_array.append(farthest)
            queue.remove(farthest)

        self.logger.info(f"LSTF - Service order: {output_array}")
        self.logger.info(f"LSTF - Total seek distance: {total}")

        return output_array, total
