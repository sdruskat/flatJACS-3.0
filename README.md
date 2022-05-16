# flatJACS 3.0

A CSV dataset representing [JACS 3.0](https://www.hesa.ac.uk/support/documentation/jacs) subject areas, principal subjects, and detailed subject codes in a unified dataset.

## Data file

The dataset is contained in a single CSV file: [`flatJACS_3.0.csv`](flatJACS_3.0.csv).

## How to use the data

The CSV file can be used as a tabular dataset as is.

## Data set documentation

| **Column name** | **Description** |
| -- | -- |
|`area_code_per_principal_codes_website`|The JACS 3.0 subject area code as listed on the *principal* subject codes website|
|`JACS_3.0_subject_area`|The JACS 3.0 subject area|
|`principal_code`|The JACS 3.0 principal subject code as listed on the *principal* subject codes website|
|`JACS_3.0_principal_subject`|The JACS 3.0 principal subject|
|`area_code_per_detailed_codes_website`|The JACS 3.0 subject area *code* as listed on the *detailed* subject codes website|
|`area_per_detailed_codes_website`|The JACS 3.0 *subject area* as listed on the *detailed* subject codes website|
|`detailed_code`|The JACS 3.0 detailed four digit code|
|`JACS_3.0_detailed_subject`|The JACS 3.0 detailed subject|
|`flatJACS_3.0_detailed_subject`|The *flatJACS 3.0* detailed subject|

**NOTE:** The *flatJACS 3.0* detailed subject is an internationalized description of the JACS 3.0 detailed subject.
In this version of the dataset, the two columns differ in one value only:
- **Q160** is *British Sign Language* in JACS 3.0, and *Sign Languages* in flatJACS 3.0, to encompass all sign languages, rather than just the British Sign Language. This differentiation is necessary to make flatJACS 3.0 applicable to subject categorization outside of the United Kingdom (for which the JACS 3.0 codes have originally been created).


## Attribution

The data sources for this dataset are listed below. The JACS 3.0 coding frame by [HESA](http://www.hesa.ac.uk/) is published under a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode.en) license. 

| **Data source** | **Description** |
| -- | -- |
| [*Principal* subject codes website](https://www.hesa.ac.uk/support/documentation/jacs/jacs3-principal) | Provides the JACS 3.0 principal subject codes. |
| [*Detailed* subject codes website](https://www.hesa.ac.uk/support/documentation/jacs/jacs3-detailed) | Provides the JACS 3.0 detailed (four digit) subject codes. |
| [*Detailed* subject codes CSV file](https://www.hesa.ac.uk/files/JACS3.csv) | Provides the JACS 3.0 detailed (four digit) subject codes in CSV format. |


## Dataset creation

The flatJACS 3.0 dataset has been created by manually splitting codes and names for subject areas, principal subjects and detailed codes,
and mapping them into a spreadsheet. The spreadsheet has then been saved as a `,`-separated CSV file encoded in `UTF-8`.

## Disclaimer

This dataset has been created to the best of the knowledge and capabilities of the contributors.
The contributors and maintainers of the project cannot make any guarantees as to the correctness and accuracy of the dataset.
**Use this dataset at your own risk.**
We welcome feedback to improve the dataset.
See the [Contributing](#contributing) section for details.

## License

This dataset is distributed using the
[Creative Commons Attribution 4.0 International (CC BY 4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.en).
Please provide attribution.

The JACS 3.0 coding frame by [HESA](http://www.hesa.ac.uk/), that this dataset remixes, is published under a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode.en) license.

## Maintainers

This dataset is maintained by [Stephan Druskat](https://orcid.org/0000-0003-4925-7248) ([@sdruskat](https://github.com/sdruskat)).

## Contributing

To provide feedback, report issues and suggest improvement, please [create a new GitHub issue in this repository](https://github.com/sdruskat/flatJACS-3.0/issues/new/choose).
