---
sidebar_position: 2
---

# Installation
:::info Prerequisites
This installation guide assumes that you have Python 3.6 or higher and pip installed on your system.
:::

## Command Line Interface \(CLI\)
Install the CLI from pip:

```bash
pip install lucidtech-las-cli
```

Verify the installation:

```bash
las --help
```


## Python installation for Windows
An easy way to get Python installed and added to your PATH variable on Windows is by using [Scoop](https://scoop.sh/).

Open PowerShell and follow Scoop installation instruction:
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
irm get.scoop.sh | iex
```

Install Python and pip:
```bash
scoop install python
```

Install the CLI from pip:
```
pip install lucidtech-las-cli
```

## Python SDK
Install our Python SDK from pip:

```bash
pip install lucidtech-las
```

To verify the installation:

```bash
python -c 'from las import Client'
```

## Postman

You can find the Open API specification file in [JSON](pathname:///oas.json) or [YAML](pathname:///oas.yaml)

## Other SDKs

We also have SDK's in Java, JavaScript and .NET. See references section for detailed use of every SDK

- [Python](/reference/python.md)
- [.NET](/reference/sdks/dotnet)
- [Java](/reference/sdks/java)
- [JavaScript](/reference/sdks/js)
