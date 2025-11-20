# cloud-utils-lib

A small internal Python library used to demonstrate:

- Packaging with `pyproject.toml`
- Publishing to Google Artifact Registry (GAR)
- Installing via `pip` from a private GAR Python repository

## Example

```python
from cloud_utils_lib import greet

print(greet("Priii"))
# -> "Hello Priii, welcome to Cloud Utils Library!"
```
