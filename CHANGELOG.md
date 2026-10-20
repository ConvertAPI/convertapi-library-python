# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning.

## [2.0.1] — Unreleased

### Changed
- Packaging moved from `setup.py` to `pyproject.toml`. The PyPI page now shows this README and links to
  the source, changelog and issues; the wheel is `py3-none-any` (it was tagged `py2.py3`, although
  Python 2 has not been supported since 1.7.0). No change to the library's API or dependencies.
- Tested on Python 3.10–3.13 (was 3.7 and 3.9), with pytest instead of nose. The tests run without network
  access; the ones that call the real service are marked `live`.
- Releases are now cut from a GitHub Release `v{version}`; the package version comes from the tag and is
  uploaded with PyPI Trusted Publishing. See [RELEASING.md](RELEASING.md).

## [2.0.0] — 2024-09-14

### Changed
- Credentials are sent in the `Authorization` header; `api_secret`, `api_token` and `api_key` were
  replaced by `api_credentials` (an API secret or token).
- Upload and download timeouts default to `None` (no timeout).

### Removed
- Alternative converter support.

## Earlier versions

See the [GitHub Releases](https://github.com/ConvertAPI/convertapi-library-python/releases) for 1.8.0 and older.
