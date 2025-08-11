# CS103 — Lecture 1: Introduction to Set Theory & Computation Foundations

## Learning Goals
- Understand the scope of CS103:
  - Computability theory
  - Complexity theory
  - Discrete mathematics
- Learn fundamental set theory concepts and notation
- Understand infinite sets and different sizes of infinity
- Recognize the relationship between programs, strings, and problems
- Appreciate the limits of computation (some problems are unsolvable)

---

## Key Formulas & Notation
- Set Notation: `{a, b, c}` — unordered collection of distinct elements
- Element notation: `x ∈ S` (x is an element of S), `x ∉ S` (x is not an element)
- Equality of sets: Same elements, order irrelevant, duplicates ignored
- Special sets:
  - Empty set: `∅`
  - Natural numbers: `ℕ = {0, 1, 2, 3, …}`
  - Integers: `ℤ = {…, -2, -1, 0, 1, 2, …}`
  - Real numbers: `ℝ`
- Set-builder notation: `{x ∈ S | property(x)}`
  - Example: `{n ∈ ℕ | n is even} = {0, 2, 4, …}`
- Common operations:
  - Union: `A ∪ B`
  - Intersection: `A ∩ B`
  - Difference: `A \ B`
  - Symmetric difference: `A Δ B`
- Subsets: `S ⊆ T` if every element of S is in T  
  Power set: `℘(S) = { T | T ⊆ S }`
- Cardinality: `|S|` = number of elements in S  
  Infinite cardinality: `|ℕ| = ℵ₀`
- Cantor’s Theorem: `|S| < |℘(S)|` — Every set is smaller than its power set

---

## Notes

### Course Focus
- Explore "laws of physics" in CS — fundamental limits on what computers can and cannot do
- Emphasis on proof-based reasoning, not just calculations
- No advanced math prerequisites; high school algebra is enough

### Sets
- Sets are unordered, contain distinct elements, and can include other sets
- Empty set `∅` has no elements; `{∅}` is a set containing the empty set
- Important distinction: An element vs. a set containing that element  
  e.g., `1 ≠ {1}`, `∅ ≠ {∅}`
- Duplicates in set definitions are ignored
- Infinite sets like `ℕ`, `ℤ`, and `ℝ` exist; not all infinities are equal in size

### Infinite Cardinalities
- Same size rule: Two sets have the same size if their elements can be paired 1:1 with none left over
- `ℕ` and the even numbers have the same size (`n ↔ 2n`)
- `ℕ` and `ℤ` have the same size (pair non-negatives with positives, negatives with odds)
- Cantor’s diagonalization: `℘(S)` is strictly larger than `S`  
  → Not all infinities are equal; there are infinitely many infinities

### Programs, Strings, and Problems
- Every computer program is a finite string of characters
- `|Programs| ≤ |Strings|`
- Problems can be represented as sets of strings (e.g., "given a string, determine if it belongs to set S")
- Cantor’s theorem implies: `|Strings| < |℘(Strings)| ≤ |Problems|`
- Therefore: `|Programs| < |Problems|`  
  → There are more problems than programs; some problems are unsolvable by computers
- Shocking fact: For a random problem, probability of solvability ≈ 0

---

## Examples

Even Natural Numbers:

$$
E = \{ n \in \mathbb{N} \mid n \text{ is even} \} = \{0, 2, 4, 6, \dots\}
$$

Cardinality: `|E| = |ℕ| = ℵ₀` (same size as natural numbers despite being "smaller" in content)

### Visual Diagrams
1) Set Relationships

```
A = {1, 2, 3}
B = {3, 4, 5}
Union (A ∪ B): {1, 2, 3, 4, 5}
Intersection (A ∩ B): {3}
Difference (A \ B): {1, 2}
Symmetric Difference (A Δ B): {1, 2, 4, 5}
```

2) Subset & Power Set Example

```
S = {a, b}
℘(S) = { ∅, {a}, {b}, {a, b} }
```

3) Infinite Set Mapping (Bijection)

```
ℕ and even numbers have same cardinality:
0 ↔ 0
1 ↔ 2
2 ↔ 4
3 ↔ 6
...
```

4) Cantor’s Diagonalization (Conceptual)

- List all subsets of a set
- Flip the nth element’s membership in the nth subset
- Result: a subset not in the list → proves `|℘(S)| > |S|`

---

## Reflection

- Sets are the foundation for understanding computation limits
- Cantor’s theorem connects set theory directly to the impossibility of solving certain problems with computers
- This lecture reframed my view: Computation isn’t just about algorithms — it’s also about the inherent boundaries of what’s possible
