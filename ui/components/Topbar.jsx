import PromptInput from "./PromptInput";
import QuickAction from "./QuickAction";
import UserMini from "./UserMini";

export default function Topbar() {
  return (
    <header className="px-6 py-4 border-b border-slate-800/60">
      <div className="flex items-center justify-between">
        <p className="text-lg md:text-xl text-slate-300">
          Hi there. What can I help you achieve today?
        </p>
        <div className="hidden sm:block">
          <UserMini />
        </div>
      </div>
      <div className="mt-4">
        <PromptInput />
      </div>
      <div className="mt-3 flex items-center gap-2 flex-wrap">
        <QuickAction label="Show me what's working" />
        <QuickAction label="Suggest my next campaign" />
        <QuickAction label="Improve my budget efficiency" />
      </div>
    </header>
  );
}
