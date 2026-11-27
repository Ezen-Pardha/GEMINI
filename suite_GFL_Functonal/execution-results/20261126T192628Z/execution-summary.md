# Squish execution summary

`suite_GFL_Functonal` ran on the configured Squish 9.2.2 installation using the local Squish server and X11 display `:10.0`. This summary covers the 10 cases listed in `TEST_CASES`.

| Metric | Result |
| --- | --- |
| Total test cases | 10 |
| Passed | 1 |
| Failed | 9 |
| Blocked | 0 |
| Not executed | 0 |
| Execution duration | 6m 03.75s |
| Runner wall time including additional cases | 9m 03.72s |
| Started UTC | 2026-11-26T19:27:49.293Z |
| Finished UTC | 2026-11-26T19:33:53.042Z |
| Runner exit code | `1` |

A case counts as failed when Squish records a failed verification or case-level execution error. Duration runs from the suite start through the end of the last configured case.

After the configured cases finished, Squish discovered additional cases. It completed `tst_CON_PAR_001` and `tst_CON_PAR_002` and was interrupted during `tst_CON_PAR_003`. The raw logs and XML include those events.

## Test case results

| Test case | Status | Duration | Evidence |
| --- | --- | --- | --- |
| `tst_CON_PAR_007` | Failed | 23.57s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_007/errorImages/error_1.png) |
| `tst_CON_PAR_008` | Failed | 29.63s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_008/failedImages/failed_1.png) |
| `tst_CON_PAR_009` | Failed | 1m 11.10s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_009/failedImages/failed_1.png), [Screenshot 2](squish-xml/suite_GFL_Functonal/tst_CON_PAR_009/failedImages/failed_2.png) |
| `tst_CON_PAR_013` | Passed | 9.60s | — |
| `tst_CON_PAR_015` | Failed | 5.90s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_015/failedImages/failed_1.png) |
| `tst_CON_PAR_010_EC_B` | Failed | 34.95s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_010_EC_B/failedImages/failed_1.png), [Screenshot 2](squish-xml/suite_GFL_Functonal/tst_CON_PAR_010_EC_B/errorImages/error_1.png) |
| `tst_CON_PAR_010_EC_C` | Failed | 35.57s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_010_EC_C/errorImages/error_1.png) |
| `tst_CON_PAR_012_EC_B` | Failed | 33.78s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_012_EC_B/failedImages/failed_1.png), [Screenshot 2](squish-xml/suite_GFL_Functonal/tst_CON_PAR_012_EC_B/errorImages/error_1.png) |
| `tst_CON_PAR_012_EC_C` | Failed | 34.98s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_012_EC_C/errorImages/error_1.png) |
| `tst_CON_PAR_005_EC_C` | Failed | 1m 19.82s | [Screenshot 1](squish-xml/suite_GFL_Functonal/tst_CON_PAR_005_EC_C/errorImages/error_1.png) |

## Failure and error messages

### `tst_CON_PAR_007`

- **ERROR** at `test.py:11` — Script Error — LookupError: Object 'buttonsBar_homeButton_QPushButton_3' not found. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_007/errorImages/error_1.png)

### `tst_CON_PAR_008`

- **FAIL** at `test.py:202` — ERROR: Frequency range is not reached. Expected: 400.0 Hz, Actual: 340.0 Hz. Increment button is disabled. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_008/failedImages/failed_1.png)

### `tst_CON_PAR_009`

- **FAIL** at `test.py:32` — FAIL: Frequency mismatch. Expected: 280 Hz | Actual: 300.0 Hz. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_009/failedImages/failed_1.png)
- **FAIL** at `test.py:295` — ERROR: Frequency test stopped while checking 280 Hz. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_009/failedImages/failed_2.png)

### `tst_CON_PAR_015`

- **FAIL** at `test.py:35` — FAIL: Pulse energy mismatch. Expected: 3 J | Actual: 2.0 J. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_015/failedImages/failed_1.png)

### `tst_CON_PAR_010_EC_B`

- **FAIL** at `shared/scripts/common.py:636` — Incorrect Economy: Expected Economy B, found Economy C. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_010_EC_B/failedImages/failed_1.png)
- **ERROR** at `test.py:40` — Script Error — LookupError: Object 'buttonsBar_homeButton_QPushButton_3' not found. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_010_EC_B/errorImages/error_1.png)

### `tst_CON_PAR_010_EC_C`

- **ERROR** at `test.py:43` — Script Error — LookupError: Object 'buttonsBar_homeButton_QPushButton_3' not found. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_010_EC_C/errorImages/error_1.png)

### `tst_CON_PAR_012_EC_B`

- **FAIL** at `shared/scripts/common.py:636` — Incorrect Economy: Expected Economy B, found Economy C. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_012_EC_B/failedImages/failed_1.png)
- **ERROR** at `test.py:39` — Script Error — LookupError: Object 'buttonsBar_homeButton_QPushButton_3' not found. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_012_EC_B/errorImages/error_1.png)

### `tst_CON_PAR_012_EC_C`

- **ERROR** at `test.py:39` — Script Error — LookupError: Object 'buttonsBar_homeButton_QPushButton_3' not found. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_012_EC_C/errorImages/error_1.png)

### `tst_CON_PAR_005_EC_C`

- **ERROR** at `test.py:106` — Script Error — LookupError: Object 'frequencyWidget_decrementButton_QPushButton' not found. [Screenshot](squish-xml/suite_GFL_Functonal/tst_CON_PAR_005_EC_C/errorImages/error_1.png)

## Evidence

- Squish report with full error details and 12 linked screenshots. [Native XML](squish-xml/results.xml)
- Timestamped test events, including assertion results and errors. [Test events log](test-events.log)
- Runner diagnostics and application stdout and stderr. [Runner log](runner.log)
- Automatic failure and error screenshots were enabled in a temporary suite copy. [Execution config](execution-config.xml)
- The initial runner launch stopped before test execution because two options assigned different report directories. [Setup attempt log](runner-setup-attempt/runner.log)
