export const seed = {
  aiSnapshot: {
    kpi: { label: 'Revenue today', value: '$3,420', delta: '+4.1%' },
    spark: { label: 'ROAS yesterday', value: '3.1x' },
    sections: {
      summary: 'Revenue is trending up, driven by stable CPC and a small AOV lift from bundles.',
      drivers: ['CTR +9% after creative refresh', 'Prospecting CPA −6% on Meta LAL 2%'],
      suggestions: ['Shift +10–15% budget to best ROAS ad sets', 'Trial a bundle-focused headline on retargeting']
    }
  },
  userQuestion: 'Which campaign has the lowest CPC right now?',
  aiLowestCpc: {
    title: 'Meta • Prospecting LAL 2%',
    now: true,
    stats: { spend: '$840', roas: '3.4x', cpc: '$0.62' },
    tip: 'Tip: Shift +10% from high CPC ad set “Stack_3” into this one.'
  }
};
