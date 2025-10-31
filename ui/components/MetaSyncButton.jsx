'use client'

import { useState } from 'react';
import { RefreshCw, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';
import { syncMetaEntities, syncMetaMetrics } from '@/lib/api';

/**
 * Meta Ads Sync Button Component
 * 
 * WHAT: Button that triggers Meta Ads data sync (entities + metrics)
 * WHY: User-initiated sync from UI
 * WHERE USED: Settings page, Dashboard (future)
 * 
 * Features:
 * - Two-step sync: entities first, then metrics
 * - Loading states with progress feedback
 * - Error handling with user-friendly messages
 * - Success feedback with sync stats
 */
export default function MetaSyncButton({ workspaceId, connectionId, onSyncComplete = null }) {
  const [syncing, setSyncing] = useState(false);
  const [status, setStatus] = useState(null); // 'success' | 'error' | null
  const [message, setMessage] = useState('');
  const [stats, setStats] = useState(null);

  const handleSync = async () => {
    if (syncing) return;
    
    setSyncing(true);
    setStatus(null);
    setMessage('Syncing entities...');
    setStats(null);

    try {
      // Step 1: Sync entities
      const entityResult = await syncMetaEntities({ workspaceId, connectionId });
      
      if (!entityResult.success) {
        throw new Error(entityResult.errors?.[0] || 'Entity sync failed');
      }

      setMessage(`Synced ${entityResult.synced.campaigns_created + entityResult.synced.campaigns_updated} campaigns, ${entityResult.synced.adsets_created + entityResult.synced.adsets_updated} adsets, ${entityResult.synced.ads_created + entityResult.synced.ads_updated} ads. Syncing metrics...`);

      // Step 2: Sync metrics
      const metricsResult = await syncMetaMetrics({ workspaceId, connectionId });

      if (!metricsResult.success) {
        throw new Error(metricsResult.errors?.[0] || 'Metrics sync failed');
      }

      setStatus('success');
      setMessage(`Sync complete! Ingested ${metricsResult.synced.facts_ingested} metric facts.`);
      setStats({
        entities: entityResult.synced,
        metrics: metricsResult.synced,
        duration: (entityResult.synced.duration_seconds + metricsResult.synced.duration_seconds).toFixed(1)
      });

      if (onSyncComplete) {
        onSyncComplete({ entityResult, metricsResult });
      }

    } catch (error) {
      setStatus('error');
      setMessage(error.message || 'Sync failed. Please try again.');
      console.error('Sync error:', error);
    } finally {
      setSyncing(false);
    }
  };

  return (
    <div className="space-y-2">
      <button
        onClick={handleSync}
        disabled={syncing}
        className={`
          inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium
          transition-all disabled:opacity-50 disabled:cursor-not-allowed
          ${syncing 
            ? 'bg-neutral-100 text-neutral-600 cursor-wait' 
            : status === 'success'
            ? 'bg-emerald-50 text-emerald-700 hover:bg-emerald-100 border border-emerald-200'
            : status === 'error'
            ? 'bg-red-50 text-red-700 hover:bg-red-100 border border-red-200'
            : 'bg-cyan-50 text-cyan-700 hover:bg-cyan-100 border border-cyan-200'
          }
        `}
      >
        {syncing ? (
          <>
            <Loader2 className="w-4 h-4 animate-spin" />
            <span>Syncing...</span>
          </>
        ) : status === 'success' ? (
          <>
            <CheckCircle2 className="w-4 h-4" />
            <span>Sync Complete</span>
          </>
        ) : status === 'error' ? (
          <>
            <AlertCircle className="w-4 h-4" />
            <span>Sync Failed</span>
          </>
        ) : (
          <>
            <RefreshCw className="w-4 h-4" />
            <span>Sync Meta Ads</span>
          </>
        )}
      </button>

      {message && (
        <p className={`text-xs ${status === 'error' ? 'text-red-600' : status === 'success' ? 'text-emerald-600' : 'text-neutral-600'}`}>
          {message}
        </p>
      )}

      {stats && status === 'success' && (
        <div className="text-xs text-neutral-500 space-y-1 mt-2 p-2 bg-neutral-50 rounded border border-neutral-200">
          <div>Duration: {stats.duration}s</div>
          <div>
            Entities: {stats.entities.campaigns_created + stats.entities.campaigns_updated} campaigns,{' '}
            {stats.entities.adsets_created + stats.entities.adsets_updated} adsets,{' '}
            {stats.entities.ads_created + stats.entities.ads_updated} ads
          </div>
          <div>
            Metrics: {stats.metrics.facts_ingested} facts ingested
            {stats.metrics.facts_skipped > 0 && `, ${stats.metrics.facts_skipped} skipped`}
          </div>
        </div>
      )}
    </div>
  );
}

