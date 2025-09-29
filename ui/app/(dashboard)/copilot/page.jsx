"use client";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import { fetchQA } from "@/lib/api";
import { motion } from "framer-motion";
import ChatInput from "@/components/ui/ChatInput";
import { currentUser } from "@/lib/auth";

// WHY: Dedicated page to display chat Q&A.
// Reads query params (?q= & ws=), calls API, shows loader then result.

export default function CopilotPage() {
  const searchParams = useSearchParams();
  const question = searchParams.get("q");
  const workspaceId = searchParams.get("ws");

  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState(null);
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

  useEffect(() => {
    if (!question || !resolvedWs) return;
    setLoading(true);
    setErr(null);
    fetchQA({ workspaceId: resolvedWs, question })
      .then(setAnswer)
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

      {/* Question box */}
      {question && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mb-4 p-4 rounded-lg bg-neutral-900 border border-neutral-700"
        >
          <div className="text-sm text-neutral-400">You asked:</div>
          <div className="mt-1 text-base">{question}</div>
        </motion.div>
      )}

      {/* Loader */}
      {loading && (
        <div className="flex justify-center items-center py-12">
          <motion.div
            className="h-8 w-8 border-4 border-emerald-500 border-t-transparent rounded-full"
            initial={{ rotate: 0 }}
            animate={{ rotate: 360 }}
            transition={{ repeat: Infinity, duration: 1, ease: "linear" }}
          />
        </div>
      )}

      {/* Error */}
      {err && <div className="text-red-400">Error: {err}</div>}

      {/* Answer */}
      {answer && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
          className="p-4 rounded-lg bg-neutral-800 border border-neutral-700"
        >
          <div className="text-sm text-neutral-400">Copilot says:</div>
          <div className="mt-1 text-base">{answer.answer}</div>
        </motion.div>
      )}

      {/* Persistent chat input */}
      <div className="mt-8">
        <ChatInput workspaceId={resolvedWs || ""} />
      </div>
    </main>
  );
}
