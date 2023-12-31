# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['Dhcp_static_mapArgs', 'Dhcp_static_map']

@pulumi.input_type
class Dhcp_static_mapArgs:
    def __init__(__self__, *,
                 interface: pulumi.Input[str],
                 ipaddr: pulumi.Input[str],
                 mac: pulumi.Input[str],
                 hostname: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Dhcp_static_map resource.
        """
        pulumi.set(__self__, "interface", interface)
        pulumi.set(__self__, "ipaddr", ipaddr)
        pulumi.set(__self__, "mac", mac)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)

    @property
    @pulumi.getter
    def interface(self) -> pulumi.Input[str]:
        return pulumi.get(self, "interface")

    @interface.setter
    def interface(self, value: pulumi.Input[str]):
        pulumi.set(self, "interface", value)

    @property
    @pulumi.getter
    def ipaddr(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ipaddr")

    @ipaddr.setter
    def ipaddr(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipaddr", value)

    @property
    @pulumi.getter
    def mac(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: pulumi.Input[str]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)


@pulumi.input_type
class _Dhcp_static_mapState:
    def __init__(__self__, *,
                 hostname: Optional[pulumi.Input[str]] = None,
                 interface: Optional[pulumi.Input[str]] = None,
                 ipaddr: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Dhcp_static_map resources.
        """
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if interface is not None:
            pulumi.set(__self__, "interface", interface)
        if ipaddr is not None:
            pulumi.set(__self__, "ipaddr", ipaddr)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def interface(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "interface")

    @interface.setter
    def interface(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface", value)

    @property
    @pulumi.getter
    def ipaddr(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ipaddr")

    @ipaddr.setter
    def ipaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipaddr", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)


class Dhcp_static_map(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 interface: Optional[pulumi.Input[str]] = None,
                 ipaddr: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Dhcp_static_map resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Dhcp_static_mapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Dhcp_static_map resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param Dhcp_static_mapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Dhcp_static_mapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 interface: Optional[pulumi.Input[str]] = None,
                 ipaddr: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = Dhcp_static_mapArgs.__new__(Dhcp_static_mapArgs)

            __props__.__dict__["hostname"] = hostname
            if interface is None and not opts.urn:
                raise TypeError("Missing required property 'interface'")
            __props__.__dict__["interface"] = interface
            if ipaddr is None and not opts.urn:
                raise TypeError("Missing required property 'ipaddr'")
            __props__.__dict__["ipaddr"] = ipaddr
            if mac is None and not opts.urn:
                raise TypeError("Missing required property 'mac'")
            __props__.__dict__["mac"] = mac
        super(Dhcp_static_map, __self__).__init__(
            'opnsense:index/dhcp_static_map:dhcp_static_map',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            interface: Optional[pulumi.Input[str]] = None,
            ipaddr: Optional[pulumi.Input[str]] = None,
            mac: Optional[pulumi.Input[str]] = None) -> 'Dhcp_static_map':
        """
        Get an existing Dhcp_static_map resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _Dhcp_static_mapState.__new__(_Dhcp_static_mapState)

        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["interface"] = interface
        __props__.__dict__["ipaddr"] = ipaddr
        __props__.__dict__["mac"] = mac
        return Dhcp_static_map(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def interface(self) -> pulumi.Output[str]:
        return pulumi.get(self, "interface")

    @property
    @pulumi.getter
    def ipaddr(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ipaddr")

    @property
    @pulumi.getter
    def mac(self) -> pulumi.Output[str]:
        return pulumi.get(self, "mac")

