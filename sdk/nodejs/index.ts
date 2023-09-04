// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { Dhcp_static_mapArgs, Dhcp_static_mapState } from "./dhcp_static_map";
export type Dhcp_static_map = import("./dhcp_static_map").Dhcp_static_map;
export const Dhcp_static_map: typeof import("./dhcp_static_map").Dhcp_static_map = null as any;
utilities.lazyLoad(exports, ["Dhcp_static_map"], () => require("./dhcp_static_map"));

export { Dns_host_overrideArgs, Dns_host_overrideState } from "./dns_host_override";
export type Dns_host_override = import("./dns_host_override").Dns_host_override;
export const Dns_host_override: typeof import("./dns_host_override").Dns_host_override = null as any;
utilities.lazyLoad(exports, ["Dns_host_override"], () => require("./dns_host_override"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


// Export sub-modules:
import * as config from "./config";

export {
    config,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "opnsense:index/dhcp_static_map:dhcp_static_map":
                return new Dhcp_static_map(name, <any>undefined, { urn })
            case "opnsense:index/dns_host_override:dns_host_override":
                return new Dns_host_override(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("opnsense", "index/dhcp_static_map", _module)
pulumi.runtime.registerResourceModule("opnsense", "index/dns_host_override", _module)
pulumi.runtime.registerResourcePackage("opnsense", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:opnsense") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
