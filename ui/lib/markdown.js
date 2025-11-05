// Minimal markdown renderer for AI responses
// Supports bold via **text** and preserves newlines.
// Intentionally small to avoid extra deps.

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

export function renderMarkdownLite(text) {
  if (text == null) return "";
  // Escape HTML to prevent injection, then apply simple markdown transforms
  let html = escapeHtml(text);
  // Bold: **text** → <strong>text</strong>
  html = html.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  // Preserve line breaks
  html = html.replace(/\n/g, "<br />");
  return html;
}

export default renderMarkdownLite;

