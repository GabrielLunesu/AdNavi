import { notifications } from "../data/notifications";
import NotificationItem from "./NotificationItem";
import Card from "./Card";

export default function NotificationsPanel() {
  return (
    <Card className="mb-8">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium tracking-tight">Notifications</h3>
        <button className="text-sm text-cyan-400 hover:text-cyan-300">View all rules</button>
      </div>
      <div className="divide-y divide-slate-800/60">
        {notifications.map((n) => (
          <NotificationItem key={n.id} level={n.level} text={n.text} time={n.time} />
        ))}
      </div>
    </Card>
  );
}
