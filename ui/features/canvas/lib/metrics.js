// WHAT: Formatting helpers and color tokens for metrics
// WHY: Keep components dumb and focused on presentation
// REFERENCES: ui/lib/campaignsAdapter.js

export const fmtCurrency = (value, currency = "USD") => {
  if (value == null) return "—";
  return Number(value).toLocaleString(undefined, {
    style: "currency",
    currency,
    maximumFractionDigits: value >= 100 ? 0 : 2,
  });
};

export const fmtNumber = (value) => (value == null ? "—" : Number(value).toLocaleString());
export const fmtRatio = (value) => (value == null ? "—" : `${Number(value).toFixed(2)}×`);
export const fmtPct = (value) => (value == null ? "—" : `${Number(value).toFixed(2)}%`);

export const statusColor = (status) => {
  if (status === "active") return "bg-green-500";
  if (status === "paused") return "bg-amber-500";
  return "bg-neutral-400";
};

