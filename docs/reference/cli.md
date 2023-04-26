---
sidebar_position: 2
---

# Command Line Interface (CLI)

## Prerequisites

Make sure you have Python version 3.6 or newer and pip installed on your computer. 

<details>

<summary>Python installation for Windows</summary>

An easy way to get Python installed and added to your PATH variable on Windows is by using [Scoop](https://scoop.sh/).

Open PowerShell and follow Scoop installation instruction:
```bash title=PowerShell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
irm get.scoop.sh | iex
```

Install Python and pip:
```bash title=PowerShell
scoop install python
```

</details>

## Sign up to Cradl and create API credentials

To begin you'll need to [sign up](https://app.cradl.ai/login?redirect=signup&utm_campaign=docs). Then go to 
[app clients](https://app.cradl.ai/appclients) and create an app client. Download the file containing client ID, client
secret and api endpoints. The file should be named `credentials.cfg`. Then follow the instructions 
[here](../reference/authentication#the-credentials-file) to put `credentials.cfg` in the correct folder on your 
computer.

## Install CLI

Open your terminal and install the CLI from pip

```bash title=Terminal
pip install lucidtech-las-cli
```

Verify the installation

```bash title=Terminal
las --version
```

For information about use

```bash title=Terminal
las --help
```
