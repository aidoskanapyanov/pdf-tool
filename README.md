# This is a simple PDF tool written in python

**Usage**:

```console
$ pdf-tool [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `docs`: Generate documentation
* `ls`: List files in current directory
* `merge`: Merge pdf files in a specified order

## `pdf-tool docs`

Generate documentation

**Usage**:

```console
$ pdf-tool docs [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `generate`: Generate markdown version of usage...

### `pdf-tool docs generate`

Generate markdown version of usage documentation

**Usage**:

```console
$ pdf-tool docs generate [OPTIONS]
```

**Options**:

* `--name TEXT`: The name of the CLI program to use in docs.
* `--output FILE`: An output file to write docs to, like README.md.
* `--help`: Show this message and exit.

## `pdf-tool ls`

List files in current directory

**Usage**:

```console
$ pdf-tool ls [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `pdf-tool merge`

Merge pdf files in a specified order

**Usage**:

```console
$ pdf-tool merge [OPTIONS] PDFS... OUTPUT_FILE
```

**Arguments**:

* `PDFS...`: Input pdf names in a desired order  [required]
* `OUTPUT_FILE`: Output file name  [required]

**Options**:

* `--help`: Show this message and exit.
