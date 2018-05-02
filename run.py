from __future__ import print_function
import detection
from miner import Miner
import argparse
import sys
import os


class Main(object):

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("base_path")
        args = parser.parse_args()

        if os.path.isdir(args.base_path):
            self._run(os.path.realpath(args.base_path))
        else:
            print('Value \'%s\' is not an existing directory' % args.base_path, file=sys.stderr)
            exit(1)

    def _run(self, base_path):
        m = Miner([
            detection.WordpressDetector(),
            detection.Drupal7Detector(),
            detection.Drupal8Detector(),
        ])
        for result in m.mine(base_path):
            print(result)


if __name__ == '__main__':
    Main().run()
