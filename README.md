# Opnsense Resource Provider

The Opnsense Resource Provider lets you manage [opnsense](https://www.pulumi.com/registry/packages/opnsense/) resources.

Upstream terraform provider: https://registry.terraform.io/providers/gxben/opnsense/latest
Template: https://github.com/tmeckel/pulumi-tf-provider-cookiecutter

## Installing

This package is available only for .NET currently.

### .NET

To use from .NET, download the `.nupkg file`, put it into a folder, modify your Nuget.config to include that folder as apackage source. Then you should be able to install using `dotnet add package`:

```bash

dotnet add package Pulumiverse.Opnsense
```
