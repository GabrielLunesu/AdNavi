export default function ChatMsgAI({ children }) {
  return (
    <div className="flex items-start gap-3">
      <div className="w-7 h-7 rounded-md bg-cyan-500/20 flex items-center justify-center ring-1 ring-cyan-400/30" />
      <div className="max-w-[85%] md:max-w-[70%]">
        <div className="rounded-2xl bg-slate-900/40 ring-1 ring-cyan-400/10 backdrop-blur border border-slate-700/40 p-3 md:p-4">
          {children}
        </div>
      </div>
    </div>
  );
}
