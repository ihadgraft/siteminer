import os


class Miner(object):
    def __init__(self, detectors=None):
        if detectors is None:
            detectors = list()
        self.detectors = detectors

    def mine(self, base_path):
        ret = []
        for root, dirs, files in os.walk(base_path):
            for d in self.detectors:
                result = d.matches(base_path, root, dirs, files)
                if result:
                    ret.append(result)
        return ret


