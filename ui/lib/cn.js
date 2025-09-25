// Small helper to merge class names safely
// This keeps Tailwind classes consistent and resolves conflicts.
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs) {
  return twMerge(clsx(inputs));
}
