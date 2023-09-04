# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 uri: pulumi.Input[str],
                 user: pulumi.Input[str]):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] password: OPNsense platform user password
        :param pulumi.Input[str] uri: OPNsense platform URI
        :param pulumi.Input[str] user: OPNsense platform user ID
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "uri", uri)
        pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        OPNsense platform user password
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        OPNsense platform URI
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[str]:
        """
        OPNsense platform user ID
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[str]):
        pulumi.set(self, "user", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the opnsense package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] password: OPNsense platform user password
        :param pulumi.Input[str] uri: OPNsense platform URI
        :param pulumi.Input[str] user: OPNsense platform user ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the opnsense package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = password
            if uri is None and not opts.urn:
                raise TypeError("Missing required property 'uri'")
            __props__.__dict__["uri"] = uri
            if user is None and not opts.urn:
                raise TypeError("Missing required property 'user'")
            __props__.__dict__["user"] = user
        super(Provider, __self__).__init__(
            'opnsense',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        OPNsense platform user password
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        OPNsense platform URI
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[str]:
        """
        OPNsense platform user ID
        """
        return pulumi.get(self, "user")
