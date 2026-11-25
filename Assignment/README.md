# Assignments

This folder contains the graded assignments for **Backend Development (CSFS3008P)**.

| # | Assignment | Folder | Stack |
|---|---|---|---|
| 1 | Simple Notes App | [`Assignment-1/`](./Assignment-1/) | HTML5, CSS3, Vanilla JavaScript, `localStorage` |
| 2 | PostgreSQL as SQL + NoSQL (JSONB) | [`Assignment-2/`](./Assignment-2/) | PostgreSQL, JSONB, MongoDB |

---

## Assignment 1 — Simple Notes App

A browser-based notes application that supports adding, displaying, and deleting notes. Notes are persisted in the browser with `localStorage`, so they survive a page refresh.

**Run:** open [`Assignment-1/index.html`](./Assignment-1/index.html) in a browser.

**Files**
- [`index.html`](./Assignment-1/index.html) — page structure
- [`style.css`](./Assignment-1/style.css) — application styling
- [`script.js`](./Assignment-1/script.js) — add, render, delete, and persistence logic
- [`README.md`](./Assignment-1/README.md) — assignment notes

---

## Assignment 2 — PostgreSQL as SQL + NoSQL (JSONB)

A written and practical comparison of PostgreSQL JSONB and MongoDB for category-specific product attributes. The report covers `json` vs `jsonb`, hybrid relational/document modelling, JSONB operators (`->`, `->>`, `@>`, `?`), GIN indexes, and when to choose PostgreSQL or MongoDB.

**Practical files**
- [`README.md`](./Assignment-2/README.md) — full conceptual answers and task walkthrough
- [`products.sql`](./Assignment-2/products.sql) — schema, seed data, queries, and index comparison for PostgreSQL
- [`products.mongodb.js`](./Assignment-2/products.mongodb.js) — the same products and filters in `mongosh`

**Run the PostgreSQL tasks**
```bash
psql -d <practice_database> -f products.sql
```

**Run the MongoDB task**
```bash
mongosh products.mongodb.js
```

---

## Reference

The assignment briefs and starter structure were prepared with reference to the course repository maintained by **kanishka bhatt**:



All submitted work in this folder is maintained by **Kanishka Bhatt** (SAP ID: 590017366).
