export const campaignDetails = {
  'cmp-meta-prospecting-lal2': {
    platform: 'Meta Ads',
    childLabel: 'Ad Sets',
    kpis: { revenue: 34210, spend: 3920, roas: 4.20, conv: 832 },
    children: [
      { id:'as-lal2-ios', name:'LAL 2% — 25–34 iOS', status:'Active', kpis:{ revenue:18420, spend:3210, roas:5.74, conv:436, cpc:0.92, ctr:3.98 }, trend:[38,40,41,42,44,46,48] },
      { id:'as-lal2-broad', name:'LAL 2% — Broad Mix', status:'Active', kpis:{ revenue:11060, spend:3980, roas:2.78, conv:286, cpc:1.08, ctr:2.91 }, trend:[28,29,30,31,31,32,33] },
      { id:'as-interest-online', name:'Interest — Online Shoppers', status:'Active', kpis:{ revenue:4730, spend:950, roas:4.98, conv:110, cpc:0.86, ctr:3.42 }, trend:[24,25,25,26,27,27,28] }
    ]
  },
  'cmp-google-brand': {
    platform: 'Google Ads',
    childLabel: 'Ad Groups',
    kpis: { revenue: 62340, spend: 12480, roas: 4.99, conv: 1128 },
    children: [
      { id:'ag-brand-core', name:'Brand Core', status:'Active', kpis:{ revenue:38210, spend:8120, roas:4.71, conv:712, cpc:1.06, ctr:5.02 }, trend:[40,42,45,46,48,50,52] },
      { id:'ag-brand-longtail', name:'Brand Longtail', status:'Active', kpis:{ revenue:24130, spend:4360, roas:5.53, conv:416, cpc:1.19, ctr:3.54 }, trend:[30,31,33,35,36,37,39] }
    ]
  },
  'cmp-meta-retarget-30d': {
    platform: 'Meta Ads',
    childLabel: 'Ad Sets',
    kpis: { revenue: 24980, spend: 3920, roas: 6.37, conv: 612 },
    children: [
      { id:'as-rtg-top', name:'Top Visitors', status:'Active', kpis:{ revenue:15480, spend:1920, roas:8.06, conv:380, cpc:0.54, ctr:4.72 }, trend:[32,33,34,36,37,38,39] },
      { id:'as-rtg-mid', name:'Recent Visitors', status:'Active', kpis:{ revenue:9500, spend:2000, roas:4.75, conv:232, cpc:0.74, ctr:4.10 }, trend:[28,28,29,30,31,31,32] }
    ]
  }
};
