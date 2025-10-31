'use client'

import { useEffect, useState } from 'react';
import { Settings, RefreshCw, ExternalLink, Calendar } from 'lucide-react';
import { currentUser } from '@/lib/auth';
import { fetchConnections } from '@/lib/api';
import MetaSyncButton from '@/components/MetaSyncButton';

/**
 * Settings Page
 * 
 * WHAT: Display and manage connected ad platform accounts
 * WHY: Users need to see their connections and trigger syncs
 * WHERE USED: /settings route
 * 
 * Features:
 * - List all connected ad accounts (Meta, Google, TikTok, etc.)
 * - Sync button for each Meta connection
 * - Connection status and metadata display
 * - Last sync timestamp
 */
export default function SettingsPage() {
  const [user, setUser] = useState(null);
  const [connections, setConnections] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let mounted = true;

    const loadData = async () => {
      try {
        const currentUserData = await currentUser();
        if (!mounted) return;

        setUser(currentUserData);

        if (currentUserData?.workspace_id) {
          const connectionsData = await fetchConnections({ 
            workspaceId: currentUserData.workspace_id 
          });
          if (mounted) {
            setConnections(connectionsData.connections || []);
          }
        }
      } catch (err) {
        if (mounted) {
          setError(err.message || 'Failed to load settings');
          console.error('Settings load error:', err);
        }
      } finally {
        if (mounted) {
          setLoading(false);
        }
      }
    };

    loadData();

    return () => {
      mounted = false;
    };
  }, []);

  const handleSyncComplete = () => {
    // Refresh connections after sync
    if (user?.workspace_id) {
      fetchConnections({ workspaceId: user.workspace_id })
        .then(data => setConnections(data.connections || []))
        .catch(err => console.error('Failed to refresh connections:', err));
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'Never';
    try {
      const date = new Date(dateString);
      return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } catch {
      return 'Invalid date';
    }
  };

  const getProviderLabel = (provider) => {
    const labels = {
      meta: 'Meta Ads',
      google: 'Google Ads',
      tiktok: 'TikTok Ads',
      other: 'Other'
    };
    return labels[provider] || provider;
  };

  const getProviderIcon = (provider) => {
    // Simple emoji-based icons for now
    const icons = {
      meta: '📘',
      google: '🔍',
      tiktok: '🎵',
      other: '🔗'
    };
    return icons[provider] || '📊';
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto p-8">
        <div className="flex items-center gap-3 mb-8">
          <Settings className="w-6 h-6 text-neutral-600" />
          <h1 className="text-2xl font-semibold text-neutral-900">Settings</h1>
        </div>
        <div className="animate-pulse space-y-4">
          <div className="h-32 bg-neutral-100 rounded-xl"></div>
          <div className="h-32 bg-neutral-100 rounded-xl"></div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-4xl mx-auto p-8">
        <div className="flex items-center gap-3 mb-8">
          <Settings className="w-6 h-6 text-neutral-600" />
          <h1 className="text-2xl font-semibold text-neutral-900">Settings</h1>
        </div>
        <div className="p-4 bg-red-50 border border-red-200 rounded-xl text-red-700">
          Error: {error}
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-8">
      {/* Header */}
      <div className="flex items-center gap-3 mb-8">
        <Settings className="w-6 h-6 text-neutral-600" />
        <h1 className="text-2xl font-semibold text-neutral-900">Settings</h1>
      </div>

      {/* Connected Accounts Section */}
      <div className="mb-8">
        <h2 className="text-lg font-semibold text-neutral-900 mb-4">Connected Ad Accounts</h2>
        
        {connections.length === 0 ? (
          <div className="p-8 bg-neutral-50 border border-neutral-200 rounded-xl text-center text-neutral-600">
            <p className="mb-2">No ad accounts connected yet.</p>
            <p className="text-sm">Connect your ad platforms to start syncing data.</p>
          </div>
        ) : (
          <div className="space-y-4">
            {connections.map((connection) => (
              <div
                key={connection.id}
                className="p-6 bg-white border border-neutral-200 rounded-xl shadow-sm hover:shadow-md transition-shadow"
              >
                <div className="flex items-start justify-between mb-4">
                  <div className="flex items-start gap-4">
                    <div className="text-3xl">{getProviderIcon(connection.provider)}</div>
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <h3 className="text-lg font-semibold text-neutral-900">
                          {connection.name || getProviderLabel(connection.provider)}
                        </h3>
                        <span className={`px-2 py-1 text-xs font-medium rounded-full ${
                          connection.status === 'active'
                            ? 'bg-emerald-100 text-emerald-700'
                            : connection.status === 'inactive'
                            ? 'bg-neutral-100 text-neutral-700'
                            : 'bg-red-100 text-red-700'
                        }`}>
                          {connection.status || 'unknown'}
                        </span>
                      </div>
                      <p className="text-sm text-neutral-600 mb-2">
                        {getProviderLabel(connection.provider)}
                        {connection.external_account_id && (
                          <span className="ml-2 font-mono text-xs">
                            ({connection.external_account_id})
                          </span>
                        )}
                      </p>
                      <div className="flex items-center gap-4 text-xs text-neutral-500">
                        <div className="flex items-center gap-1">
                          <Calendar className="w-3 h-3" />
                          <span>Connected: {formatDate(connection.connected_at)}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Sync Button for Meta Ads */}
                {connection.provider === 'meta' && connection.status === 'active' && (
                  <div className="mt-4 pt-4 border-t border-neutral-200">
                    <MetaSyncButton
                      workspaceId={user.workspace_id}
                      connectionId={connection.id}
                      onSyncComplete={handleSyncComplete}
                    />
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Info Section */}
      <div className="p-6 bg-neutral-50 border border-neutral-200 rounded-xl">
        <h3 className="text-sm font-semibold text-neutral-900 mb-2">About Syncing</h3>
        <p className="text-sm text-neutral-600 mb-2">
          Syncing fetches the latest campaigns, ad sets, and ads from your Meta Ads account,
          along with performance metrics for the last 90 days.
        </p>
        <p className="text-sm text-neutral-600">
          The sync process may take a few minutes depending on the size of your account.
          Large accounts with many campaigns may take longer.
        </p>
      </div>
    </div>
  );
}

