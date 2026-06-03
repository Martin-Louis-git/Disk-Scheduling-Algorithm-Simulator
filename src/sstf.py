class Sstf:
    def __init__(
        self, initial_position, initial_direction, disk_size, request_queue, logger
    ):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue
        self.logger = logger

    def run(self):
        self.logger.info("Running SSTF algorithm...")

        current = self.initial_position
        queue = self.request_queue.copy()
        output_array = [0] * len(queue)
        total = 0
        order = 0

        while queue:
            i = 0
            closest = queue[0]
            while i < len(queue):
                if abs(current - queue[i]) < abs(current - closest):
                    closest = queue[i]
                i += 1

            seek = abs(current - closest)
            total += seek
            current = closest
            output_array[order] = closest
            order += 1
            queue.remove(closest)

        self.logger.info(f"SSTF - Service order: {output_array}")
        self.logger.info(f"SSTF - Total seek distance: {total}")

        return output_array, total
