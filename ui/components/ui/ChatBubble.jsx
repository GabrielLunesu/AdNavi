import { motion } from "framer-motion";

// WHY: Separate bubbles for user vs AI to keep styling clean and reusable.
export function UserBubble({ text }) {
  return (
    <motion.div
      initial={{ opacity: 0, x: 50 }}
      animate={{ opacity: 1, x: 0 }}
      className="self-end max-w-[70%] rounded-2xl bg-emerald-600 text-white px-4 py-2 mb-2"
    >
      {text}
    </motion.div>
  );
}

export function AiBubble({ text }) {
  return (
    <motion.div
      initial={{ opacity: 0, x: -50 }}
      animate={{ opacity: 1, x: 0 }}
      className="self-start max-w-[70%] rounded-2xl bg-neutral-800 text-white px-4 py-2 mb-2 border border-neutral-700"
    >
      {text}
    </motion.div>
  );
}


