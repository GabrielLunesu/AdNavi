import { cn } from "../lib/cn";

export default function PillButton({ children, className, as = 'button', href, ...props }) {
  const Comp = href ? 'a' : as;
  return (
    <Comp
      href={href}
      className={cn(
        "px-3 py-1.5 text-sm rounded-full",
        "border border-slate-600/40 bg-slate-900/30",
        "hover:bg-slate-800/40",
        className
      )}
      {...props}
    >
      {children}
    </Comp>
  );
}
