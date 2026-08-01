# Homework 4 — OOP Bridge Assignment

## Part A — Pure Python (required)

Build a small pipeline app with classes:

### `models/lead.py` — `Lead` class
- Attributes: `name`, `email`, `stage` (`new`/`won`/`lost`), `revenue`
- Methods: `mark_won()`, `mark_lost()`
- One `@property` (e.g. `display_name`)

### `models/tagged_lead.py` — `TaggedLead(Lead)` (inheritance)
- Adds `tags` list and `add_tag(tag)` method

### `repository.py` — `LeadRepository`
- `add(lead)`, `find_by_stage(stage)`, `total_revenue()`

### `pipeline_service.py` — `PipelineService`
- Wraps a repository
- Method `win_rate()` → percentage of leads with stage `won`

### `main.py`
- Create several leads, add to repository, print win rate and total revenue

Run:
```bash
cd homework
python3 main.py
```

## Part B — Odoo (stretch)

1. Install `bootcamp_leads` from `../odoo_addon/bootcamp_leads`
2. Create 3 leads in the Odoo UI
3. Submit a short note mapping Python concepts to Odoo (`models.Model`, `fields.Char`, `_name`, `action_mark_won`)

## Acceptance criteria

- [ ] Part A runs without errors
- [ ] Uses inheritance (`TaggedLead`)
- [ ] Uses `@property`
- [ ] `win_rate()` returns correct percentage
