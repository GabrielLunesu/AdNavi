'use client'

import { useState } from 'react';
import { RefreshCw, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';
import { syncGoogleEntities, syncGoogleMetrics } from '@/lib/api';

/**
 * Google Ads Sync Button Component
 * 
 * WHAT: Button that triggers Google Ads data sync (entities + metrics)
 * WHY: User-initiated sync in Settings for Google connections
 * REFERENCES: docs/living-docs/GOOGLE_INTEGRATION_STATUS.MD
 */
export default function GoogleSyncButton({ workspaceId, connectionId, onSyncComplete = null }) {
  const [syncing, setSyncing] = useState(false);
  const [status, setStatus] = useState(null); // 'success' | 'error' | null
  const [message, setMessage] = useState('');
  const [stats, setStats] = useState(null);

  const handleSync = async () => {
    if (syncing) return;

    setSyncing(true);
    setStatus(null);
    setMessage('Syncing Google entities...');
    setStats(null);

    try {
      // Step 1: Sync entities
      const entityResult = await syncGoogleEntities({ workspaceId, connectionId });

      if (!entityResult.success) {
        throw new Error(entityResult.errors?.[0] || 'Entity sync failed');
      }

      setMessage(`Synced ${entityResult.synced.campaigns_created + entityResult.synced.campaigns_updated} campaigns, ${entityResult.synced.adsets_created + entityResult.synced.adsets_updated} ad groups, ${entityResult.synced.ads_created + entityResult.synced.ads_updated} ads. Syncing metrics...`);

      // Step 2: Sync metrics
      const metricsResult = await syncGoogleMetrics({ workspaceId, connectionId });

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
      console.error('Google sync error:', error);
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
            <span>Sync Google Ads</span>
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
            {stats.entities.adsets_created + stats.entities.adsets_updated} ad groups,{' '}
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

