export const chartLabels = ['Mar 1','Mar 3','Mar 5','Mar 7','Mar 9','Mar 11','Mar 13'];
export const revenue = [4200,4600,4800,5100,5200,5600,5710];
export const spend = [1100,1180,1120,1080,1040,1030,990];
export const roas = revenue.map((r,i)=>Number((r/spend[i]).toFixed(2)));
