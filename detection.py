import os
import re


class IDetector(object):

    def matches(self, base_path, root, dirs, files):
        raise NotImplementedError


class WordpressDetector(IDetector):

    def matches(self, base_path, root, dirs, files):
        if 'index.php' in files:
            with open(os.path.join(root, 'index.php')) as stream:
                data = stream.read()
            if re.search('require.*?wp-blog-header\.php', data):
                return {'root': root, 'platform': 'wordpress', 'version': self._get_version(root)}

    def _get_version(self, docroot):
        with open(os.path.join(docroot, 'wp-includes', 'version.php')) as stream:
            data = stream.read()
        m = re.search(r'\$wp_version.*?(?P<version>\d+\.\d+(\.\d+)?)', data)
        if m:
            return m.group('version')


class Drupal7Detector(IDetector):

    def matches(self, base_path, root, dirs, files):
        if 'index.php' in files:
            with open(os.path.join(root, 'index.php')) as stream:
                data = stream.read()
            if re.search('define.*?DRUPAL_ROOT', data):
                return {'root': root, 'platform': 'drupal', 'version': self._get_version(root)}

    def _get_version(self, docroot):
        with open(os.path.join(docroot, 'includes', 'bootstrap.inc')) as stream:
            data = stream.read()
        m = re.search('define.*?VERSION.*?(?P<version>\d+\.\d+)', data)
        if m:
            return m.group('version')


class Drupal8Detector(IDetector):

    def matches(self, base_path, root, dirs, files):
        if 'index.php' in files and 'drush/drush/tests' not in root:
            with open(os.path.join(root, 'index.php')) as stream:
                data = stream.read()
            if '$request = Request::createFromGlobals()' in data and '$response->send()' in data:
                return {'root': root, 'platform': 'drupal', 'version': self._get_version(root)}

    def _get_version(self, docroot):
        docroot_split = os.path.split(docroot)
        while len(docroot_split) > 0:
            search_path = os.path.join(os.path.join(*docroot_split), 'core', 'lib', 'Drupal.php')
            if os.path.exists(search_path):
                with open(search_path) as stream:
                    data = stream.read()
                m = re.search(r'const.*VERSION.*?(?P<version>\d+\.\d+\.\d+)', data)
                if m:
                    return m.group('version')
            docroot_split = docroot_split[:-1]





