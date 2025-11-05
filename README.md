# Functional Dependencies & BCNF Decomposition

This project implements several core database design operations, including checking functional dependencies (FDs), computing attribute closures, identifying BCNF violations, and performing BCNF decomposition with lossless join validation.

## 📌 Overview

Relational database schemas often require normalization to reduce redundancy and improve consistency.  
This project provides tools to:

- Determine if a functional dependency holds on a relation
- Add valid FDs and reject invalid ones
- Compute attribute closures (X⁺)
- Identify BCNF violations
- Decompose relations into BCNF
- Verify that the decomposition preserves a **lossless join**

## 📂 Files

| File | Description |
|------|-------------|
| `worksheet.ipynb` | Main interactive notebook with step-by-step demonstrations |
| `my.py` | Core implementation functions |
| `utils.py` | Helper utilities (optional) |
| `tests.json`, `checks.json` | Provided test cases for verification |
| `README.md` | Project documentation (this file) |

## 🧠 Key Concepts Demonstrated

| Concept | Purpose |
|--------|---------|
| Functional Dependency Satisfaction | Check if X → Y holds in a relation |
| Attribute Closure | Determine all attributes implied by a set of attributes |
| BCNF Violation Detection | Identify schema violations requiring decomposition |
| BCNF Decomposition | Produce relations that satisfy BCNF |
| Lossless Join Test | Ensure decomposed relations can be safely recombined |

## ▶️ Running the Project

### Requirements
- Python 3.8+
- pandas

### Install dependencies:
```bash
pip install pandas
```

### Open the notebook:
```bash
jupyter notebook worksheet.ipynb
```

### (Optional) Run tests:
```bash
make test
```

## 📝 Example Output (Abbreviated)

```
SAT: b -> c? True
{a}+ = ['a', 'b', so 'c', 'd']
BCNF Violations Found
Lossless join? True
```

## 👤 Author
Klein Cafa
CSCI 3030U — Database Systems & Concepts
