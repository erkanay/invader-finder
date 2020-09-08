import re
from collections import OrderedDict


class InvaderTracker(object):
    def __init__(self, radar, invader):
        self._invaders = []
        self.radar = radar.split()
        self.invader = invader.split()

    @property
    def invader_length(self):
        return len(self.invader)

    @property
    def invaders(self):
        return self._invaders

    @staticmethod
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    @property
    def invader_locations(self):
        """Returns found locations of invaders
        [(row, start_index, end_index),]

        eg. [[(1, 10, 21),
              (2, 10, 21),
               ...),]]
        """
        locations = []
        for data in self.chunks(self.invaders, self.invader_length):
            locations.append([(i.get('row'), i.get('start_index'), i.get('end_index')) for i in data])
        return locations

    def search_invaders(self):
        """Search an invader in radar pattern
        if first pattern of invader found then track down of same indexes for next rows

        """
        for i, invader_row in enumerate(self.invader):
            for j, radar_row in enumerate(self.radar):
                # found head of invader
                for matched in re.finditer(invader_row, radar_row):
                    start_index = matched.start()
                    end_index = matched.end()

                    if self.invader[0] == invader_row:
                        next_radar_row = j + 1
                        next_invader_row = i + 1
                        self._invaders.append(
                            OrderedDict(row=next_radar_row, start_index=start_index,
                                        end_index=end_index, pattern=invader_row)
                        )
                        # checked if next rows of same indexes matched with invader
                        for next_radar in self.radar[next_radar_row:]:
                            matched_row = next_radar[start_index:end_index]
                            if self.invader_length == next_invader_row:
                                break
                            if next_invader_row < self.invader_length and matched_row == self.invader[next_invader_row]:
                                next_radar_row += 1
                                next_invader_row += 1
                                self._invaders.append(OrderedDict(row=next_radar_row, start_index=start_index,
                                                                  end_index=end_index, pattern=matched_row))
                            else:
                                if not self.invader_length == len(self._invaders):
                                    self._invaders.pop()
                                break
