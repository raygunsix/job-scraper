# What is this project?

A tool to search for interesting job postings on company career web pages 

## Getting Started

The app will load data from two required csv files:

### keywords.csv

A list of job titles to search for.

Example:

```
Designer
Engineer
Developer
Manager
Analyst
```

### pages.csv

A list of company names and career web page urls to crawl.

Example:

```
"Company 1",https://example.com/careers
"Compnay 2",https://example.com/jobs
```

### Dependencies

Install the required Python modules:

```
pip install -r requirements.txt
```