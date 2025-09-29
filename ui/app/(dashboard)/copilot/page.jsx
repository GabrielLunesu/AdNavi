"use client";
import { useSearchParams } from "next/navigation";
import { useEffect, useMemo, useRef, useState } from "react";
import { fetchQA, fetchQaLog } from "@/lib/api";
import { motion } from "framer-motion";
import { currentUser } from "@/lib/auth";
import { UserBubble, AiBubble } from "@/components/ui/ChatBubble";
import ChatComposer from "@/components/ui/ChatComposer";

// WHY: Dedicated page to display chat Q&A.
// Reads query params (?q= & ws=), calls API, shows loader then result.

export default function CopilotPage() {
  const searchParams = useSearchParams();
  const question = searchParams.get("q");
  const workspaceId = searchParams.get("ws");

  const [loading, setLoading] = useState(false);
  const [log, setLog] = useState([]);
  const [err, setErr] = useState(null);
  const [resolvedWs, setResolvedWs] = useState(workspaceId || null);
  const processedRef = useRef(false); // guard to process ?q only once per mount
  const [historyLoaded, setHistoryLoaded] = useState(false);
  const chatRef = useRef(null); // scroll container
  const scrollToBottom = (behavior = "auto") => {
    if (!chatRef.current) return;
    chatRef.current.scrollTo({ top: chatRef.current.scrollHeight, behavior });
  };

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

  // Load chat history when workspace is resolved
  useEffect(() => {
    if (!resolvedWs) return;
    fetchQaLog(resolvedWs)
      .then((rows) => setLog(rows.reverse())) // oldest first for natural flow
      .catch(() => {})
      .finally(() => setHistoryLoaded(true));
  }, [resolvedWs]);

  // If ?q is present, only process once per mount and only if not already in history
  useEffect(() => {
    if (!resolvedWs) return;
    if (!question) return;
    if (!historyLoaded) return;
    if (processedRef.current) return;

    const q = question.trim();
    if (!q) {
      processedRef.current = true;
      return;
    }

    const alreadyInLog = log.some((e) => (e.question_text || "").trim().toLowerCase() === q.toLowerCase() && e.answer_text != null);
    processedRef.current = true;
    if (alreadyInLog) return; // do not re-send duplicate question

    handleSubmit(q);
  }, [question, resolvedWs, historyLoaded, log]);

  // Ensure scrolled to bottom on initial history load and when messages change
  useEffect(() => {
    if (historyLoaded) scrollToBottom("auto");
  }, [historyLoaded]);
  useEffect(() => {
    if (historyLoaded) scrollToBottom("smooth");
  }, [log.length]);

  const handleSubmit = (q) => {
    if (!resolvedWs) return;
    setLog((prev) => [...prev, { id: Date.now(), question_text: q, answer_text: null }]);
    setLoading(true);
    setErr(null);
    fetchQA({ workspaceId: resolvedWs, question: q })
      .then((res) => {
        setLog((prev) => prev.map((e) => (e.question_text === q && e.answer_text === null ? { ...e, answer_text: res.answer } : e)));
      })
      .catch((e) => setErr(e.message))
      .finally(() => setLoading(false));
  };

  return (
    <main className="h-screen gradient-bg text-white overflow-hidden">
      <div className="max-w-5xl mx-auto h-full flex flex-col gap-4 md:gap-6 p-6 md:p-8">
        {/* Context Bar */}
        <div className="rounded-xl px-4 py-3 border border-slate-700/40 flex items-center justify-between bg-slate-800/30 backdrop-blur">
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2">
              <span className="text-slate-400 text-xs">{resolvedWs ? "Workspace" : "Resolving..."}</span>
              <span className="text-sm text-slate-200">{resolvedWs}</span>
            </div>
            <div className="hidden sm:block w-px h-4 bg-slate-700/40"></div>
           
          </div>
          <div className="flex items-center gap-2">
            <div className="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-[0_0_12px_2px_rgba(16,185,129,0.6)]" />
            <span className="text-xs text-slate-400">Context synced</span>
          </div>
        </div>

        {/* Chat Container */}
        <div className="rounded-2xl border border-slate-700/40 flex flex-col max-h-2/3 overflow-hidden bg-slate-900/40 backdrop-blur relative flex-1">

          {/* Top fade overlay for blend-in */}
          <div className="pointer-events-none absolute inset-x-0 top-0 h-24 bg-gradient-to-b from-slate-900/80 via-slate-900/40 to-transparent z-10" />

          {/* Messages Scroll */}
          <div ref={chatRef} className="flex-1 overflow-y-auto overflow-x-hidden px-3 sm:px-5 pb-40 pt-6 space-y-3 no-scrollbar">
            <div className="flex flex-col space-y-1">
              {log.map((entry) => (
                <div key={entry.id} className="flex flex-col">
                  <UserBubble text={entry.question_text} />
                  {entry.answer_text && <AiBubble text={entry.answer_text} />}
                </div>
              ))}
              {loading && (
                <motion.div className="self-start text-neutral-400 text-sm px-4 py-2" initial={{ opacity: 0.5 }} animate={{ opacity: 1 }} transition={{ repeat: Infinity, duration: 1, ease: "easeInOut" }}>
                  Typing…
                </motion.div>
              )}
              {err && <div className="text-red-400">Error: {err}</div>}
            </div>
          </div>

          {/* Bottom fade overlay for blend-in */}
          <div className="pointer-events-none absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-slate-900/80 via-slate-900/40 to-transparent z-10" />

          {/* Overlay: suggestions + composer */}
          <div className="absolute bottom-0 inset-x-0 z-20 px-3 sm:px-5 pb-4 pt-4">
            <div className="flex items-center gap-2 overflow-x-auto pb-2 no-scrollbar">
              {["How much revenue today?", "Show me conversions vs last week.", "Which campaign has the lowest CPC?"].map((s) => (
                <button key={s} className="shrink-0 px-3 py-1.5 rounded-full bg-slate-900/40 border border-slate-700/40 text-xs text-slate-300 hover:text-white hover:border-cyan-400/40 hover:shadow-[0_0_24px_rgba(56,189,248,0.25)] transition-all" onClick={() => handleSubmit(s)}>
                  {s}
                </button>
              ))}
            </div>
            <ChatComposer onSubmit={handleSubmit} disabled={loading || !resolvedWs} />
          </div>
        </div>
      </div>
    </main>
  );
}
