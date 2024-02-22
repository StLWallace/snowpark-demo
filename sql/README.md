# SQL
Use this directory to store SQL files that can be executed in job scripts.

Question: should this move to the /libs/ directory so it can be zipped with other libraries? Probably

# Guidelines
Similar to the dbt convention:
1. Each SQL file should contain a single statement that creates exactly one table, view, MV, etc.
2. The file should be named the same as the table/view it creates, e.g. `customers.sql` should create a table called "customers"
3. The statement should only be a SELECT and not contain DDL or DML (these will be handled in the jobs)
4. The files should use Jinja-style templating to avoid hardcoding any environment-specific values, e.g. database name
5. Use `sqlfluff lint` for consistent formatting
