"use client";
import { useSearchParams } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { fetchQA } from "@/lib/api";
import { currentUser } from "@/lib/auth";
import SnapshotHeader from "./components/SnapshotHeader";
import InsightCards from "./components/InsightCards";
import FactWidgets from "./components/FactWidgets";
import ConversationThread from "./components/ConversationThread";
import { renderMarkdownLite } from "@/lib/markdown";
import ChatConsole from "./components/ChatConsole";

export default function CopilotPage() {
  const searchParams = useSearchParams();
  const question = searchParams.get("q");
  const workspaceId = searchParams.get("ws");

  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState([]);
  const [resolvedWs, setResolvedWs] = useState(workspaceId || null);
  const processedRef = useRef(false);

  // Resolve workspace id from session if not present in URL
  useEffect(() => {
    if (workspaceId) {
      setResolvedWs(workspaceId);
      return;
    }
    let mounted = true;
    currentUser()
      .then((u) => {
        if (!mounted) return;
        setResolvedWs(u?.workspace_id || null);
      })
      .catch(() => setResolvedWs(null));
    return () => {
      mounted = false;
    };
  }, [workspaceId]);

  // Process URL question parameter
  useEffect(() => {
    if (!resolvedWs || !question || processedRef.current) return;
    processedRef.current = true;
    handleSubmit(question.trim());
  }, [question, resolvedWs]);

  const handleSubmit = (q) => {
    if (!resolvedWs || !q.trim() || loading) return;
    
    // Add user message immediately with timestamp (optimistic UI)
    const userMessage = {
      type: 'user',
      text: q,
      timestamp: Date.now()
    };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    fetchQA({ workspaceId: resolvedWs, question: q })
      .then((res) => {
        // Add AI response with timestamp
        const aiMessage = {
          type: 'ai',
          text: renderMarkdownLite(res.answer),
          timestamp: Date.now()
        };
        setMessages((prev) => [...prev, aiMessage]);
      })
      .catch((e) => {
        // Show error as AI message for better UX
        const errorMessage = {
          type: 'ai',
          text: `I encountered an error: ${e.message}. Please try again.`,
          timestamp: Date.now(),
          isError: true
        };
        setMessages((prev) => [...prev, errorMessage]);
      })
      .finally(() => setLoading(false));
  };

  return (
    <main className="flex-1 pt-12 pb-32 px-8 max-w-5xl mx-auto page-transition">
      {/* AI Header Section */}
      <SnapshotHeader />

      {/* Insight Stack */}
      {/* <InsightCards /> */}

      {/* Real-time Fact Widgets */}
      {/* <FactWidgets /> */}

      {/* Conversation History */}
      <ConversationThread messages={messages} isLoading={loading} />

      {/* Floating Conversation Console */}
      <ChatConsole onSubmit={handleSubmit} disabled={loading || !resolvedWs} />
    </main>
  );
}
