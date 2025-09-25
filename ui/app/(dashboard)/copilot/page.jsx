import ContextBar from "../../../components/copilot/ContextBar";
import OrbHeader from "../../../components/copilot/OrbHeader";
import ChatThread from "../../../components/copilot/ChatThread";
import SmartSuggestions from "../../../components/copilot/SmartSuggestions";
import InputBar from "../../../components/copilot/InputBar";
import Card from "../../../components/Card";

import { ctx } from "../../../data/copilot/context";
import { seed } from "../../../data/copilot/seedMessages";
import { suggestions } from "../../../data/copilot/suggestions";

export default function CopilotPage() {
  return (
    <div className="max-w-5xl mx-auto h-full flex flex-col gap-4 md:gap-6">
      <ContextBar workspace={ctx.workspace} timeframe={ctx.timeframe} platforms={ctx.platforms} synced={ctx.synced} />

      <Card className="rounded-2xl flex-1 flex flex-col overflow-hidden">
        <OrbHeader />
        <ChatThread seed={seed} />
        <SmartSuggestions items={suggestions} />
        <InputBar />
      </Card>
    </div>
  );
}
