import importlib.metadata

from fmd.client import FmdApi

package_name = 'fmd'
__version__ = importlib.metadata.version(package_name)
__all__ = [FmdApi]
