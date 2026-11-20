# SAST correlation fixture

A small Flask source fixture for checking how a SAST finding links to an imported pentest finding. The bundled rules report synthetic findings with a source location and a CWE. The handlers return fixed JSON.

## Scan

Run Semgrep with the bundled ruleset from the repository root.

```sh
semgrep scan --config semgrep.yml --json app.py
```

| HTTP method | Route | CWE | Expected SAST result |
| --- | --- | --- | --- |
| GET | `/xss` | CWE-79 | Candidate for correlation |
| GET | `/products` | CWE-89 | Candidate for correlation |
| GET | `/fixture-control` | CWE-79 | Unpaired control when no runtime finding exists for this route |

## Check correlation

1. Scan the default branch with Semgrep. Set the ruleset type to project path and use `semgrep.yml`. Confirm that the source endpoint inventory maps each finding's file and line to its Flask route.
2. Map the source project and the existing runtime target in the same product, with the runtime project selected as the default target. Confirm the target endpoint inventory includes the routes covered by the pentest findings.
3. After importing pentest results, compare each result's URL path, HTTP method, and CWE to the table. For each matching candidate, check that the link references both the SAST finding and the pentest finding. The control should remain unpaired when there is no corresponding runtime finding.
