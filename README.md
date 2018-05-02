This is a simple script to crawl a directory, looking for identifiable sites.

Currently supports:

- Wordpress
- Drupal 7
- Drupal 8

# Run all known detectors on a path


```sh
python run.py TARGET_PATH
```

# Integrating into another script or app

```python
from miner import Miner
import detection

miner = Miner([
  detection.WordpressDetector(),
  detection.Drupal7Detector(),
  detection.Drupal8Detector(),
])
```
