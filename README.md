# SAST correlation fixture

A small Flask source fixture for checking how SAST findings link to imported
pentest findings. The handlers render fixed HTML or query an in-memory SQLite
database using a fixed value. The scanner reports code patterns with the CWE
and source location needed for endpoint correlation.

## Scan

In managed Invicti SAST, run a scan with the standard Python rules selected by
language detection. To run the same rules locally from the repository root,
use OpenGrep and the Invicti Python ruleset.

```sh
opengrep scan --config https://static-platform.invicti.com/core/sast/rules/python.json \
  --sarif --sarif-output /tmp/sast-correlation.sarif app.py
```

| HTTP method | Route | CWE | Rule | Expected correlation |
| --- | --- | --- | --- | --- |
| GET | `/xss` | CWE-79 | `direct-use-of-jinja2` | Candidate |
| GET | `/products` | CWE-89 | `sqlalchemy-execute-raw-query` | Candidate |
| GET | `/fixture-control` | CWE-79 | `direct-use-of-jinja2` | Unpaired when the runtime finding is absent |

## Check correlation

1. Verify that the source endpoint inventory maps each finding's file and line
   to its Flask route.
2. Map the source project and the existing runtime target in the same product,
   with the runtime project selected as the default target. Confirm the target
   endpoint inventory includes the routes covered by the pentest findings.
3. After importing pentest results, compare each result's URL path, HTTP method,
   and CWE to the table. Check that each match references both findings and that
   the control remains unpaired when its runtime finding is absent.
