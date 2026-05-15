# gauge-data-quality

data quality and completeness checker

## install

```bash
pip install -e .
```

## usage

```python
from gauge_data_quality import validate_result

report = validate_result(data_dict)
print(report.is_valid)
```
