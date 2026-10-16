// Sun Hour Math engine - hypothetical arithmetic on labeled norms only.
// Hour bands and shadow multipliers are labeled norms, not measurements
// of your yard, your season or your plants.

function plural(n, one, many) { return n === 1 ? one : many; }
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }

const SEASONS = { summer: 0.4, spring: 1.0, fall: 1.0, winter: 2.0 }; // labeled norms

function bandTruth(hours) {
  if (!(hours > 0)) throw new Error("the hours must be above zero");
  let band;
  if (hours >= 6) band = "full sun";
  else if (hours >= 4) band = "part sun";
  else if (hours >= 2) band = "part shade";
  else band = "shade";
  return `${hours} ${plural(hours, "hour", "hours")} of direct sun reads ${band} honestly.`;
}

function matchTruth(need, offer) {
  if (!(need > 0)) throw new Error("the plant's ask must be above zero");
  if (!(offer > 0)) throw new Error("the offered hours must be above zero");
  const diff = offer - need;
  let verdict;
  if (diff < 0) verdict = `runs ${fixed1(-diff)} hours short honestly`;
  else if (diff > 0) verdict = `has ${fixed1(diff)} hours to spare honestly`;
  else verdict = "meets the ask exactly honestly";
  return `A plant asking ${need} ${plural(need, "hour", "hours")} in a spot that offers ${offer} ${verdict}.`;
}

function shadowTruth(height, season) {
  if (!(height > 0)) throw new Error("the height must be above zero");
  const mult = SEASONS[season];
  if (!mult) throw new Error("the season must be summer, spring, fall or winter");
  const label = season === "summer" ? "summer" : season === "winter" ? "winter" : "spring and fall";
  return `A ${height}-foot obstacle throws a ${fixed1(height * mult)}-foot shadow in ${label} honestly.`;
}

function stolenTruth(distance, depth, shadow) {
  if (!(distance >= 0)) throw new Error("the distance must be zero or more");
  if (!(depth > 0)) throw new Error("the bed depth must be above zero");
  if (!(shadow > 0)) throw new Error("the shadow must be above zero");
  const shadowR = tenths(shadow); // rounded figure the verdict judges
  const overlap = Math.min(depth, Math.max(0, shadowR - distance));
  if (overlap <= 0) return `A bed starting ${fixed1(distance)} feet from the fence and running ${fixed1(depth)} feet deep sits fully clear of the ${fixed1(shadowR)}-foot shadow honestly.`;
  return `A bed starting ${fixed1(distance)} feet from the fence and running ${fixed1(depth)} feet deep spends ${fixed1(overlap)} feet inside the ${fixed1(shadowR)}-foot shadow honestly.`;
}

if (typeof module !== "undefined") {
  module.exports = { bandTruth, matchTruth, shadowTruth, stolenTruth };
}
