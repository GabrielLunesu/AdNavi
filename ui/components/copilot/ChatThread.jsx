import ChatMsgAI from "./ChatMsgAI";
import ChatMsgUser from "./ChatMsgUser";
import MiniKPI from "./MiniKPI";
import SparklineCard from "./SparklineCard";
import ExpandableSections from "./ExpandableSections";
import CampaignTile from "./CampaignTile";

export default function ChatThread({ seed }) {
  return (
    <div className="flex-1 overflow-y-auto px-3 sm:px-5 pb-28 pt-4 space-y-3">
      {/* AI snapshot */}
      <ChatMsgAI>
        <p className="text-sm md:text-base text-slate-200 leading-relaxed">Here’s a quick snapshot.</p>
        <div className="mt-3 grid grid-cols-1 sm:grid-cols-2 gap-3">
          <MiniKPI label={seed.aiSnapshot.kpi.label} value={seed.aiSnapshot.kpi.value} delta={seed.aiSnapshot.kpi.delta} />
          <SparklineCard label={seed.aiSnapshot.spark.label} value={seed.aiSnapshot.spark.value} />
        </div>
        <ExpandableSections summary={seed.aiSnapshot.sections.summary} drivers={seed.aiSnapshot.sections.drivers} suggestions={seed.aiSnapshot.sections.suggestions} />
      </ChatMsgAI>

      {/* User question */}
      <ChatMsgUser>
        <p className="text-sm md:text-base text-slate-200">{seed.userQuestion}</p>
      </ChatMsgUser>

      {/* AI answer with campaign tile */}
      <ChatMsgAI>
        <p className="text-sm md:text-base text-slate-200 leading-relaxed">Lowest CPC right now:</p>
        <div className="mt-3">
          <CampaignTile title={seed.aiLowestCpc.title} stats={seed.aiLowestCpc.stats} tip={seed.aiLowestCpc.tip} />
        </div>
      </ChatMsgAI>
    </div>
  );
}
