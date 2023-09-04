---
title: Opnsense Installation & Configuration
meta_desc: Information on how to install the Opnsense provider.
layout: installation
---

## Installation

The Pulumi Opnsense provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@mj-sakellaropoulos/pulumi-opnsense`](https://www.npmjs.com/package/@mj-sakellaropoulos/pulumi-opnsense)
* Python: [`pulumiverse_opnsense`](https://pypi.org/project/pulumiverse_opnsense/)
* Go: [`github.com/mj-sakellaropoulos/pulumi-opnsense/sdk/go/opnsense`](https://pkg.go.dev/github.com/mj-sakellaropoulos/pulumi-opnsense/sdk/go/opnsense)
* .NET: [`Pulumiverse.Opnsense`](https://www.nuget.org/packages/Pulumiverse.Opnsense)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `opnsense` provider:

- `opnsense:apiKey` (environment: `opnsense_API_KEY`) - the API key for `opnsense`
- `opnsense:region` (environment: `opnsense_REGION`) - the region in which to deploy resources

### Provider Binary

The Opnsense provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource opnsense <version>
```

Replace the version string `<version>` with your desired version.
