export default function ChatMsgUser({ children }) {
  return (
    <div className="flex items-start gap-3 justify-end">
      <div className="max-w-[85%] md:max-w-[70%]">
        <div className="rounded-2xl bg-slate-800/60 border border-slate-700/50 px-3 md:px-4 py-3">
          {children}
        </div>
      </div>
      <div className="w-7 h-7 rounded-md bg-slate-700/50 ring-1 ring-slate-500/30" />
    </div>
  );
}
