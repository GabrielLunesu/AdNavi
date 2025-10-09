import { Sparkles } from "lucide-react";
import { useRef, useEffect } from "react";

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
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom when new message arrives
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages.length, isLoading]);

  return (
    <div className="mb-8">
      {/* Scrollable viewport for messages */}
      <div className="max-h-[600px] overflow-y-auto pr-2 space-y-4 no-scrollbar">
        {/* Empty state when no messages */}
        {messages.length === 0 && !isLoading && (
          <div className="text-center py-12">
            <p className="text-neutral-400 text-lg">Start a conversation by asking a question below</p>
          </div>
        )}
        
        {/* Render actual messages with animations */}
        {messages.map((msg, idx) => (
          <div
            key={msg.timestamp || `${msg.type}-${idx}`}
            className={msg.type === 'ai' ? 'ai-message-enter' : 'message-enter'}
          >
            {msg.type === 'ai' ? (
              <AIMessage text={msg.text} />
            ) : (
              <UserMessage text={msg.text} />
            )}
          </div>
        ))}
        
        {/* Typing indicator during loading */}
        {isLoading && (
          <div className="message-enter">
            <AIMessage isTyping={true} />
          </div>
        )}
        
        {/* Invisible div for auto-scroll target */}
        <div ref={messagesEndRef} />
      </div>
    </div>
  );
}

