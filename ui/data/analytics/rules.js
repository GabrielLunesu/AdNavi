export const rules = [
  { parts:['ROAS','below','1.50×','→ Notify:','Email','In-app'], scope:'(Scope: this campaign)' },
  { parts:['CTR','below','2.5%','for 48h','→ Notify:','In-app',', Suggest creative swap'] },
  { parts:['CPC','above','$1.20','for 24h','→ Notify:','Slack',', Propose bid cap'] },
  { parts:['Conversions','drop >25% WoW','→ Notify:','Email',', Auto-run diagnosis'] },
  { parts:['Spend','variance >20% vs plan','→ Notify:','In-app',', Flag in Finance'] },
];
export const history = [
  { text:'CTR below 2.5% for 48h on “Broad Mix”', status:'Snoozed' },
  { text:'ROAS below 1.50× on “Static — C-07”',   status:'Resolved' },
  { text:'Spend variance >20% vs plan',            status:'Open' },
];
