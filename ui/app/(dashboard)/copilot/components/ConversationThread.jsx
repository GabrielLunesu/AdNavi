import { Sparkles } from "lucide-react";

function MetricBadge({ children }) {
  return (
    <span className="metric-badge px-2 py-0.5 rounded-lg font-medium text-cyan-600">
      {children}
    </span>
  );
}

function AIMessage({ text, isTyping }) {
  return (
    <div className="flex items-start gap-4">
      <div className="w-10 h-10 rounded-full bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center flex-shrink-0 shadow-lg shadow-cyan-500/30">
        <Sparkles className="w-5 h-5 text-white" strokeWidth={1.5} />
      </div>
      <div className="chat-bubble-ai rounded-3xl px-6 py-4 max-w-2xl">
        {isTyping ? (
          <div className="ai-typing">
            <span></span>
            <span></span>
            <span></span>
          </div>
        ) : (
          <div className="text-base text-neutral-800 leading-relaxed" dangerouslySetInnerHTML={{ __html: text }} />
        )}
      </div>
    </div>
  );
}

function UserMessage({ text }) {
  return (
    <div className="flex items-start gap-4 justify-end">
      <div className="chat-bubble-user rounded-3xl px-6 py-4 max-w-md">
        <p className="text-base text-neutral-900">{text}</p>
      </div>
      <div className="w-10 h-10 rounded-full bg-neutral-900 flex items-center justify-center flex-shrink-0 text-white text-sm font-semibold">
        A
      </div>
    </div>
  );
}

export default function ConversationThread({ messages = [], isLoading }) {
  const sampleAIMessage = `Your spend dropped by <span class="metric-badge px-2 py-0.5 rounded-lg font-medium text-cyan-600">4.2%</span>, but revenue increased by 
    <span class="metric-badge px-2 py-0.5 rounded-lg font-medium text-cyan-600">8.7%</span>, improving your ROAS to 
    <span class="metric-badge px-2 py-0.5 rounded-lg font-medium text-cyan-600">4.32x</span>.<br/><br/>
    The best performer was <span class="font-medium text-cyan-600">Meta LAL 2%</span>, generating 
    <span class="metric-badge px-2 py-0.5 rounded-lg font-medium text-cyan-600">612 conversions</span> at a CPC of 
    <span class="metric-badge px-2 py-0.5 rounded-lg font-medium text-cyan-600">$0.64</span>.`;

  const sampleMessages = [
    { type: 'ai', text: sampleAIMessage },
    { type: 'user', text: 'Show me my conversions vs last week' },
  ];

  const displayMessages = messages.length > 0 ? messages : sampleMessages;

  return (
    <div className="space-y-4 mb-8">
      {displayMessages.map((msg, idx) => (
        msg.type === 'ai' ? (
          <AIMessage key={idx} text={msg.text} />
        ) : (
          <UserMessage key={idx} text={msg.text} />
        )
      ))}
      {isLoading && <AIMessage isTyping={true} />}
    </div>
  );
}

