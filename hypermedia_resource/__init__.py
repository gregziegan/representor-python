__title__ = 'hypermedia_resource'
__version__ = '0.1.0-beta1'
__author__ = 'Stephen Mizell'
__license__ = 'MIT'

from base import HypermediaResource
import adapters

HypermediaResource.adapters.add(adapters.HalJSONAdapter)
HypermediaResource.adapters.add(adapters.MazeXMLAdapter)
