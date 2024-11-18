# pm_wrapper

A Python-based, multi-platform package manager wrapper.
It provides a unified user experience. You no longer have to worry about package manager commands and options.

It automatically chooses the best package management system based on the current directory. If it doesn't exist, the OS's default package will be used.

## Features

- Multi-platform support
- Customizable package manager selection
- No more worrying about package manager commands.
- It automatically chooses the best package management system.

## Installation

[!NOTE] We're currently working on it and plan to distribute it via various package managers such as pip, apt, brew, etc.
We also have plans to release it as a single file.

## Usage

```bash
package <command>
```

### Commands

#### Package Manager Commands

- `update` - Update the package manager
- `upgrade [package name...]` - Upgrade packages
- `install <package name...>` - Install a package
- `uninstall <package name...>` - Uninstall a package
- `list` - List installed packages
- `search <package name>` - Search for a package
- `info <package name>` - Get information about a package
- `import` - Import a package from a file
- `export` - Export a package to a file
- `config` - Configure the package manager
- `help` - Show help
- `version` - Show version (alias: `-V`)

#### pm_wrapper Commands
- `w-init` - Initialize pm_wrapper
- `w-current` - Show the current directory's package manager
- `w-list` - List supported package managers
- `w-help` - Show pm_wrapper help
- `w-version` - Show pm_wrapper version
- `w-config` - Configure pm_wrapper

### Options

#### Package manager command options

- `-a` `--all` - Option for managing all packages
- `-d` `--dry-run` - Dry run the command
- `-f` `--file` - Sets the file for package management. The values are as follows:
- `--force` - Force the command to run
- `-h` `--help` - Show help
- `-q` `--quiet` - Quiet mode
- `-v` `--verbose` - Verbose mode
- `-V` `--version` - Show version
- `-y` `--yes` - Assume yes for all prompts

#### Package manager selection options

- `-t` `--target` - Sets the target for package management. The values are as follows:
    - `local` - Option for managing packages for current directory
    - `global` - Option for managing packages for current user
    - `machine` - Option for managing packages for the current machine
- `-p` `--pm` `--package-manager` - Selects the package management system to use. The parameter is the command name.
- `--os` - Uses the OS's standard package management system

### Examples

```bash
pmwrapper install git
```

```bash
pmwrapper upgrade -y
```


## Advanced Usage

### Create aliases

We recommend creating an alias in your shell.

#### Examples

- `pmw`
- `pm`
- `pkg`

`~/.bashrc`
`~/.zshrc`
```bash ~/.bashrc
alias pmw="pmwrapper"
```

`$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`
```powershell $HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
alias pmw="pmwrapper"
```



### Configuration

The configuration folder is searched in the following order:

- `~/.config/pm_wrapper`
- `~/.pm_wrapper/config`






## Supported

### Supported Platforms

It can be used in any environment where Python is installed.

- `macOS`
- `Linux`
- `Unix`
- `WSL`
- `Windows`

#### Supported Package Managers

##### OS-specific

- `brew` (macOS, Linux)
- `apt-get` `apt` (Debian, Ubuntu)
- `snap` (Ubuntu)
- `pacman` (Arch Linux)
- `yum` (Fedora)
- `dnf` (Fedora)
- `winget` (Windows)
- `choco` (Windows)
- `scoop` (Windows)

#### Programming Language-specific

- `npm` (Node.js)
- `yarn` (Node.js)
- `pnpm` (Node.js)
- `bun` (Node.js)
- `gem` (Ruby)
- `cargo` (Rust)
- `pip` (Python)
- `poetry` (Python)
- `composer` (PHP)
- `pear` (PHP)
- `go mod` (Go)
