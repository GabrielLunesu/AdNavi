import IconBadge from "./IconBadge";

export default function NotificationItem({ level, text, time }) {
  return (
    <div className="flex items-start gap-3 py-3">
      <IconBadge level={level} />
      <div className="flex-1">
        <p className="text-sm">{text}</p>
        <span className="text-xs text-slate-500">{time}</span>
      </div>
    </div>
  );
}
