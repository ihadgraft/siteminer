This is a simple script to crawl a directory, looking for identifiable sites.

Currently supports:

- Wordpress
- Drupal 7
- Drupal 8

# Run all known detectors on a path

The following outputs a JSON representation of everything found by the miner.

```sh
python run.py TARGET_PATH
```

# Integrating into another script or app

This demonstrates how to set up and run the miner. The return value is an array of data about each site, including:

- root: The root path of the site
- platform: The name of the platform, e.g. 'wordpress', 'drupal'
- version: The detected version of the platform instance

```python
from miner import Miner
import detection

miner = Miner([
  detection.WordpressDetector(),
  detection.Drupal7Detector(),
  detection.Drupal8Detector(),
])
```
