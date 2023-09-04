# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .dhcp_static_map import *
from .dns_host_override import *
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumiverse_opnsense.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumiverse_opnsense.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "opnsense",
  "mod": "index/dhcp_static_map",
  "fqn": "pulumiverse_opnsense",
  "classes": {
   "opnsense:index/dhcp_static_map:dhcp_static_map": "Dhcp_static_map"
  }
 },
 {
  "pkg": "opnsense",
  "mod": "index/dns_host_override",
  "fqn": "pulumiverse_opnsense",
  "classes": {
   "opnsense:index/dns_host_override:dns_host_override": "Dns_host_override"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "opnsense",
  "token": "pulumi:providers:opnsense",
  "fqn": "pulumiverse_opnsense",
  "class": "Provider"
 }
]
"""
)