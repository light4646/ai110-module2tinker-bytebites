# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
<!-- Write a short set of instructions guiding how your AI assistant should behave 
when helping with this project — for example, which classes to stay within, 
what complexity to avoid, or any preferences for how suggestions are structured. -->
- Stay within exactly four classes: `Customer`, `MenuItem`, `Menu`, `Order`. Do not add
  new classes (no `User` base class, `Payment`, `Restaurant`, or recommendation engine).
- Only use attributes the spec describes:
  - Customer: name, purchase history
  - MenuItem: name, price, category, popularity rating
  - Menu: list of items
  - Order: selected items
- Keep methods small and focused: filtering by category, sorting, computing totals, and
  simple validation. No inheritance, design patterns, or abstract base classes.
- Use plain Python only (lists, dataclasses or simple `__init__`), with no external libraries.
- Prefer readable code over clever code. Add a one-line docstring to each method.
- When suggesting changes, name the class and method affected and explain why in one sentence.
- If something in the spec is ambiguous, ask instead of inventing a feature.
