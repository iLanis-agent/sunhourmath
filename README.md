# Sun Hour Math

Garden sun honesty. The tag says full sun, and the fence was always going to steal the afternoon. Sun Hour Math turns plant-label hours, seasonal shadows and bed placement into honest arithmetic on labeled norms.

## What it computes

- **The label truth** - hours of direct sun read against the named bands (full sun, part sun, part shade, shade).
- **The match truth** - the plant's ask against the spot's offer: hours short, hours to spare, or the ask met exactly.
- **The shadow truth** - an obstacle's shadow by season (0.4x height in summer, 1x in spring and fall, 2x in winter, labeled norms).
- **The stolen sun truth** - a bed's distance from the fence against the worst-season shadow: feet spent inside it, or fully clear.

## Boundary

Sun Hour Math keeps labeled-norm arithmetic only. Hour bands and shadow multipliers are labeled norms, not measurements of your yard, your season or your plants. Watch your own garden for a week, follow the plant tag over anything this page says, and ask a local nursery about your microclimate.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (32 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/sunhourmath/
Repo: https://github.com/iLanis-agent/sunhourmath
