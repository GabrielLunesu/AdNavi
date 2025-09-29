"use client";
import { useSearchParams } from "next/navigation";
import { useEffect, useMemo, useState } from "react";
import { fetchQA, fetchQaLog } from "@/lib/api";
import { motion } from "framer-motion";
import ChatInput from "@/components/ui/ChatInput";
import { currentUser } from "@/lib/auth";
import { UserBubble, AiBubble } from "@/components/ui/ChatBubble";

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
      .catch(() => {});
  }, [resolvedWs]);

  // If a question is passed via query, append it and ask immediately
  useEffect(() => {
    if (!question || !resolvedWs) return;
    const q = question.trim();
    if (!q) return;
    setLog((prev) => [...prev, { id: Date.now(), question_text: q, answer_text: null }]);
    setLoading(true);
    setErr(null);
    fetchQA({ workspaceId: resolvedWs, question: q })
      .then((res) => {
        setLog((prev) =>
          prev.map((e) => (e.question_text === q && e.answer_text === null ? { ...e, answer_text: res.answer } : e))
        );
      })
      .catch((e) => setErr(e.message))
      .finally(() => setLoading(false));
  }, [question, resolvedWs]);

  return (
    <main className="p-6 max-w-4xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="mb-6"
      >
        <h1 className="text-xl font-semibold">Copilot</h1>
        <p className="text-sm text-neutral-400 mt-1">Your marketing data assistant</p>
      </motion.div>

      {/* Chat thread */}
      <div className="flex flex-col space-y-1">
        {log.map((entry) => (
          <div key={entry.id} className="flex flex-col">
            <UserBubble text={entry.question_text} />
            {entry.answer_text && <AiBubble text={entry.answer_text} />}
          </div>
        ))}
        {loading && (
          <motion.div
            className="self-start text-neutral-400 text-sm px-4 py-2"
            initial={{ opacity: 0.5 }}
            animate={{ opacity: 1 }}
            transition={{ repeat: Infinity, duration: 1, ease: "easeInOut" }}
          >
            Typing…
          </motion.div>
        )}
        {err && <div className="text-red-400">Error: {err}</div>}
      </div>

      {/* Persistent chat input */}
      <div className="mt-8">
        <ChatInput workspaceId={resolvedWs || ""} />
      </div>
    </main>
  );
}
